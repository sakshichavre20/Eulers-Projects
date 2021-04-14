
pow=[]
def power(p):
    global pow 
    for i in range(2,p):
        for j in range(2,p):
            pw=i**j
            if(pw<p):
                pow.append(pw)
                print(i, "**", j, "=", pow)
    return(pow)
(power(p))
print(pow)




            
