##def create_pentagon_numbers(begin,end):
##    pen_list=list()
##    for i in range(begin,end+1):
##        pen_list.append(int(i*(3*i-1)*0.5))
##    return pen_list
##
##pen_list=create_pentagon_numbers(1,100000000)
##for a in range(len(pen_list)):
##    for b in range(a,len(pen_list)):
##        if pen_list[a]+pen_list[b] in pen_list:
##            if abs(pen_list[a]-pen_list[b]) in pen_list:
##                print(a,b)
##print("End")
##def is_pentagonal(n):
##    if (1+(24*n+1)**0.5) % 6 == 0:
##        return True
##    return False
##for a in range(len(pen_list)-1):
##    if is_pentagonal(pen_list[a]+pen_list[a+1]):
##        if is_pentagonal(abs(pen_list[a]-pen_list[a+1])):
##            print(abs(pen_list[a]-pen_list[a+1]))
##    
##print("End")
import time

# time at the start of program execution
start = time.time()


def is_pentagonal(n):
    """function to check if the number
    is pentagonal number or not"""
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False

# flag to check if the number is found or not
flag = True

# while loop iterator
i = 1

# while loop
while flag:
    for j in range(1, i):
        a = i*(3*i-1)/2
        b = j*(3*j-1)/2
        print ("(",a,b,")")
        if is_pentagonal(a+b) and is_pentagonal(a-b):
            
            flag = False
            break
    i += 1

# time at the end of program execution
end = time.time()

# printing the total time for execution
print (end - start)
