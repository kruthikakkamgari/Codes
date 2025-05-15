def merge_the_tools(string,k):
    for i in range(0,len(string),k):
        s=str[i:i+k]
        left="" 
        for j in (s):
            if j not in left:
                left+=j
        print(left)