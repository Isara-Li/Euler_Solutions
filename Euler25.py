## Question 25
## Isara Liyanage

"""
Returns the number of digits of a given parameter
"""
def count_digits(i):
    i=str(i)
    return len(i)


fib = [1,2];i=0
while True:
    i=fib[len(fib)-2]+fib[len(fib)-1]
    fib.append(i)
    if count_digits(i)>=1000:
        break
print(fib.index(i)+1+1)
