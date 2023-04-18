# make a list
power_rangers = ["Red", "Blue", "Yellow"]

#get first power ranger
first = power_rangers[0]

# print list
print(first)

Adding more to list

# make a list
power_rangers = ["Red", "Blue", "Yellow"]

# add power ranger
power_rangers.append("Pink")
power_rangers.append("Black")
power_rangers.append("Green")

# Show power rangers
print(power_rangers)

Reverse list : Starting with the last

# make a list
power_rangers = ["Red", "Blue", "Yellow"]

# add power ranger
power_rangers.append("Pink")
power_rangers.append("Black")
power_rangers.append("Green")

# Reverse list
power_rangers.reverse()

# Show power rangers
print(power_rangers)

Sorting the list: Alphabetically

# make a list
power_rangers = ["Red", "Blue", "Yellow"]

# add power ranger
power_rangers.append("Pink")
power_rangers.append("Black")
power_rangers.append("Green")

# Reverse list
power_rangers.reverse()

# Sort List
power_rangers.sort()

# Show power rangers
print(power_rangers)

If you want to delete the first "value" from up - Pop will do that

print(power_rangers)

power_rangers.pop()

If you want to delete a specific value - Pop & number placement of that respective value

print(power_rangers)

power_rangers.pop(1)

# Show power rangers
print(power_rangers)

If you want to delete a specific value - Pop & number placement of that respective value
Remove : Will also delete the specific value mentioned = So two at the same time
print(power_rangers)

power_rangers.pop(1)
power_rangers.remove("Red")

# Show power rangers
print(power_rangers)

If you want to know the size/ length of the list

# to show the size / length of the list

number_of_rangers = len(power_rangers)

# Show power rangers
print(number_of_rangers)
