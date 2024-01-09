a = 1   # n-2
b = 1   # n-1
c = 0
sum = 0
n = 0
# print(a , b , end=" ")
while sum < 4000000 :
    c =a+b
    if c % 2 == 0:
        sum += c
    # print(c, end=" ")
    a=b
    b=c
    n+=1
print(sum)