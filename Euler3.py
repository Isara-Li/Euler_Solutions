##Question 3
##Isara Liyanage
##This file contains 4 approches for the same problem. First one is very slow.

"""
This method is super effective to find factors of small numbers. But when the number
becomes large, this code is very slow
"""
def Factors(num):
    factors=[]
    for i in range(1,num+1):
        if num%i==0:
            factors.append(i)
    return factors

factors=Factors(600851475143)
for j in factors:
    primeFac=Factors(j)
    if len(primeFac)==2:
        print(j)           
"""
This method is very effective for any number. The concept behind this code is to
narrowing the factor set.
Example : when finding factors of 100
             i) 1 ----> 10
             if 100%1==0 then both 1 and 100//1 (100) are added
             when i=2 ; both 2 and 50 are added
             wheni=3; nothing
             when i=4 ; 4 and 25 are added. So on
"""

def factors(n):
    u=[]
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i not in u:
                u.append(i)
            if n//i not in u:
                u.append(n//i)
    return u
    
fac=factors(600851475143)
for i in fac:
    PrimeFac=factors(i)
    if len(PrimeFac)==2:
        print(i)
"""
This method uses the long divition method. This method doesn't find all tthe factors but find all the prime factors
"""

a=2;n=600851475143;m=0
while a<=n:
    if n%a==0:
        if a>m:
            m=a
        n=n/a
    else:
        a+=1
print(m)


"""
This method uses a standard method in the theory tute to find the prime factors. Also special case of FOR loop is also used
"""
def factors(n):
    u=[]
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i not in u:
                for j in range(2,i): 
                    if i%j==0:
                        break
                else:                  # Else-Clause assoiated with the for loop
                    u.append(i)
            if n//i not in u:
                x=n//i
                for j in range(2,x):
                    if x%j==0:
                        break
                else:
                    u.append(x)
    return u

print(factors(600851475143))      
    
