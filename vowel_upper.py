text = input("")
new = ""

for char in text:
    asci = ord(char)
    if 97 <= asci <= 122: 
        if char in 'aeiou':
            new += chr(asci - 32) 
        else:
            new += char
    else:
        new += char 

print(new)
