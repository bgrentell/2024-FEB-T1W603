# Non-primitive data types - hold/store multiple pieces of data

# List - Array - collection of data - indexed - mutable (changed)
numbers = [ 13, 2, 5, 98, 56 ]

print(numbers)
print(numbers[2])

numbers[2] = 10
print(numbers)

numbers.append(42)
print(numbers)

numbers.insert(0, 16)
print(numbers)

numbers.pop()
print(numbers)

numbers.remove(98)
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(len(numbers))

# index, count
print("\n\n\n\n\n")
# Tuple - collection of data - indexed - immutable (cannot be changed)

names = ( "John", "Jane", "Mike", "Jane", "Jane" )

print(names)
print(names[1])

# names[2] = "Steve" # - Does not work
# names.append("Steve") # - Does not work

print(len(names))
print(names.count("Jane"))
print(names.count("Mike"))