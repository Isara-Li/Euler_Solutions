## Euler 35
## Isara Liyanage

def rotate_the_digits(n):
    n=str(n);r_set=set();r_set.add(n)
    for i in range(len(n)-1):
        new_n=n[len(n)-1]+n[0:len(n)-1]
        r_set.add(new_n)
        n=new_n
    return r_set
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
count=s_count=0
for i in range(2,1000000):
    temp_set=rotate_the_digits(i)
    for element in temp_set:
        if is_Prime(int(element)):
            count+=1
        else:
            continue
    if count==len(temp_set):
        s_count+=1
    count=0
print(s_count)
