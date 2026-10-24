#Average of a List
def mean_of_list(numbers_list_in):
    total = 0
    for count in range(len(numbers_list_in)):
        total = total + numbers_list_in[count]

    #Divide by the length of the list to find the mean
    average = total / len(numbers_list_in)
    return average

def main():
    numbers_list = [0, 7, 5, 3, 22, 23, 11, 34, 51, 32, 5, 3, 1]

    mean = mean_of_list(numbers_list)
    print("The mean average of", numbers_list, "=", mean)

if __name__ == '__main__':
    main()
