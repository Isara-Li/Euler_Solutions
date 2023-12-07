##Question 2
##Isara Liyanage

## Code to print out the first 10 fib numbers

##fib = [1,2]; i=1
##while True:
##    fib.append(fib[len(fib)-2]+fib[len(fib)-1])
##    i+=1
##    if i ==9:  ## To get the first 10 numbers i must be 9 because increment is done before the condition....
##        break
##print(fib)
    

fib = [1,2];total=0
while True:
    temp=fib[len(fib)-2]+fib[len(fib)-1]
    fib.append(temp)
    if temp>=4000000:
        break
for num in fib:
    if num%2==0:
        total+=num
print(total)
    
