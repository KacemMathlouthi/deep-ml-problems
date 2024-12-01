import numpy as np

def pad(input_matrix, padding):
    zero_padded = np.pad(input_matrix, (padding,padding), mode='constant', constant_values=0)
    return zero_padded

def convolve(input_matrix, kernel):
    result = 0
    input_height, input_width = input_matrix.shape
    for i in range(input_height):
        for j in range(input_width):
            result += input_matrix[i][j] * kernel[i][j]
    return result

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape

    padded_input = pad(input_matrix, padding)

    output_height = ((input_height + 2*padding - kernel_height) // stride) + 1
    output_width = ((input_width + 2*padding - kernel_width) // stride) + 1
    output_matrix = np.zeros((output_height, output_width))

    for i in range(output_height):
        for j in range(output_width):
            region = padded_input[i * stride:i * stride + kernel_height, j * stride:j * stride + kernel_width]
            output_matrix[i, j] = convolve(region, kernel)
    return output_matrix