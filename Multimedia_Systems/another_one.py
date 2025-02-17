import copy
import numpy as np
import cv2
import math




class Node:
    def __init__(self, data):
        self.data = data
        self.frequency = None
        code = None
        self.left = None
        self.right = None


def block_dct(block):
    return cv2.dct(block.astype(np.float32))


def find_node(node, value):
    if node is None or node.data == value:
        return node

    found_node = find_node(node.left, value)
    if found_node is None:
        found_node = find_node(node.right, value)

    return found_node

def chrominance_downsample(sample):
    height, width = sample.shape
    downsample = np.zeros((math.ceil(height / 2), math.ceil(width / 2)), dtype=np.float32)

    for row in range(0, height, 2):
        for col in range(0, width, 2):
            block = sample[row:row + 2, col:col + 2]
            average = np.mean(block)
            downsample[math.ceil(row/2),math.ceil(col/2)] = average

    return  downsample

def quantinize(block , matrix):
    h , w = block.shape
    q_block = np.zeros((h,w),dtype=np.float32)

    for row in range(0, h):
        for col in range(0, w):
            q_block[row][col] = round(block[row][col] / matrix[row][col])
    return q_block

def zigzag_run_length(block):


    rows = len(block)
    cols = len(block[0])

    encoded_list = []
    value = block[0][0]
    count = 1

    row, col = 0, 1
    is_upward = False

    while row < rows and col < cols:
        # If moving upward
        if is_upward:
            while row > 0 and col < cols - 1:
                if block[row][col]!=value:
                    encoded_list.append([value,count])
                    value = block[row][col]
                    count = 1
                else:
                    count += 1
                row -= 1
                col += 1
            if block[row][col] != value:
                encoded_list.append([value, count])
                value = block[row][col]
                count = 1
            else:
                count += 1

            if col == cols - 1:
                row += 1
            else:
                col += 1

        # If moving downward
        else:
            while col > 0 and row < rows - 1:
                if block[row][col] != value:
                    encoded_list.append([value, count])
                    value = block[row][col]
                    count = 1
                else:
                    count += 1
                row += 1
                col -= 1
            if block[row][col] != value:
                encoded_list.append([value, count])
                value = block[row][col]
                count = 1
            else:
                count += 1

            if row == rows - 1:
                col += 1
            else:
                row += 1

        is_upward = not is_upward
    encoded_list.append([value,count])
    return encoded_list

def assign_codes(node,code):
    if node is None:
        return
    node.code = code

    assign_codes(node.left, code + "0")
    assign_codes(node.right, code + "1")

def huffman_encoding(block):

    block.sort(key = lambda x : x[0], reverse=True)
    row = 1
    while row < len(block):
        if block[row][0] == block[row-1][0]:
            block[row-1][1] += block[row][1]
            del(block[row])
        else:
            row += 1
    block.sort(key = lambda x : x[1])

    node_list=[]

    for row in block:
        new_node = Node(row[0])
        new_node.frequency = row[1]
        node_list.append(new_node)


    while len(node_list) > 1:
        min1 = min(node_list , key =lambda node: node.frequency)
        node_list.remove(min1)
        min2 = min(node_list , key =lambda node: node.frequency)
        node_list.remove(min2)
        new_node = Node(None)
        new_node.frequency = min1.frequency+min2.frequency
        new_node.left = min1
        new_node.right = min2
        node_list.append(new_node)
    root = node_list[0]
    assign_codes(root," ")

    return  root

def compress_iframe(frame, block_size=8):

    ycrcb = cv2.cvtColor(frame, cv2.COLOR_RGB2YCrCb)

    # Split the channels
    y, cr, cb = cv2.split(ycrcb)

    downsample_cr = chrominance_downsample(cr)
    downsample_cb = chrominance_downsample(cb)


    yheight, ywidth = y.shape
    cheight , cwidth = downsample_cr.shape


    quantization_matrix_y = [
        [16, 11, 10, 16, 24, 40, 51, 61],
        [12, 12, 14, 19, 26, 58, 60, 55],
        [14, 13, 16, 24, 40, 57, 69, 56],
        [14, 17, 22, 29, 51, 87, 80, 62],
        [18, 22, 37, 56, 68, 109, 103, 77],
        [24, 35, 55, 64, 81, 104, 113, 92],
        [49, 64, 78, 87, 103, 121, 120, 101],
        [72, 92, 95, 98, 112, 100, 103, 99]
    ]

    quantization_matrix_cbcr = [
        [17, 18, 24, 47, 99, 99, 99, 99],
        [18, 21, 26, 66, 99, 99, 99, 99],
        [24, 26, 56, 99, 99, 99, 99, 99],
        [47, 66, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99]
    ]

    compressed_y=[]
    compressed_cr=[]
    compressed_cb=[]


    for row in range(0, yheight, block_size):
        for col in range(0, ywidth, block_size):

            block = y[row:row + block_size, col:col + block_size]
            dct_block = block_dct(block)
            quantinized_block = quantinize(dct_block , quantization_matrix_y)
            zig_zag_block = zigzag_run_length(quantinized_block)
            zig_zag_block_copy = copy.deepcopy(zig_zag_block)
            tree = huffman_encoding(zig_zag_block_copy)
            message = " "
            for i in zig_zag_block:
                node = find_node(tree,i[0])
                message += node.code * i[1]
            message = message.replace(" ","")
            if message =="":
                message = 64 * "0"
                tree.code = "0"
            compressed_y.append((message,tree))


    for row in range(0, cheight, block_size):
        for col in range(0, cwidth, block_size):

            block = cr[row:row + block_size, col:col + block_size]
            dct_block = block_dct(block)
            quantinized_block = quantinize(dct_block, quantization_matrix_cbcr)
            zig_zag_block = zigzag_run_length(quantinized_block)
            zig_zag_block_copy = copy.deepcopy(zig_zag_block)
            tree = huffman_encoding(zig_zag_block_copy)
            message = " "
            for i in zig_zag_block:
                node = find_node(tree, i[0])
                message += node.code * i[1]
            message = message.replace(" ", "")
            compressed_cr.append((message,tree))

            block = cb[row:row + block_size, col:col + block_size]
            dct_block = block_dct(block)
            quantinized_block = quantinize(dct_block, quantization_matrix_cbcr)
            zig_zag_block = zigzag_run_length(quantinized_block)
            zig_zag_block_copy = copy.deepcopy(zig_zag_block)
            tree = huffman_encoding(zig_zag_block_copy)
            message = " "
            for i in zig_zag_block:
                node = find_node(tree, i[0])
                message += node.code * i[1]
            message = message.replace(" ","")
            compressed_cb.append((message, tree))
            print("block" , row , col)
    return compressed_y,compressed_cr,compressed_cb


def huffman_decoding(encoded_message, root):
    decoded_message = []
    current_node = root

    for bit in encoded_message:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.data is not None:
            decoded_message.append(current_node.data)
            current_node = root

    return decoded_message

def reverse_zigzag_run_length(encoded_list):

    rows = 8
    cols = 8
    row = 0
    col = 0
    block = np.zeros((rows,cols),dtype= np.float32)

    is_upward = True
    _ = 0
    while row < rows and col < cols:
        # If moving upward
        if is_upward:
            while row > 0 and col < cols - 1:
                block[row][col] = encoded_list[_]
                _ += 1
                row -= 1
                col += 1
            block[row][col] = encoded_list[_]
            _ += 1

            if col == cols - 1:
                row += 1
            else:
                col += 1

        # If moving downward
        else:
            while col > 0 and row < rows - 1:
                block[row][col] = encoded_list[_]
                _ += 1
                row += 1
                col -= 1
            block[row][col] = encoded_list[_]
            _ += 1

            if row == rows - 1:
                col += 1
            else:
                row += 1

        is_upward = not is_upward
    return block

def reverse_quantinize(q_block , matrix):

    rows , cols = q_block.shape
    block = np.zeros((rows,cols),dtype=np.float32)


    for row in range(0,rows):
        for col in range(0,cols):
            block[row][col] =q_block[row][col] * matrix[row][col]

    return block

def block_idct(block):
    return cv2.idct(block.astype(np.float32))

def chrominance_upsample(block):
    height, width = block.shape
    upsample = np.zeros((height * 2, width * 2), dtype=np.float32)

    for row in range(0, height):
        for col in range(0, width):
            upsample[row*2:row*2+2, col*2:col*2+2] = block[row, col]

    return upsample
def decompress_iframe(compressed_y , compressed_cr , compressed_cb , block_size , image_shape ):

    yheight, ywidth = image_shape
    cheight, cwidth = math.ceil(image_shape[0] / 2), math.ceil(image_shape[1] / 2)

    quantization_matrix_y = [
        [16, 11, 10, 16, 24, 40, 51, 61],
        [12, 12, 14, 19, 26, 58, 60, 55],
        [14, 13, 16, 24, 40, 57, 69, 56],
        [14, 17, 22, 29, 51, 87, 80, 62],
        [18, 22, 37, 56, 68, 109, 103, 77],
        [24, 35, 55, 64, 81, 104, 113, 92],
        [49, 64, 78, 87, 103, 121, 120, 101],
        [72, 92, 95, 98, 112, 100, 103, 99]
    ]

    quantization_matrix_cbcr = [
        [17, 18, 24, 47, 99, 99, 99, 99],
        [18, 21, 26, 66, 99, 99, 99, 99],
        [24, 26, 56, 99, 99, 99, 99, 99],
        [47, 66, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99],
        [99, 99, 99, 99, 99, 99, 99, 99]
    ]

    decompressed_y = np.zeros((yheight, ywidth), dtype=np.float32)
    decompressed_cr = np.zeros((cheight, cwidth), dtype=np.float32)
    decompressed_cb = np.zeros((cheight, cwidth), dtype=np.float32)

    c = 0
    block_count = 0

    for row in range(0,len(compressed_y)):
        row_message = compressed_y[row][0]
        row_message_tree = compressed_y[row][1]
        zig_zag_block = huffman_decoding(row_message,row_message_tree)
        quantinized_block = reverse_zigzag_run_length(zig_zag_block)
        dct_block = reverse_quantinize(quantinized_block,quantization_matrix_y)
        block = block_idct(dct_block)
        decompressed_y[c*block_size:c*block_size+block_size,block_count*block_size:block_count*block_size+block_size] = block
        block_count +=1
        if block_count*block_size >= ywidth:
            c += 1
            block_count=0

    c = 0
    block_count = 0

    for row in range(0, len(compressed_cr)):
        row_message = compressed_cr[row][0]
        row_message_tree = compressed_cr[row][1]
        zig_zag_block = huffman_decoding(row_message, row_message_tree)
        quantinized_block = reverse_zigzag_run_length(zig_zag_block)
        dct_block = reverse_quantinize(quantinized_block, quantization_matrix_y)
        block = block_idct(dct_block)
        decompressed_cr[c * block_size:c * block_size + block_size,
        block_count * block_size:block_count * block_size + block_size] = block
        block_count += 1
        if block_count * block_size >= cwidth:
            c += 1
            block_count = 0


    c = 0
    block_count = 0

    for row in range(0, len(compressed_cb)):
        row_message = compressed_cb[row][0]
        row_message_tree = compressed_cb[row][1]
        zig_zag_block = huffman_decoding(row_message, row_message_tree)
        quantinized_block = reverse_zigzag_run_length(zig_zag_block)
        dct_block = reverse_quantinize(quantinized_block, quantization_matrix_y)
        block = block_idct(dct_block)
        decompressed_cb[c * block_size:c * block_size + block_size,
        block_count * block_size:block_count * block_size + block_size] = block
        block_count += 1
        if block_count * block_size >= cwidth:
            c += 1
            block_count = 0

    upsampled_cr = chrominance_upsample(decompressed_cr)
    upsampled_cb = chrominance_upsample(decompressed_cb)


    ycrcb = cv2.merge([decompressed_y,upsampled_cr,upsampled_cb])
    frame = cv2.cvtColor(ycrcb,cv2.COLOR_YCrCb2RGB)

    return frame

def video_to_frames(video_path, path ):
    video = cv2.VideoCapture(video_path)

    frame_count = 0

    success, frame = video.read()
    frames= []
    while success:
        frame_filename = f"{path}/frame_{frame_count}.jpg"
        frames.append(frame_filename)
        cv2.imwrite(frame_filename, frame)

        success, frame = video.read()
        frame_count += 1

    video.release()
    return  frames

def frames_to_video(frames, output_path, fps=15):
    frame = frames[0]
    height, width, _ = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame in frames:

        video_writer.write(frame)

    video_writer.release()

def get_residual_frame(current_frame, reference_frame):
    residual_frame = cv2.absdiff(current_frame, reference_frame)


    return residual_frame


def reconstruct_frame(reference_frame, residual_frame):

    reconstructed_frame = np.clip(reference_frame + residual_frame, 0, 255).astype(np.uint8)

    return reconstructed_frame
def make_residual_video(frames,residual_frames):
    for frame_path in range(1, len(frames)):
        frame = cv2.imread(frames[frame_path])
        reference_frame = cv2.imread(frames[frame_path - 1])
        residual_frame = get_residual_frame(frame, reference_frame)
        residual_frames.append(residual_frame)

    output_path = "vid/residual_video.mp4"

    frames_to_video(residual_frames, output_path)

video_path = "vid/Untitled video.mp4"
frame_path = "vid/frames"

frames = video_to_frames(video_path, frame_path )
first_frame = cv2.imread(frames[0])

compressed_y , compressed_cr , compressed_cb = compress_iframe(first_frame)

residual_frames = []
make_residual_video(frames,residual_frames)

compressed_residual_y =[]
compressed_residual_cr =[]
compressed_residual_cb = []

for frame in residual_frames:
    t1 ,t2 ,t3 =compress_iframe(frame)
    compressed_residual_y.append(t1)
    compressed_residual_cr.append(t2)
    compressed_residual_cb.append(t3)

decompressed_first_frame = decompress_iframe(compressed_y , compressed_cr , compressed_cb ,  8 , first_frame.shape[0:2])
decompressed_vid = decompressed_first_frame

for i in range (0,len(compressed_residual_y)):
    decompressed_residual_frame = decompress_iframe(compressed_residual_y[0],compressed_residual_cr[0],compressed_residual_cb[0],8,first_frame.shape[0:2])
    decompressed_vid.append(decompressed_residual_frame)

frames_to_video(decompressed_vid,"vid/output.mp4" , fps =15)
