#Bubble Sort

def Bubble_Sort():
    List = [0,1,4,7,2,6,9,2,3,5]

    for x in range(len(List)):
        for Index in range(0,len(List)-x-1):

            if List[Index] > List[Index + 1]:
                Temp = List[Index]
                List[Index] = List[Index+1]
                List[Index+1] = Temp

    return List



