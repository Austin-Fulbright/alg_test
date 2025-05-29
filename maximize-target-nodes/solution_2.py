def compute_gains(nums, k):
    gains = [0 for _ in range(len(nums))]
    for i in range(len(nums)):
        num = nums[i]
        numxor = num ^ k
        gain = numxor - num
        gains[i] = gain
    return gains 
    
