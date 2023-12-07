def Lexi_Permu(l):
    least_num=l
    per_list=list();b=False
    for j in range (10000000):
        num=int(least_num)
        sort=sorted(least_num)
        for i in range (len(sort)-1):
            if sort[i]==sort[i+1] or "0" in sort:
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
    print(len(per_list))

Lexi_Permu("123456789")
