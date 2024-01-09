def is_prime(n):
    if n <=1 :
        return False
    a = int(n**0.5)+1
    for i in range(2,a):
        if n % i == 0 :
            return False
    return True 
a =600851475143
Max = 0
for i in range (1,int(a**0.5)+1):
    if a % i == 0 and is_prime(i):
        Max=i

print(f"Max = {Max}")