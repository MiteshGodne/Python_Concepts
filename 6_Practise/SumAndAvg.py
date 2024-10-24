def sumCal(nums):
    sum = 0
    for i in range(len(nums)):
        sum = nums[i] + sum
    return sum
nums = eval(input())
print(nums)
print(len(nums))
print(sumCal(nums))