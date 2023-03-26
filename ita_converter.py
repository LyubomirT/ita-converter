from PIL import Image
import numpy as np
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100, new_height=None):
    """Resizes the given image to a new width and height while maintaining aspect ratio."""
    (original_width, original_height) = image.size
    if new_height is None:
        aspect_ratio = original_height / float(original_width)
        new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))
    
def get_image_gray_scale(image):
    """Converts the given image to grayscale and returns a numpy array."""
    return np.array(image.convert('L'))

def get_ascii_art(image_path, symbol_set=None, width=100, height=None, color=True):
    """Converts the given image to ASCII art and returns it as a string."""
    if symbol_set is None:
        symbol_set = ASCII_CHARS
    image = Image.open(image_path)
    image = resize_image(image, new_width=width, new_height=height)
    gray_image = get_image_gray_scale(image)
    if color:
        color_image = np.array(image)
        ascii_art = ""
        for i in range(gray_image.shape[0]):
            row = ""
            for j in range(gray_image.shape[1]):
                intensity = gray_image[i, j] / 255
                symbol_index = int(intensity * (len(symbol_set) - 1))
                symbol = symbol_set[symbol_index]
                color = color_image[i, j]
                row += f"\033[38;2;{color[0]};{color[1]};{color[2]}m{symbol}\033[0m"
            ascii_art += row + "\n"
    else:
        ascii_art = ""
        for i in range(gray_image.shape[0]):
            row = ""
            for j in range(gray_image.shape[1]):
                intensity = gray_image[i, j] / 255
                symbol_index = int(intensity * (len(symbol_set) - 1))
                symbol = symbol_set[symbol_index]
                row += symbol
            ascii_art += row + "\n"
    return ascii_art