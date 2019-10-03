# Think of at least five places in the world you’d like to visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
to_visit = [ 'italy', 'france', 'spain', 'turkey', 'germany']

# Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
print(f'Original order: {to_visit}')

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print(f'Alphabetical order: {sorted(to_visit)}')

# Show that your list is still in its original order by printing it.
print(f'Original order: {to_visit}')

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(f'Reverse alphabetical order: {sorted(to_visit, reverse=True)}')

# Show that your list is still in its original order by printing it again.
print(f'Original list: {to_visit}')

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
to_visit.reverse()
print(f'Reverse order: {to_visit}')

# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
to_visit.reverse()
print(f'Original List: {to_visit}')

# Use sort() to change your list so it’s stored in alphabetical order.
to_visit.sort()

# Print the list to show that its order has been changed.
print(f'Alphabetically sorted: {to_visit}')

# Use sort() to change your list so it’s stored in reverse alphabetical order.
to_visit.sort(reverse=True)

# Print the list to show that its order has changed.
print(f'Reverse Alphabetical: {to_visit}')
