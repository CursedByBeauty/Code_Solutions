

def moveZeroes(nums):
    l = 0
    
    for r in range(len(nums)):
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
    return nums

print(moveZeroes([1,3,0,8,0,5,4,0,6]))


# def moveZeroes(nums):
#     for num in nums:
#         if num == 0:
#             nums.remove(num)
#             nums.append(num)
#     return nums
# print(moveZeroes([1,3,0,8,0,5,4,0,6]))