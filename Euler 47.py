def find_factors(num):
    l=[]
    while num != 1:
        for i in range(2,num+1):
            if is_prime(num):l.append(num);num=1;break
            if num%i==0:
                l.append(i)
                num=int(num/i)
                break
    return set(l)

def is_prime(num):
    if num==0 or num==1: return False
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
count=1
while True:
    if len(find_factors(count))==4:
        if len(find_factors(count+1))==4:
            if len(find_factors(count+2))==4:
                if len(find_factors(count+3))==4:print(count);break
    count+=1
                
        
    


        
    
