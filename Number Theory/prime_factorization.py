import math

def prime_factorization(n):
    result = []
    
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i 
                count += 1       
            result.append((i, count))
    
    if n > 1:
        result.append((n,1))
    
    return result

print(prime_factorization(32))
print(prime_factorization(45))
print(prime_factorization(75))