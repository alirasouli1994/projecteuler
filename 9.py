# a**2 + b**2 = c**2
# a + b + c =1000

c = 0
for a in range(1001):
    for b in range(1001):
        if a < b < (1000 - a - b) and a**2 + b**2 == (1000 - a - b)**2 :
            print(a * b * (1000 - a - b))


