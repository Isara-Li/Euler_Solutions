##Question 6
##Isara Liyanage

def difference(num):
    total1=total2=0
    for i in range(1,num+1):
        total1=total1+i**2
        total2=total2+i
    total2=total2**2
    return total2-total1
print(difference(100))
    
