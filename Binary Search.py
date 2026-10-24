#Binary Search
def Binary_Search(Find_This):
    List = list(range(0,100))
    Start = 0
    End = len(List) - 1
    Mid = Start + (End-Start)//2

    while Start <= End:
        Mid = Start + (End-Start)//2

        if List[Mid] == Find_This:
            return Mid
        elif List[Mid] < Find_This:
            Start = Mid + 1
        else:
            End = Mid - 1

    return "Not Found"




            
        
            

