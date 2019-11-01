num=int(input("please enter the number:"))
x = list(range(1,num+1))

divisorList = []

for number in x:
    if num % number == 0:
        divisorList.append(number)
print(divisorList)
