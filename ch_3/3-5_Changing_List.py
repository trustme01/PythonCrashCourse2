# Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.
guest_list = ['robert', 'erik', 'john']

print(f'Hello, {guest_list[0].title()} you are invited to come to dinner.')
print(f'Hello, {guest_list[1].title()} you are invited to come to dinner.')
print(f'Hello, {guest_list[2].title()} you are invited to come to dinner.')

name = guest_list[0].title()
print(f'\nSorry everyone. {name} cant make it to dinner.')

# Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
del(guest_list[0])
guest_list.insert(0, 'russell')

# Print a second set of invitation messages, one for each person who is still
# in your list.
print(f'\nHello, {guest_list[0].title()} you are invited to come to dinner.')
print(f'Hello, {guest_list[1].title()} you are invited to come to dinner.')
print(f'Hello, {guest_list[2].title()} you are invited to come to dinner.')
