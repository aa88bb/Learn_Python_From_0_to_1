import random

def compareNum(num1,num2):
    if(num1 > num2):
        return 1
    elif(num1 == num2):
        return 0
    else:
        return -1

num1 = random.randrange(1,9)
num2 = random.randrange(1,9)

print(num1,num2,compareNum(num1,num2))
print(str(num1)+str(num2))