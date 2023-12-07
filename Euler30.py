## Question 30
## Isara Liyanage


"""
10^(d−1) ≤ d⋅9^(5) < 10^(d)
= (d−1)log(10)≤log(d)+5log(9)<dlog(10)
= d≤6.47<d+1
​
*(d) is the number of digits
* 9 is the maximum which one digit can have
ex :- (9^5)*d
if there are (d) digits then the least number with (d) digits is 10^(d-1)
likewise maximum number is 10^d


Here (d)=6 ; so upper bound is 10^6
"""
def sum_of_digits(num):
    total=0
    copy_num=str(num)
    for ele in copy_num:
        total=total+(int(ele)**5)
    if total==num:
        return True
    return False
tot=0
for i in range(2,1000000):
    if sum_of_digits(i):
        print(i)
        tot+=i
print("The total is : ",tot)
