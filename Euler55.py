def isPalindrome(num):
    return True if str(num)==str(num)[::-1] else False

count=0
for n in range(1,10000+1):
    check=n
    for _ in range(50):
        if isPalindrome(check+int(str(check)[::-1])): break
        else: check=check+int(str(check)[::-1])
    else:
        count+=1

print(count)    
