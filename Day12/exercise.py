import math
    
def is_prime(num):
    # Numbers less than 2 are not prime numbers
    if num <= 1:
        return False
    # 2 is a prime number
    if num == 2:
        return True
    # Even numbers are not prime numbers
    if num % 2 == 0:
        return False

    # Instead of checking every number up to num, we only check up to sqrt(num). 
    # If num is divisible by some number p, then num = p * q. 
    # It's impossible for both p and q to be greater than sqrt(num) 
    # therefore we don't need to check numbers greater then sqrt(num)    
    max_number = int(math.sqrt(num)) + 1
    for i in range(3, max_number, 2):
        if num % i == 0:
            return False
            

    return True
