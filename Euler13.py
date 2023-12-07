##Question 13
##Isara Liyanage

total=0
with open('Q13.txt') as f:  
    while True:
        line = f.readline()
        if not line: 
            break
        a=int(line)
        total+=a
print(total)
        
