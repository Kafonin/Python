import numpy as np
weight_list=[]

myNum = 1

while myNum <=4:
    token = input('Enter weight %d:\n' % myNum)
    myNum +=1
    weight_list.append(float(token))
else:
    print('Weights:', [float(i) for i in weight_list])

print('\nAverage weight:', np.mean(weight_list))
maximum = max(weight_list)
print('Max weight: %.2f\n' % maximum)

a = int(input('Enter a list index (1 - 4):\n')) #added int() because inputting a number caused an error because the program said i input a string
a -= 1

pounds = weight_list[a]
kilograms = weight_list[a] / 2.2

print('Weight in pounds: %.2f' % pounds)
print('Weight in kilograms: %.2f' % kilograms)

print('\nSorted list:', sorted([float(i) for i in weight_list]))