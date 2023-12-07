def return_square(num):
    return sum(map(lambda a:int(a)**2,str(num)))


count=0
for j in range(2,1000000):
    i=j
    while True:
        if i==89: count+=1;break
        if i==1:break
        i=return_square(i)

print(count)
