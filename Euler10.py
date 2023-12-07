##Question 10
##Isara Liyanage

"""
Takes some considerable amount of time to process
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
total=0
for i in range (2000000):
    if len(factors(i))==2:
        total+=i
print(total)
