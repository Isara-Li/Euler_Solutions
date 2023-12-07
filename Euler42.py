## Question 42
## Isara Liyanage

def create_triagle_number_list(n):
    triangle_list=list()
    for i in range(1,n+1):
        t_num=(1/2)*i*(i+1)
        triangle_list.append(t_num)
    return triangle_list
letter_dic={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13,
              'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
file_h=open("Question42.txt")
for line in file_h:
    line=line.rstrip()
    temp_word_list=line.split(",")
word_list=list()
for word in temp_word_list:
    new_str=word[1:len(word)-1]
    word_list.append(new_str)

triangle_list=create_triagle_number_list(130)
total_for_word=word_count=0
for word in word_list:
    for letter in word:
        letter=letter.lower()
        total_for_word+=letter_dic.get(letter)
    if total_for_word in triangle_list:
        word_count+=1
    total_for_word=0
print(word_count)
