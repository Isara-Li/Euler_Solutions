import math
def Digit_Wise_Fact(n):
    n=str(n);total=0
    for each_num in n:
        each_num=int(each_num)
        total+= math.factorial(each_num)
    return total
"""
Determining the upper bound is little bit tricky. So had to use this method.
10^d−1≤d⋅9!<10^d # d is the number of digits
 
(d−1)log(10)≤log(d)+log(9!)<dlog(10)

d≤7.33<d+1
​
So the maximum number of digits is (d+1)=8
                                    d=7

"""
for i in range(10,1000000):
    if i==Digit_Wise_Fact(i):
        print(i)
