# code for generating Fibonacci sequence and adding its even numbers
num = int(input("enter a number : ")) #user input 
n1, n2 = 0, 1
list1=[]
list2=[]
evensum=0
count=0
if (num <= 0):
    print("enter a positive number")
elif(num == 1):
    print("Fibonacci of given numer is : 1")
else:
    print("The sequence is :")
    while(count<num):
        sum=n1+n2
        n1=n2  #updating values of n1 and n2
        n2=sum
        count += 1
        list1.append(n1) #collection of fibonacci sequence
    print("list of fibonacci sequence : ",list1)        
    for i in list1:
        if (i%2==0):
            list2.append(i)     #collection of even numbers of sequence
            evensum=evensum+i   #sum of even elements os list 1
    print("list of even numbers of fibonacci sequence : ",list2)
    print("Sum of Even numbers of fibonacci sequence : ",evensum)







