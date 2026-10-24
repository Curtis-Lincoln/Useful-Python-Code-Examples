#Lowest Number in a List
#Example 1
numbers_list = [9,8,7,5,6,2,1,12,14,0,13]

lowest = numbers_list[0]

for count in range(len(numbers_list)):
    if numbers_list[count] < lowest:
        lowest = numbers_list[count]

print("The lowest number in the list is ", lowest)

#Example 2
def find_lowest(numbers_list_in):
    lowest = numbers_list_in[0]

    for count in range(len(numbers_list_in)):
        if numbers_list_in[count] < lowest:
            lowest = numbers_list_in[count]

    return lowest

Numbers_list = [9,8,7,5,6,2,1,12,14,0,13]
Lowest_num = find_lowest(Numbers_list)
print("The lowest number in the list is ", Lowest_num)
