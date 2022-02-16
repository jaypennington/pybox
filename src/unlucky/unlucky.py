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
        