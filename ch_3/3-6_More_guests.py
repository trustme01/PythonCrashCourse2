# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger dinner table.

guest_list = ['robert', 'erik', 'john']

print(f'Hello, {guest_list[0].title()} you are invited to come to dinner.')
print(f'Hello, {guest_list[1].title()} you are invited to come to dinner.')
print(f'Hello, {guest_list[2].title()} you are invited to come to dinner.')

name = guest_list[0].title()
print(f'\nSorry everyone. {name} cant make it to dinner.')

del(guest_list[0])
guest_list.insert(0, 'russell')


print(f'\nHello, {guest_list[0].title()} you are invited to come to dinner.')
print(f'Hello, {guest_list[1].title()} you are invited to come to dinner.')
print(f'Hello, {guest_list[2].title()} you are invited to come to dinner.')

print("\nEveryone, I found a bigger table!")

# Use insert() to add one new guest to the beginning of your list.
guest_list.insert(0, 'greg')
# Use insert() to add one new guest to the middle of your list.
guest_list.insert(2, 'carrie')
# Use append() to add one new guest to the end of your list.
guest_list.append('rosa')
# Print a new set of invitation messages, one for each person in your list.
print(f'\nHello, {guest_list[0].title()} you are invited to come to dinner.')
print(f'Hello, {guest_list[1].title()} you are invited to come to dinner.')
print(f'Hello, {guest_list[2].title()} you are invited to come to dinner.')
print(f'Hello, {guest_list[3].title()} you are invited to come to dinner.')
print(f'Hello, {guest_list[4].title()} you are invited to come to dinner.')
print(f'Hello, {guest_list[5].title()} you are invited to come to dinner.')

