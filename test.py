from ita_converter import *

# Create ASCIIArt object
ascii_art = get_ascii_art("ttt.png", width=100, height=25, color=True, symbol_set=["*", ".", ":", ";", ","])
print(ascii_art)