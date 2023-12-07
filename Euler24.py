least_num="123456789"
per_list=list();b=False
for j in range(1000):
    num=int(least_num)
    sort=sorted(least_num)
    for i in range (len(sort)-1):
        if sort[i]==sort[i+1]:
            num+=1
            least_num=str(num);b=True
            break
    if b:
        b=False
        continue
    per_list.append(least_num)
    num+=1
    least_num=str(num)
per_list.sort()
print(per_list)
least_num="0123456789"
##per_list=list()
b=False
for j in range(1000):
    num=int(least_num)
    sort=sorted(least_num)
    for i in range (len(sort)-1):
        if sort[i]==sort[i+1]:
            num+=1
            least_num=str(num);b=True
            break
    if b:
        b=False
        continue
    per_list.append(least_num)
    num+=1
    least_num=str(num)
per_list.sort()
print(per_list)
