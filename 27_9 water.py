def trap(height):
    if not height:
        return 0
    left,right=0,len(height)-1
    left_max=right_max=water=0
    while left<right:
        if height[left]<height[right]:
            water+=max(0,left_max-height[left])
            left_max=max(left_max,height[left])
            left+=1
        else:
            water+=max(0,right_max-height[right])
            right_max=max(right_max,height[right])
            right+=1
    return water
height=list(map(int,input().split()))
print(trap(height))

