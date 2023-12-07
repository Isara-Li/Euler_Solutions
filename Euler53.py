import math as m

count=0
for n in range(1,101):
    for r in range(1,n+1):
        if int(m.factorial(n)/(m.factorial(r)*m.factorial(n-r))) > 1000000:
            count+=1

print(count)
