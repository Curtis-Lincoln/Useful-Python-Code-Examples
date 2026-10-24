#Highest Number in a List
numbers = [9, 8, 72, 22, 21, 81, 2, 1, 11, 76, 32, 54]

highest = numbers[0]

for count in range(len(numbers)):
    if highest < numbers[count]:
        highest = numbers[count]

print("The highest number is", highest)

#An alternative approach using a function:

numbers = [9, 8, 72, 22, 21, 81, 2, 1, 11, 76, 32, 54]

def highest_num(numbers_in):
    highest = numbers[0]

    for count in range(len(numbers)):
        if highest < numbers[count]:
            highest = numbers[count]

    return highest

highest_out = highest_num(numbers)
print("The highest number is", highest_out)
