#Total of a List
#Example 1
number_list = [9, 8, 3, 5, 4, 1, 8, 4, 1]

total = 0

for count in range(len(number_list)):
    total = total + number_list[count]

print("The total sum of the list is ", total)

#Example 2
def total_list(number_list_in):
    total = 0

    for count in range(len(number_list)):
        total = total + number_list[count]

    return total #the toatl is returned

def main():
    #The main function contains all inputs and outputs
    number_list = [9, 8, 3, 5, 4, 1, 8, 4, 1]

    op = input("Do you wish to find the mean, lowest value, highest value or the total of the list?: ")

    #Call the relevant function based on the user input
    if op == "total":
        total_out = total_list(number_list)
        print("The total sum of the list is ", total_out)

#Call the main function
main()
        
