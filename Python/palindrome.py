def isPalindrome(num):
    return str(num)==str(num)[::-1]
def largest (min,max):
    z=0
    for i in range(max,min,-1):
        for j in range(max,min,-1):
            if isPalindrome(i*j):
                if i*j >z:
                    z=i*j
    return z
print(largest(100,999))



