import math

def find_all_divisors_of_a_number(n):
    result = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            result.append(i)
            if i*i != n:
                result.append(n//i)
    return result        

print(find_all_divisors_of_a_number(12))
