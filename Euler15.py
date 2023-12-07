##Question 15
##Isara Liyanage

"""
Question : Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

           How many such routes are there through a 20×20 grid?
For this kind of questions, we can use pascals triangle.
#1   #1  #1  #1  #1
 .---.---.---.---.
 |   |   |   |   |
 |  #2  #3  #4   |#5
#1.---.---.---.---.
 |   |   |   |   |
 |  #3  #6   #10 #15
#1.---.---.---.---.
 |   |   |   |   |
 |   |   |   |   |
#1.---.---.---.---.
     #4  #10 #20  #35

"""

def findSum(x):
    out_list=[];total=0
    for i in range(len(x)):
        if i==0:
            out_list.append(1)
            continue
        total=total+x[i-1]
        out_list.append(total+x[i])
    return out_list
def findPaths(n,m):
    n=n+1;m=m+1
    row_list=[];grid=[]
    for i in range(n):
        row_list.append(1)
    grid.append(row_list)
    for j in range(2,m+1):
        grid.append(findSum(grid[j-2]))
    return grid[m-1][n-1]



print(findPaths(20,20))
    
