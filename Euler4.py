##Question 4
##Isara Liyanage

"""
This code is designed in a way that user can find the largest Palindromic number
get by multiplying two numbers with any number of digits.

When calling the palindromicNum(power) by user, for power he/she must enter the
number of digits in one number

Ex : Finding the largest Fib number made from product of 2 digit numbers user
     must enter

     palindromicNum(2)

Output will be the largest fib number
"""

def test(product,power):
    length=power*2
    if len(str(product))==length:
        if str(product)[0:int(length/2)]== str(product)[-1:-1-int(length/2):-1]:
            return True
    return False
    
    

def palindromicNum(power):
    maxNum=0
    begin = 10**(power-1);end=10**(power)
    for i in range(begin,end,1):
        for j in range(begin,end,1):
            product=i*j
            if test(product,power):
                if product>maxNum:
                    maxNum=product
    return maxNum

print(palindromicNum(3))            
        
