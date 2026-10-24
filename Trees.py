#Tree

Countries = [
    [1,"moldova",2],
    [3,"leichenstein",10],
    [16,"north macedonia",5],
    [-1,"afghanistan",4],
    [-1,"fiji",6],
    [7,"uzbekistan",-1],
    [12,"israel",14],
    [-1,"palestine",8],
    [9,"ukaine",-1],
    [11,"taiwan",-1],
    [-1,"libya",-1],
    [-1,"syria",-1],
    [-1,"iran",13],
    [-1,"iraq",-1],
    [-1,"kuwait",15],
    [-1,"lebanon",-1],
    [-1,"north korea",-1],
    [-1,"England", -1]
    ]

LEFT = 0
DATA = 1
RIGHT = 2

def Pre_Order(Root = 0):
    print(Countries[Root][DATA])
    if Countries[Root][LEFT] != -1:
        Pre_Order(Countries[Root][LEFT])
    if Countries[Root][RIGHT] != -1:
        Pre_Order(Countries[Root][RIGHT])

def In_Order(Root = 0):
    if Countries[Root][LEFT] != -1:
        In_Order(Countries[Root][LEFT])
    print(Countries[Root][DATA])
    if Countries[Root][RIGHT] != -1:
        In_Order(Countries[Root][RIGHT])

def Post_Order(Root = 0):
    if Countries[Root][LEFT] != -1:
        Post_Order(Countries[Root][LEFT])
    if Countries[Root][RIGHT] != -1:
        Post_Order(Countries[Root][RIGHT])
    print(Countries[Root][DATA])

def Add_Item_Procedure(Item):
    if len(Countries) == 0:
        Countries.append([-1, Item, -1])
    else:
        Next_Item = 0
        while Next_Item != -1:
            Current_Item = Next_Item
            if Item < Countries[Current_Item][DATA]:
                Next_Item = Countries[Current_Item][LEFT]
                Direction = LEFT
            else:   
                Next_Item = Countries[Current_Item][RIGHT]
                Direction = RIGHT
        Countries[Current_Item][Direction] = len(Countries)
        Countries.append([-1, Item, -1])
        
def Add_Item_Recursive(Item, Root = 0):
    if len(Countries) == 0:
        Countries.append([-1, Item, -1])
    elif Item < Countries[Root][DATA]:
        if Countries[Root][LEFT] == -1:
            Countries[Root][LEFT] = len(Countries)
            Countries.append([-1, Item, -1])
        else:
            Add_Item_Recursive(Item, Countries[Root][LEFT])
    elif Item > Countries[Root][DATA]:
        if Countries[Root][RIGHT] == -1:
            Countries[Root][RIGHT] = len(Countries)
            Countries.append([-1, Item, -1])
        else:
            Add_Item_Recursive(Item, Countries[Root][RIGHT])
        
    
            
    
    
