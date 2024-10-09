def remove(nums,val):
    k=0
    for i in range(len(nums)):
        if nums[i]!=val:
            # accepted elements moving forward
            nums[k]=nums[i]
            k+=1
    return k
f=remove([0,1,2,2,3,0,4],2)
print(f)