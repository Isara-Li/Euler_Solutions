##Question 21
##Isara Liyanage

"""
This method finds all the  factors of a number, except the entered number. 
"""
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
"""
This method finds the sum of a list
"""
def findSum(fac_list):
    total=0
    for num in fac_list:
        total+=num
    return total
amicable_dict=dict();t=0
for i in range(2,10000):
    amicable_dict[i]=findSum(factors(i))
for k,v in amicable_dict.items():
    for k_0,v_0 in amicable_dict.items():
        if v==k_0 and v_0==k:
            if v!=k and v_0!=k_0:
                t=t+(k+v)/2
                print(k,v,k_0,v_0)
print("The sum of all the pais are :#",t)
