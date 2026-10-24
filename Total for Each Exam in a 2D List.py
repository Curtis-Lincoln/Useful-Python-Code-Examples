#Total for Each Exam in a 2D List
cs_scores = [["Karman", "45", "60", "72"],
             ["Daniel", "55", "65", "70"],
             ["Giacomo", "68", "79", "80"],
             ["Edie", "98", "85", "91"]]

total = 0

for exam in range(1,4):
    #iterate through each exam
    for student in range(len(cs_scores)):
        #update the total by iterating through each student
        total = total + int(cs_scores[student][exam])

    #Calculate the total
        print("Total for exam num", exam, "=", total)
    #Reset the total before starting on the next exam
        total = 0
