##Question 5
##Isara Liyanage

"""
If the user wants to find the smallest number divisible by all the integers smaller
than n (including n) : user must enter divideByAll(n)

"""

def divideByAll(num):
    count=0;
    temp=num
    while True:
        for i in range(1,num+1):
            if temp%i==0:
                count+=1
        if count != num:
            temp+=num
            count=0
        else:
            return temp
        
print(divideByAll(20))    
