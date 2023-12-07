"""Copied from Internet"""
import time

start = time.time()
cubes = []
i = 0
while True:
 cube = sorted(list(str(i**3)))
 cubes.append(cube)
 if cubes.count(cube) == 5:
  print ((cubes.index(cube))**3)
  break
 i += 1

end = time.time()
print (end - start)

"""My own code"""
import time

start = time.time()
i=0;dic={}
while True :
    num = "".join(sorted(list(str(i**3))))
    dic[num] = dic.get(num,0) + 1
    if dic[num] == 5 : break
    i+=1

i=0
while True:
    if "".join(sorted(list(str(i**3)))) == num: print(i**3);break
    i+=1


end = time.time()
print (end - start)
    
