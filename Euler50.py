##def is_Prime(n):
##    if n==1: return False
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
##prime_list=list()
##for i in range(1,1000+1):
##    if is_Prime(i):prime_list.append(i)
##count=2
##while count<=len(prime_list):
##    for x in range(0,len(prime_list)-count+1):
##        s= sum(prime_list[x:x+count])
##        if is_Prime(s)and s<=1000:
##            c=count
##    count+=1
##print(c)

def is_Prime(n):
    if n==1: return False
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
for i in range(1,int(1000000*0.5)+1):
    if is_Prime(i):prime_list.append(i)
print(len(prime_list))
count=183
while count<=len(prime_list):
    for x in range(0,len(prime_list)-count+1):
        s= sum(prime_list[x:x+count])
        if s>=1000000:continue
        if is_Prime(s):
            c=count;break
    count+=1
print(c)
