## Question 29
## Isara Liyanage


term=set()
for a in range(2,101):
    for b in range(2,101):
        ele=a**b
        term.add(ele)
print(len(term))
