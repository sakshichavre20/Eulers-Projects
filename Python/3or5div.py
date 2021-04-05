print("program find sum of numbers divisible by 3 or 5 from the given input range by user")
sum=0
num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number "))
list1=[]
for i in range(num1,num2):
    if (i%3==0 or i%5==0):
        sum=sum+i
        list1.append(i)
print("sum of numbers divisible by 3 or 5 : ",sum) 
print("number of elements divisible by 3 or 5 : ",len(list1))   
print(list1)    
