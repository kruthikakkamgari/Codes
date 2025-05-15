text = input("")
new = ""

for char in text:
    if 'a' <= char <= 'z':
        new += chr(ord(char) - 32)
    elif 'A' <= char <= 'Z':
        new += chr(ord(char) + 32) 
    else:
        new += char  
print(new)




