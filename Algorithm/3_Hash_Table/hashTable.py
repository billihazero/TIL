def two_sum(nums, target):
    dictionary= {} 
    for v in nums:
        dictionary[v] = True
    
    for v in nums:
        need_num = target - v
        if need_num in dictionary and need_num != v:
            return True
    return False;

print(two_sum({4,1,9,7,5,3,16}, 14))