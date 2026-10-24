#Average for Each Student in a 2D List
cs_scores = [["Karman", "45", "60", "72"], ["Daniel", "55", "65", "70"],
             ["Giacomo", "71", "78", "78"], ["Jessica", "68", "79", "80"],
             ["Edie", "98", "85", "91"]]

def mean_student(scores_in):
    total = 0

    for exam in range(1,4):
        #iterate through each exam
        for student in range(len(cs_scores)):
            #update the total by iterating through each student
            total = total + int(cs_scores[student][exam])

            #Calculate and output the mean
            mean = total / len(cs_scores)
            print("Mean average for exam num", exam, "=", mean)

            #Reset the total before starting on the next exam
            total = 0

mean_student(cs_scores)
