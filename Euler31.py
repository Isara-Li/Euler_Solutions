## Question 31
## Isara Liyanage


"""
Might not be a very effective method. But it gets the job done.
"""
count=0
for p200 in range(0,2):
    for p100 in range(0,3):
        for p50 in range(0,5):
            for p20 in range(0,11):
                for p10 in range(0,21):
                    for p5 in range(0,41):
                        for p2 in range(0,101):
                            for p1 in range(0,201):
                                total= (1*p1)+(2*p2)+(5*p5)+(10*p10)+(20*p20)+(50*p50)+(100*p100)+(200*p200)
                                if total>200:
                                    break
                                if total==200:
                                    count+=1
print(count)
