sum1=0
sum2 = 0
squares = []

#find squares upto 100

def square():
    global squares,sum1
    for i in range (1,101):
        sq=i**2
        squares.append(sq)
    

    for i in squares:
        sum1=sum1+i
    
square()
#find addition of all numbers upto 100
def results():
    global sum2
    for i in range(1,101):
        sum2=sum2+i
    
results()
#find square of addition of all numers upto 100
sumnum=sum2**2
#substract square of sum of all numbers-sum of squares of all the numbers
result=sumnum-sum1
print(result)
