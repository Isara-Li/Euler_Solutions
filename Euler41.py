## Question 41
## Isara Liyanage


"""
if the sum of the numbers are divisile by 3; then they cannot be prime numbers. So only the sums of 4 digits numbers and 7 digit numbers are not divisible by 3
So only they have the tendancy to be prime numbers. Since 4<7 the largest prime number definetly belongs to the 7 category. So our checking range narrowa down to
   ## 1234567 to 7654321

1+2+3+4+5+6+7+8+9 = 45

1+2+3+4+5+6+7+8 = 36

1+2+3+4+5+6+7 = 28

1+2+3+4+5+6 = 21

1+2+3+4+5 = 15

1+2+3+4 = 10

1+2+3 = 6

1+2 = 3

From here it is pretty clear that all pandigital numbers except 4 and 7 digit ones are divisible by 3 and thus can’t be primes. 
"""
##def is_Prime(n):
##    if n==1:
##        return False
##    u=list()
##    for i in range(2, int(n**0.5) + 1):
##        if n % i == 0:
##            if i not in u and i!=n:
##                u.append(i)
##                break
##            if n//i not in u and i!=n:
##                u.append(n//i)
##                break
##    if len(u)==0:
##        return True
##    return False
"""
This method ckecks whether a given number is a Pandigital or not. 
"""
##def is_Pandigital(num):
##    num=str(num);pan=set();l_1=l_2=list()
##    for ele in num:
##        if int(ele)!=0:
##            pan.add(int(ele))
##    if len(pan)!=len(num):
##        return False
##    l_1=list(pan);l_1.sort();l_2=list(range(1,len(num)+1));l_2.sort()
##    #print(l_1,l_2)
##    if l_1==l_2:
##        return True
##    return False
"""
This method is kind of using brute force to solve the problem.
"""
##for i in range(10,97654321):
##    if is_Prime(i):
##        if is_Pandigital(i):
##            print(i)
##print("End")
def is_Prime(n):
    if n==1:
        return False
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
def test_by_parts(begin,end):
    prime_set=list()
    for i in range(begin,end-1,-1):
        if is_Prime(i): prime_set.append(i) ## Create a prime list first and then start checking whether they are pandigital from the last element, since we are looking for
                                            ## the largest prime number
    for j in range(len(prime_set)):
        temp_var=(prime_set[len(prime_set)-1-j])
        if is_Pandigital_modified(temp_var):
            print(temp_var);return True
            break
    return False
"""
Since we know we are looking for 7 digit numbers, the list we create(l_2) now has a specific value unlike in the previous scenario.
"""
def is_Pandigital_modified(num):
    num=str(num);pan=set();l_1=list();l_2=list(range(1,7+1));
    for ele in num:
        if int(ele)!=0:
            pan.add(int(ele))
    if len(pan)!=len(num):
        return False
    l_1=list(pan);l_1.sort()
    if l_1==l_2:
        return True
    return False
a=7654321
"""
First we check 7654321 to 7654321 - 10000 limit. IF we failed to find a number both prime and pandigital then we jump to the limit of 7654321 - 10000 to 7654321 - 20000
"""
while True:
    if test_by_parts(a,a-10000):
        print("End");break
    else:
        a=a-999
    
