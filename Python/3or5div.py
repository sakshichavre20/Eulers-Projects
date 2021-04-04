print("program find sum of numbers divisible by 3 or 5 upto 1000")
sum=0
list1=[]
for i in range(1000):
    if (i%3==0 or i%5==0):
        sum=sum+i
        list1.append(i)
print(sum) 
print("number of elements divisible by 3 or 5 upto 1000: ",len(list1))       
