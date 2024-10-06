def leet(nums):
    a=max(nums)
    for x in nums:
        if abs(x)<abs(a):
            a=x
        elif abs(x)==abs(a):
            a=max(x,a)
    return a
f=leet([-4,-2,1,4,8])
print(f)




