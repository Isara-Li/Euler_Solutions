def is_Prime(n):
    if n==1 or n<0:
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
def check_num(n):
    for i in range(0,int(n**0.5)+1):
        if is_Prime(n-(2*(i**2))) and (n-(2*(i**2)))>0:
            break
    else:
        print(n)
        return True
    return False
i=5
while True:
    if check_num(i):
        break
    i+=2
