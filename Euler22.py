##Question 22
##Isara Liyanage


import string
file_handler=open("Question22.txt")
for line in file_handler:
    name_list=line.split(',')
name_list.sort()
place=1;alph_total=final_total=0
alphabet=list(string.ascii_uppercase)   # Gives a list of the english alphabet. "import" part is important
for each_name in name_list:
    temp_str=each_name[1:len(each_name)-1]
    for letter in temp_str:
        alph_total+=alphabet.index(letter)+1
    final_total+=alph_total*place
    alph_total=0
    place+=1
print(final_total)
        
