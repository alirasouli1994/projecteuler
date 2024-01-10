
def palindrome(n):
    a = n
    c=''
    while a > 0 :
        
        b= int(a%10)
        a=(a-b)/10
        c+=str(b)
    if int(c)==n :
        return True
    return False
Max = 0
for i in range (100,1000):
    for j in range(100,1000):
        if palindrome(i*j):
            if i*j > Max :
                Max = i*j
print(Max)