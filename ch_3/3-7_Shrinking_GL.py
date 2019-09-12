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

# Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
print('\nSorry everyone. Only two people can come to dinner.')
# Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# message to that person letting them know you’re sorry you can’t invite them to dinner.
print(f'Sorry, {guest_list.pop().title()}, that you cannot come to the dinner')
print(f'Sorry, {guest_list.pop().title()}, that you cannot come to the dinner')
print(f'Sorry, {guest_list.pop().title()}, that you cannot come to the dinner')
print(f'Sorry, {guest_list.pop().title()}, that you cannot come to the dinner\n')

# Print a message to each of the two people still on your list, letting them
# know they’re still invited.
print(len(guest_list))
print(f'{guest_list[0].title()}, you can still come to dinner.')
print(f'{guest_list[-1].title()}, you can still come to dinner.')

# Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end of your program.
del guest_list[:]
print(guest_list)
