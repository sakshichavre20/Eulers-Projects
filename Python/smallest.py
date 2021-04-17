
def isDivsible1ton(number):
    for i in range(2,21):
        if number%i !=0:
            return False
    return True
number=20

while True:
    if isDivsible1ton(number):
        break
    number += 20

print(number)
