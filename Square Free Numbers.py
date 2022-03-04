import math


def squarefree(number):
    if number % 2 == 0:
        number = number/2
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)+1)):
        if(number % i == 0):
            number-number/i
        if (number % i == 0):
            return False
    return True

   


num = int(input())
outofsquare = []
fact = []
for i in range(1, num+1):
    if num % i == 0:
        fact.append(i)
for i in fact[1:]:
    if squarefree(i):
        outofsquare.append(i)
print(len(outofsquare))