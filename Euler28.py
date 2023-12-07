## Question 28
## Isara Liyanage


diagonal_list=[1,3,13]
square_count=5
while True:
    next_dif= (diagonal_list[len(diagonal_list)-1]- diagonal_list[len(diagonal_list)-2])+8
    next_ele= diagonal_list[len(diagonal_list)-1] + next_dif
    diagonal_list.append(next_ele)
    square_count+=2
    if square_count==1001:
        break
increment=2;square_list=list()
for item in diagonal_list[1:]:
    temp=item
    for i in range(3):
        temp=temp+increment
        square_list.append(temp)
    increment+=2
print(sum(diagonal_list)+sum(square_list))
