print("program find sum of numbers divisible by 3 or 5 from the given input range by user")
sum=0
i=int(input("Enter number from where you want sum of numbers divisible by 3 or 5"))
j=int(input("Enter number upto where you want sum of numbers divisible by 3 or 5"))
list1=[]
for i in range(j):
    if (i%3==0 or i%5==0):
        sum=sum+i
        list1.append(i)
print(sum) 
print("number of elements divisible by 3 or 5 upto 1000: ",len(list1))       
