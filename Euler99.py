import math


## Using logarithms

file_h=open("Question99.txt")
maximum=0;line_num=1
for line in file_h:
    a,b=map(int,line.split(","))
    ex = b*math.log(a,10)
    if ex > maximum:
        maximum=ex
        out_line=line_num
    line_num+=1
print(out_line)
