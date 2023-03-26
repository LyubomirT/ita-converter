# ita-converter

ita-converter is a lightweight and fast Python library that converts an image to ASCII art. It allows users to resize images, convert them to grayscale, and customize the symbols used to create the ASCII art. [View on PyPi!](https://pypi.org/project/ita-converter/)

## Installation

You can install `ita-converter` using pip:
```
pip install ita-converter 
```

## Usage

To use `ita-converter`, simply import the `get_ascii_art()` function and pass in the path to the image file you want to convert. By default, the function will use a set of ASCII characters to create the art, but you can also pass in your own symbol set.

```python
from ita_converter import get_ascii_art

ascii_art = get_ascii_art("path/to/image.png", symbol_set=["@", "#", "*", " "])
print(ascii_art)
```
By default, the function will use color in the output. If you want a black and white output, set `color` to `False`.
```python
ascii_art = get_ascii_art("path/to/image.png", color=False)
print(ascii_art)
```
You can also resize the image and specify the width and height of the output. If you only specify the width, the height will be adjusted automatically to maintain the aspect ratio.
```python
ascii_art = get_ascii_art("path/to/image.png", width=50, height=50)
print(ascii_art)
```
## Contributing

Contributions to `ita-converter` are welcome! If you have an idea for a new feature or want to report a bug, please open an issue. If you want to contribute code, please fork the repository, make your changes, and submit a pull request.

## License

`ita-converter` is licensed under the [MIT License](https://opensource.org/licenses/MIT).