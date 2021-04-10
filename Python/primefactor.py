import math 
num = 600851475143
list1 =[]
list2=[]
# find all factors 
def factors(num):
    global list1
    
    for i in range(2, int(math.sqrt(num))):
        if (num % i == 0):           
            list1.append(i)
    print(list1)
    
    
factors(num)


# check for prime factors

def prime(num):
    global list2
    for i in list1:
        prime= True
        for j in range (2,i):
            if i%j==0:
                prime= False
        if prime == True :
            list2.append(i)
    print(list2)

prime(num)
            
# print largest prime factor
print(max(list2))   
      
