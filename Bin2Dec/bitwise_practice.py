"""
bitwise practice to implement bitwise functions for better algo runtime on bin2dec.py
"""
print(f'five: \t{bin(5)}')
print(f'six: \t{bin(6)}')

five = bin(5)
six = bin(6)
print(f'five: \t{five.lstrip("0b")}')
print(f'six: \t{six.lstrip("0b")}')
print(f'5 & 6: \t{5 & 6}')  