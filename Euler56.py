highest_sum=0
for a in range(100):
    for b in range(100):
        highest_sum=max(sum(map(int,tuple(str(a**b)))),highest_sum)
print(highest_sum)
