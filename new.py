def _not_divisible(n):
    return lambda x: x % n > 0
    
print(list(filter(_not_divisible(3),[3,6,9,20])))
    
