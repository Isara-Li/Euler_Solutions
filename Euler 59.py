def is_english(msg,key):
    return True if 32 <= msg ^ key <=90 or  97 <= msg ^ key <=122 else False

file = open("Euler59.txt")
for line in file:
    l=line.split(",")

letter_1 = list(l[i] for i in range(0,123,3))

for i in range(97,123):
    for ele in letter_1:
        print(ele,i)
        if is_english(int(ele),i):
            if ele == letter_1[-1]: print(i)
            continue
        else : break
