
def is_text(text):
    total = 0
    for char in text.upper():
        if 'A' <= char <= 'Z':
            pos = ord(char) - ord('A') + 1
            total += pos
    return total

code = input()
sum_pt = is_text(code)
print(sum_pt)
