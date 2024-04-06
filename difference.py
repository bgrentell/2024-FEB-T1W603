num1 = 5

num2 = num1

num1 = 10

print(num1)
print(num2)

list1 = [ 1, 2, 3, 4 ]

list2 = list1 # assign list1 to list2 # copy by reference

list1.append(5)
list3 = list1.copy()
list1.append(1)
print(list1)
print(list2)
print(list3)
