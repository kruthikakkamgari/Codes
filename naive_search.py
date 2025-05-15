def search(pattern,text):
    m=len(pattern)
    n=len(text)
    for i in range(n-m+1):
        j=0
        while j<m and text[i+j]==pattern[j]:
            j+=1
            if j==m:
                print(i)
text="AABAACCCDAABAABA"
pattern="AABA"
search(pattern,text)