import re

fh=open("week2.1.txt")
for line in fh:
    print(line)
    l=re.findall('[0-9]+',line)

total=0
for num in l:
    num=int(num)
    total+=num
print(total)
