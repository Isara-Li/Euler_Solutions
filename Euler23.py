## Question 23
## Isara Liyanage


def factors(n):
    u=list()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i not in u:
                u.append(i)
            if n//i not in u:
                u.append(n//i)
    if n in u:
        u.remove(n)
    return u

def find_Abun_list():
    temp_list=Abun_list=list();total=0
    for i in range(12,28123-12+1):
        temp_list=factors(i)
        for ele in temp_list:
            total+=ele
        if total > i:
            Abun_list.append(i)
        total=0
    return Abun_list

def sum_Of_Abun_num(Abun_list):
    sum_list=set()                     ## set doesn't allow to duplicate elements in it
    for i in range(0,len(Abun_list)):
        if Abun_list[i]<=14107:
            for j in range(i,len(Abun_list)):
                sum_Abun= Abun_list[i]+Abun_list[j]
                if sum_Abun>28213:
                    break
                sum_list.add(sum_Abun)
        else:
            break
    return sum_list
    
real_abundant=sum_Of_Abun_num(find_Abun_list())
m = set(i for i in range(1,28214)) ## Create a set of integers from i to 28214

total_sum = m - real_abundant  ## Remove the elements in real_abundant from m
print(sum(total_sum))  
 
