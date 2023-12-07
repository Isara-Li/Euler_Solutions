def isPrime(num):
    if num==0 or num==1: return False
    for n in range(2,int(num**0.5)+1):
        if num%n==0: return False
    return True

prime_list=list();count=1;exp=1000000;a=False
for i in range(exp):
    if isPrime(i): prime_list.append(i)

for _ in range(len(prime_list)-1,1,-1):
    if a: break
    for j in range(0,count+1):
        l= prime_list[j:j+len(prime_list)-count]
        if sum(l)>exp: break
        if isPrime(sum(l)): print(sum(l));a=True;break
    count+=1
    
