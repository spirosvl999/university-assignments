import numpy as np
import cv2

def load_video_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        frames.append(frame)
    cap.release()
    #print(f"Number of frames loaded: {len(frames)}")
    return frames

def compute_mad(block1, block2):
    return np.mean(np.abs(block1 - block2))

def motion_compensation(reference_frame, current_frame, block_size=64, search_radius=32):
    height, width = reference_frame.shape
    compensated_frame = np.zeros((height, width))

    for y in range(0, height, block_size):
        for x in range(0, width, block_size):
            min_mad = float('inf')
            best_offset = (0, 0)

            for dy in range(-search_radius, search_radius+1):
                for dx in range(-search_radius, search_radius+1):
                    mv_y = y + dy
                    mv_x = x + dx

                    if mv_y < 0 or mv_y + block_size > height or mv_x < 0 or mv_x + block_size > width:
                        continue
                    
                    if(x+block_size>width):
                        ref_block = reference_frame[y:y+block_size,x:width]
                    else:
                        ref_block = reference_frame[y:y+block_size, x:x+block_size]
                    if(x+block_size>width):
                        curr_block = current_frame[y:y+block_size,x:width]
                    else:
                        curr_block = current_frame[mv_y:mv_y+block_size, mv_x:mv_x+block_size]

                    if curr_block.shape != (block_size, block_size):
                        continue
                    
                    #print("Shapes:", ref_block.shape, curr_block.shape)
                    
                    mad = compute_mad(ref_block, curr_block)

                    if mad < min_mad:
                        min_mad = mad
                        best_offset = (dy, dx)

            mv_y, mv_x = best_offset
            compensated_frame[y:y+block_size, x:x+block_size] = current_frame[y+mv_y:y+mv_y+block_size, x+mv_x:x+mv_x+block_size]

    return compensated_frame


def hierarchical_search(reference_frame, current_frame, block_size=64, search_radius=32, max_levels=3):
    predicted_frames = [reference_frame]
    error_frames = []

    for level in range(1, max_levels+1):
        scaled_ref = cv2.resize(predicted_frames[-1], (predicted_frames[-1].shape[1] // 2, predicted_frames[-1].shape[0] // 2))
        scaled_curr = cv2.resize(current_frame, (current_frame.shape[1] // (2 ** level), current_frame.shape[0] // (2 ** level)))

        if level == max_levels:
            predicted_frame = motion_compensation(scaled_ref, scaled_curr, block_size, search_radius)
        else:
            predicted_frame = cv2.resize(predicted_frames[-1], (predicted_frames[-1].shape[1] * 2, predicted_frames[-1].shape[0] * 2))
            predicted_frame = motion_compensation(scaled_ref, predicted_frame, block_size, search_radius)

        predicted_frames.append(predicted_frame)
        error_frame = scaled_curr - predicted_frame
        error_frames.append(error_frame)

    return predicted_frames, error_frames

def encode_motion_vectors(motion_vectors):
    motion_vectors_encoded = []
    for motion_vector in motion_vectors:
        mv_y, mv_x = motion_vector
        mv_y_packed = int((mv_y + 32) * 64) 
        mv_x_packed = int((mv_x + 32) * 64) 
        motion_vectors_encoded.append((mv_y_packed, mv_x_packed))
    return motion_vectors_encoded

def decode_motion_vectors(motion_vectors_encoded):
    motion_vectors = []
    for mv_y_packed, mv_x_packed in motion_vectors_encoded:
        mv_y = (mv_y_packed / 64) - 32
        mv_x = (mv_x_packed / 64) - 32
        motion_vectors.append((mv_y, mv_x))
    return motion_vectors

def encode_video(frames, block_size=64, search_radius=32, max_levels=3):
    encoded_data = []
    reference_frame = frames[0]
    encoded_data.append(reference_frame)

    for frame in frames[1:]:
        predicted_frames, error_frames = hierarchical_search(reference_frame, frame, block_size, search_radius, max_levels)
        motion_vectors = []
        for predicted_frame, error_frame in zip(predicted_frames[1:], error_frames):
            motion_vector = motion_compensation(reference_frame, frame)
            motion_vectors.append(motion_vector)
            reference_frame = predicted_frame

        encoded_data.append(encode_motion_vectors(motion_vectors))
        encoded_data.append(error_frames[-1])

    return encoded_data

def decode_video(encoded_data, block_size=64, search_radius=32, max_levels=3):
    decoded_frames = []
    reference_frame = encoded_data[0]

    for i in range(1, len(encoded_data), 2):
        motion_vectors = decode_motion_vectors(encoded_data[i])
        error_frame = encoded_data[i + 1]

        predicted_frames = [reference_frame]
        for motion_vector in motion_vectors:
            predicted_frame = motion_compensation(reference_frame, error_frame + reference_frame, block_size, search_radius)
            predicted_frames.append(predicted_frame)
            reference_frame = predicted_frame

        decoded_frames.extend(predicted_frames[1:])

    return decoded_frames

video_path = 'C:/Users/User/Desktop/sxolh/Systimata polymeswn/videoplayback_.mp4'               #We load video, and we load the videoframes to start encoding it
video_frames = load_video_frames(video_path)

encoded_data = encode_video(video_frames)                                                       #We start encoding all the video frames

decoded_frames = decode_video(encoded_data)                                                     #We use the encoded data to decode the video

np.save('prediction_frames.npy', encoded_data[::2])                                             #We save prediction frames
np.save('error_frames.npy', encoded_data[1::2])                                                 #We save error_frames

for i, frame in enumerate(encoded_data[::2]):
    cv2.imshow('Prediction Frame {}'.format(i), frame)                                          #We show the prediction frames
    cv2.waitKey(0)
    cv2.destroyAllWindows()