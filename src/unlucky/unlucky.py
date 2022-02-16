# Write a function to return the sum of an array of integers.
# However, the number 13 is very unlucky, so do not include
# it in the sum. Addtionally, the number immediately after 13
# is unlucky, so don't include it, either.


def unlucky(nums):
    sum = 0
    is13 = False
    for num in nums:
        if num == 13:
            is13 = True
            continue
        if num != 13 and is13:
            is13 = False
            continue
        if num != 13:
            sum = sum + num
    
    return sum
        