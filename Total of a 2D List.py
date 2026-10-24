#Total of a 2D List
cs_scores = [["Karman", "45", "60", "72"],
             ["Daniel", "55", "65", "70"],
             ["Giacomo", "71", "78", "78"],
             ["Jessica", "68", "79", "80"],
             ["Edie", "98", "85", "91"]]

total = 0
for student in range(len(cs_scores)):
    for exam in range(1,4):
        total = total + int(cs_scores[student][exam])
    print("Total for", cs_scores[student][0], "=", total)
    total = 0
