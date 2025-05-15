def find_mid(num):
    count = 0
    for i in num:
        count += 1
    if count % 2 == 1:
        mid= count // 2
        return [num[mid]]
    else:
        mid1 = count // 2 - 1
        mid2 = count // 2
        return [num[mid1],num[mid2]]
# print(find_mid([10,30,20,40,20]))     
print(find_mid([10,20,30,40,50,60]))     
