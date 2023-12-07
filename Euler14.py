##Question 14
##Isara Liyanage


def isEven(num):
    if num%2==0:
        return True
    return False
"""
This code uses a dictionary in order to store previous values and return counts easily
in case we find the same number in two different situations.
"""
out=0;max_num=0;count=0;dicto={}
for i in range(2,1000000):
    i=float(i)
    first_term=i
    count+=1
    while True:
        if isEven(first_term):
            next_term = first_term/2
        else:
            next_term = 3*first_term+1
        if next_term in dicto:
            count=count+dicto[next_term]
            break
        count+=1
        if next_term==1:
            break
        first_term=next_term
    if i not in dicto:
        dicto[i]=count
    if max_num<count:
        max_num=count
        out=i
    count=0
print(out)
