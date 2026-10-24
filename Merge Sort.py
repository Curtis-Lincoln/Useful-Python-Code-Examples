import random
def MergeSort(Sort_List):
    if len(Sort_List) > 1:
        Mid = len(Sort_List) // 2
        Left = Sort_List[:Mid]
        Right = Sort_List[Mid:]

        MergeSort(Left)
        MergeSort(Right)

        Left_Pointer = 0
        Right_Pointer = 0
        Main_Pointer = 0
        
        while Left_Pointer < len(Left) and Right_Pointer < len(Right):
            if Left[Left_Pointer] <= Right[Right_Pointer]:
              Sort_List[Main_Pointer] = Left[Left_Pointer]
              Left_Pointer += 1
            else:
                Sort_List[Main_Pointer] = Right[Right_Pointer]
                Right_Pointer += 1
            Main_Pointer += 1

        while Left_Pointer < len(Left):
            Sort_List[Main_Pointer] = Left[Left_Pointer]
            Left_Pointer += 1
            Main_Pointer += 1

        while Right_Pointer < len(Right):
            Sort_List[Main_Pointer]= Right[Right_Pointer]
            Right_Pointer += 1
            Main_Pointer += 1
        return Sort_List[0], Sort_List[-1], Sort_List

List = []
for _ in range(100):
    List.append(random.randint(1,1000000))
print(MergeSort(List))
