# def re(a,i):
#     mask=1<<i
#     mask=~mask
#     return a&mask
# print(re(8,3))


def re(a,i):
    mask=1<<i
    return int(mask&a>0)
print(re(8,1))






# def re(a,i):
#     mask=1<<i
#     return a|mask
# print(re(8,3))