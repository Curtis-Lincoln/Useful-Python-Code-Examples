#Grade Boundaries
def marks(grade_in):
    grades = [["A*", "90"], ["A", "83"], ["B", "72"], ["C", "60"], ["D", "49"], ["E", "30"]]

    for count in range(len(grades)):
        if grades[count][0] == grade_in:
            return grades[count][1]

grade = input("What grade do you wish to achieve: ")
mark_req = marks(grade)
print("For grade", grade, "you need to gain", mark_req)
