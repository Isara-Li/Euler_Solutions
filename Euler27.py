## Question 27
## Isara Liyanage


"""
This method takes co-efficients and returns the number of prime numbers produced. 
"""
def test_expression(a,b):
    n=0
    while True:
        expression=(n**2)+(a*n)+(b)
        if expression <0:
            break
        if not is_Prime(expression):
            break
        n+=1
    return n
"""
Checks whether a given number is a prime number or not. 
"""
def is_Prime(n):
    u=list()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i not in u and i!=n:
                u.append(i)
                break
            if n//i not in u and i!=n:
                u.append(n//i)
                break
    if len(u)==0:
        return True
    return False
prime_list=list()
for i in range(2,1001):
    if is_Prime(i):
        prime_list.append(i)
        prime_list.append(-i)
max_num=0;(x,y)=(0,0)
for b in prime_list:
    for a in range(-999,1000):
        n=test_expression(a,b)
        if n>max_num:
            max_num=n
            (x,y)=(a,b)
print(x,y,"Product =",x*y)
    
    
