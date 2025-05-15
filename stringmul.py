# n=input()
# k=""
# i=0
# while i<len(n):
#     count=int(n[i])
#     char=n[i+1]
#     k+=char*count
#     i+=2
# print(k)














n = input()
i = 0
result = ""
while i < len(n):
    count = ""
    while i < len(n) and n[i].isdigit():
        count += n[i]
        i += 1
    substring = ""
    while i < len(n) and not n[i].isdigit():
        substring += n[i]
        i += 1
    result += substring * int(count)
print(result)
