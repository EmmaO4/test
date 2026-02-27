char1 = "a"
char2 = "b"
char3 = "c"

print(char1, ord(char2), ord(char3))

def is_consecutive(a, b):
    return abs(ord(a) - ord(b)) == 1

print(is_consecutive(char1, char2))
print(is_consecutive(char1, char3))