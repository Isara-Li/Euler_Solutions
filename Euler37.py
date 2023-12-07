##Question 37
##Isara Liyanage


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
def R2L(num):
    condition=True
    for i in range(1,len(num)):
        if condition:
            temp_str=num[0:i]
            if is_Prime(int(temp_str)):
                pass
            else:
                condition=False
        else:
            break
    return condition
def L2R(num):
    condition=True
    for i in range(-2,-len(num)-1,-1):
        if condition:
            temp_str=num[-1:i:-1]
            temp_str=temp_str[::-1]
            if is_Prime(int(temp_str)):
                pass
            else:
                condition=False
        else:
            break
    return condition
j=10;final_list=list()
while True:
    if is_Prime(j):
        if R2L(str(j)):
            if L2R(str(j)):
                num=str(j)[::-1]                
                final_list.append(j)
    if len(final_list)==11:
        break
    j+=1

print(final_list)
print(sum(final_list))

