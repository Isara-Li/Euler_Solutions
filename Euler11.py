##Question 11
##Isara Liyanage

"""
The input for the code is       08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
                                49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
                                81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
                                52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
                                22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
                                24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
                                32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
                                67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
                                24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
                                21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
                                78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
                                16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
                                86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
                                19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
                                04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
                                88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
                                04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
                                20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
                                20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
                                01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""

"""
This function takes four lists and calculate the product through the diagonals
      [a,b,c,d]
      [e,f,g,h]    calulate afkm and dgjx and return the largest value
      [i,j,k,l]
      [x,y,x,m]
      
"""
def Rows(list1,list2,list3,list4):
    p1=list1[0]*list2[1]*list3[2]*list4[3]
    p2=list4[0]*list3[1]*list2[2]*list1[3]
    if p1>p2:
        return p1
    return p2
"""
 Standard code to read data from a text document. f.readline() read line by line and gives the output as a string while f.readlines() gives the output as a list

with open('readme.txt') as f:  
    while True:
        line = f.readline()

The while loop is a must to read all the lines

data = line.split() splits the string from spaces and returns the elements as a list.
"""

maxiumRow=maxiumColumn=maxiumDiagonal=0
upDown=[];dia=[];dia2=[]
with open('Q11.txt') as f:  
    while True:
        line = f.readline()
        if not line: # In python (empty string)==(false) and (non empty string)==(true)
            break    # Cease the loop when empty line is found 
        data = line.split()  # i==0 : data =['08', '02', '22', '97', '38', '15', '00', '40', '00', '75', '04', '05', '07', '78', '52', '12', '50', '77', '91', '08']
        upDown.append(data)
        for i in range(0,len(data)-3):
            dia.append(int(data[i]));dia.append(int(data[i+1]));dia.append(int(data[i+2]));dia.append(int(data[i+3]))# i==0: dia=[08,02,22,97] : dia2=[[08,02,22,97]]
            dia2.append(dia);dia=[]  # We have to rest the dia                                                       # i==1: dia=[02,22,97,38] : dia2=[[08,02,22,97],[02,22,97,38]]
            product=int(data[i])*int(data[i+1])*int(data[i+2])*int(data[i+3])
            if product>maxiumRow:
                maxiumRow=product   # Finding the maximum product in one row
"""
j=upDown[k] ---> get the first row
j=j[kk] ---> get the first element of the first row
reverse.append(j)
"""
Column=[]
for kk in range(20):
    for k in range(20):
        j=upDown[k];j=j[kk];Column.append(j) # When the inner loop stops list column has 20 elements down the column of the main matrix
    for i in range(0,len(data)-3):
        product=int(Column[i])*int(Column[i+1])*int(Column[i+2])*int(Column[i+3]) #Finding the max of product down the column
        if product>maxiumColumn:
            maxiumColumn=product
    Column=[] # Reseting the list to avoid confusions
for a in range(17*17):
   diaMax=Rows(dia2[a],dia2[a+17],dia2[a+34],dia2[a+17+34]) # dia2[a+17]= first four elements of the second row
   if maxiumDiagonal<diaMax:
       maxiumDiagonal=diaMax
print(max(maxiumRow,maxiumColumn,maxiumDiagonal))
