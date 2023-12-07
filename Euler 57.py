from fractions import Fraction as frac

a_1= 1 + frac(1,2);count=0

for _ in range(1000-1):
    a_2 = 1+ frac(1,(1+a_1))
    if len(str(frac(a_2).numerator))>len(str(frac(a_2).denominator)): count+=1
    a_1=a_2

print(count)
