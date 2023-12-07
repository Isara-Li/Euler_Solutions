## Question 43
## Isara Liyanage

from itertools import permutations   ## Permutations of given numbers.


solution=0  ## Specific code.
perm = permutations(range(0,10)) ## per has integers.
                                 ## if perm=permutations('012346789') was used, then perm is in string format.

pan_list=list()
for num in perm:
    if int(str(num[1])+str(num[2])+str(num[3]))%2==0:
        if int(str(num[2])+str(num[3])+str(num[4]))%3==0:
            if int(str(num[3])+str(num[4])+str(num[5]))%5==0:
                if int(str(num[4])+str(num[5])+str(num[6]))%7==0:
                    if int(str(num[5])+str(num[6])+str(num[7]))%11==0:
                        if int(str(num[6])+str(num[7])+str(num[8]))%13==0:
                            if int(str(num[7])+str(num[8])+str(num[9]))%17==0:
                                pan_list.append(num)

num_str="";total=0
for each_tuple in pan_list:
    for each_num in each_tuple:
        num_str+=str(each_num)
    total+=int(num_str)
    num_str=""
print(total)

"""
Method two using join function.
"""

from itertools import permutations
perm = permutations("0123456789")
for i in perm:
    if(int(''.join(i[7:10])) % 17 == 0 and
            int(''.join(i[6:9])) % 13 == 0 and   ## Joining string elements of a tuple using ''.
            int(''.join(i[5:8])) % 11 == 0 and
            int(''.join(i[4:7])) % 7 == 0 and
            int(''.join(i[3:6])) % 5 == 0 and
            int(''.join(i[2:5])) % 3 == 0 and
            int(''.join(i[1:4])) % 2 == 0):
            solution += int(''.join(i))  ## Joining the whole tuple into a number.
print (solution)
