def fizzbuzz(n):   
    for i in range (1, n+1):
        if(i % 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
        elif(i%5==0):
            print('buzz') 
        elif(i%3==0):
            print("fizz")
        else:
            print(i)
n=int(input('enter a number'))           
fizzbuzz(n)
