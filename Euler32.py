## Question 32
## Isara Liyanage

def countNumbers(a,b,product):
    return len(str(a))+len(str(b))+len(str(product))

def pandigital_Test(a,b,product):
    l=set()
    temp_var=str(a)+str(b)+str(product)
    for element in temp_var:
        l.add(element)
    if len(l)==9 and "0" not in l:
        return True
    return False
a=2;b=1;l=set()
while True:
    while True:
        product=a*b
        count=countNumbers(a,b,product)
        if count==9:
            if pandigital_Test(a,b,product):
                l.add(product)
                print(a,b,product)
        elif count>9:
            break
        b+=1
    if b==4:  ## We knew we have to stop when b=4, because we ran the program once and
              ## observed that the first pair is (4*1738=6952). Then the last pair should
              ## be (1738*4). So to aviod this bad practice, we must store the first value
              ## for (b) and later use it to break the outer loop.
        break
    b=0
    a+=1
print("The sum is ",sum(l))
