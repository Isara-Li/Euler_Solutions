## Question 38
## Isara Liyanage

out_str="";count_set=set()
for i in range(1,10000): ## Since the begining of Pandigital multiples should be i,
    for j in range(1,10): ## the largest possible is 9876*1. So 10,000 is a good limit
        out_str+=str(i*j)
        if len(out_str)>=9:
            break
    if len(out_str)!=9:
        out_str=""
        continue
    for num in out_str:
        count_set.add(num)
    if len(count_set)==9 and "0" not in count_set:
        print(i,out_str)
    out_str="";count_set.clear()
print("End")
