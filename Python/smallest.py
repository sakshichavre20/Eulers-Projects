import math
#find all prime numbers below 20
list1=[]
list2=[]
list3=[]
def prime ():
    global list1
    for i in range(1,21):
        if i > 1:
            for j in range (2,i):
                if(i%j == 0):
                    break
            else:
                list1.append(i)

prime()

#find all powers of 2 and 3 below 20
for i in range (2,20):
    p2=i**2
    if(p2<20):
        list2.append(p2)


list1=list1+list2
  

# calclate which terms to remove
for i in list2:
    s=int(math.sqrt(i))
    list3.append(s)

# from list 1 if there are common lcm of any of elemets remove it
for i in range(len(list3)):
    list1.remove(list3[i])

#multiply all the prime numbers and powers



def answer(list1):
    result=1
    for x in list1:
        result = result*x
    return result

print(answer(list1))
