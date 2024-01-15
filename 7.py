def is_prime(n):
    if n <= 1 :
        return False
    a = int(n**0.5)+1
    for i in range(2,a):
        if n%i == 0:
            return False
    return True

a = 0
n = 0
while a != 10001:
    if is_prime(n):
        a += 1
        
    n +=1


print(n-1)