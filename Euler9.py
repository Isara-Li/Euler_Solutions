##Question 9
##Isara Liyanage

"""
This method takes a huge amount of time in order to do the calculation. The reason is, it's really hard to distinguish triplets without missing any.

So instead of this code, it's much easy to use a code with a genaral term to obtain the specific triplets.

def ifTriplet(a,b,c):
    if a**2+b**2==c**2:
        return True
    return False
control=control2=False
a,b,c=3,4,5
while a<=1000:
    while b<=1000-a:
        while c<=1000-b-a and a**2+b**2>=c**2:
            print(a,b,c)
            if ifTriplet(a,b,c):
                
                if a+b+c==1000:
                    print(a,b,c)
                    control=True
                    break
                else:
                    control2=True
                    break
            else:
                c+=1
        b+=1;c=b+1
        if control:
            break
    a+=1;b=a+1;c=b+1
    if control:
        break


"""

"""
This code uses a genaral term to find triplets. a=m**2-n**2; b=2*m*n; c=m**2+n**2
m and n could be any integer but they should satisfy m>n
"""
m=2;n=1;control=False
while True:
    while m>n:
        a=m**2-n**2;b=2*m*n;c=m**2+n**2
        if ifTriplet(a,b,c) and a+b+c==1000 :
                print(a,b,c,a*b*c)
                control=True
                break
        n+=1
    m+=1;n=1
    if control:
        break
                
