## Euler 36
## Isara Liyanage

def is_Palindromic(n):
    n=str(n)
    if n==n[::-1]:
        return True
    return False
def is_Palindromic_bin(n):
    n=str(n);n=n[2:]
    if n==n[::-1]:
        return True
    return False
total=0    
for i in range(1,1000000):
    if is_Palindromic(i):
        if is_Palindromic_bin(bin(i)):
            total+=i
print(total)
       
