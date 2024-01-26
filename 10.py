def is_prime(n):
    if n <=1 :
        return False
    a = int(n**0.5)+1
    for i in range(2,a):
        if n % i == 0 :
            return False
    return True 
s = 0
for i in range(2000000):
    if is_prime(i):
        s += i

print(s)