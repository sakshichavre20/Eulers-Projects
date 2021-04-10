num=int(input("enter a number: "))
list1=[]
print("the values are")
for i in range (2,num):
    if(num%i==0):
        print(i) 
        list1.append(i)
print(list1)
print(max(list1))
      
