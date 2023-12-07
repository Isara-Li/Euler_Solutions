##Question 12
##Isara Liyanage

def factors(n):
    u=[]
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i not in u:
                u.append(i)
            if n//i not in u:
                u.append(n//i)
    return u
i=0;total=0
while True:
    if len(factors(total))>500:
        print(total)
        break
    total=i+total
    i+=1
