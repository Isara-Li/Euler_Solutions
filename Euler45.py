## Question 45
## Isara Liyanage

## These quations were taken from wikipedia.org
def is_hex(n):
    a=(((8*n+1)**0.5)+1)/4
    b=int(a)
    if a/b == 1.0:
        return True
    return False

def is_pent(n):
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False
t=40756
while True:
    n=t*(t+1)*0.5
    if is_hex(int(n)) and is_pent(int(n)):
        print(n)
        break
    t+=1
    
