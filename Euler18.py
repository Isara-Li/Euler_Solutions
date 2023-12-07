##Question 18
##Isara Liyanage


"""
This method doesn't satisfy the requirments of the question.
This methods goes from top to bottom of the triangle,adding the largest element in the row.
That is not what is expected by the question.
"""

def findLargest_Comp(row,index):
    if int(row[index])>int(row[index+1]):
        return int(row[index]),index
    else:
        return int(row[index+1]),(index+1)
triangle=open("Question18.txt")
total=0;row=list();index=0;row2=[]
for line in triangle:
    line=line.rstrip()
    if len(line)==2:
        total=total + int(line)
        continue
    row=line.split()
    row2.append(row)
for each_line in row2:
    if len(each_line)==1:
        continue
    if len(row)==2:
        index=row.index(str((max(int(row[0]),int(row[1])))))
    comp,index=findLargest_Comp(each_line,index)
    print(comp,index)
    total+=comp
    print(total)
print(total)

"""
This is the correct approach for the question 18
The method associated with this code is : https://www.mathblog.dk/project-euler-18/

Dynamic Programming – The Algorithm part in this website.
"""
def create_New_Row(row1,row2):
    new_row=list()
    for i in range(len(row2)-1):
        num_1=int(row2[i])+int(row1[i])
        num_2=int(row2[i+1])+int(row1[i])
        if num_1>num_2:
            new_row.append(str(num_1))
        else:
            new_row.append(str(num_2))
    return new_row

data_triangle=open("Question18.txt")
total=0;each_row=list();index=0
for line in data_triangle:
    line=line.rstrip()
    each_row.append(line.split())
while True:
    if len(each_row)==1:
        break
    temp_row=create_New_Row(each_row[len(each_row)-2],each_row[len(each_row)-1])
    each_row.remove(each_row[len(each_row)-1]);each_row.remove(each_row[len(each_row)-1])
    each_row.append(temp_row)
print(each_row)






















