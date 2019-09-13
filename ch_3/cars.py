# Sorting a list PERMANENTLY with the sort() method.
#  Alphabetically:
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#  Reverse alphabetically:
cars.sort(reverse=True)
print(cars)

# Sorting a list TEMPORARILY with the sort() method.
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
print('\nHere is the original list: ')
print(cars2)

print('\nHere is the sorted (alphabetical) list: ')
print(sorted(cars2))

print('\nHere is the original list again: ')
print(cars2)

#  Reverse alphabetically:
print('\nHere is the list reversed in alphabetical order: ')
print(sorted(cars2, reverse=True))

# Printing a List in Reverse Order
#  reverse() method
cars3 = ['bmw', 'audi', 'toyota', 'subaru']
print(cars3)

cars3.reverse()
print(cars3)
