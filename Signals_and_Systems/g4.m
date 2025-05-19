image = 'me.jpg';
num_coeff = 2000;

array = imread(image);
[~, ~, p] = size(array);

if p == 3
    array = rgb2gray(array);
end
    
dbl = double(array);

dft = dct2(dbl);

sqr = (dft).^2;
sqr = sqr(:);
[~,index] = sort(sqr);
index = flipud(index);

compressed_dft = zeros(size(dbl));   

for i = 1:num_coeff
    compressed_dft(index(i)) = dft(index(i));   
end

output = idct2(compressed_dft);
output = uint8(output);

imwrite(output, 'mecompressed.jpg');
subplot 121; imshow(array); title('Before');
subplot 122; imshow(output); title('After');