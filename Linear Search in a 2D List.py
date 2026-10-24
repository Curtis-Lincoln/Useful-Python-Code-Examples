#Linear Search in a 2D List
cs_scores = [["Jo", "45", "60", "72"], ["Zi", "55", "65", "70"],
             ["Ellie", "71", "78", "78"], ["Jessica", "68", "79", "80"],
             ["Abdul", "65", "70", "71"]]

print("We will try to find the result for a given student's exam")

name = input("Enter a student's name: ")
exam_number = int(input("Enter the exam number: "))

found = False

for count in range(len(cs_scores)):
    if name == cs_scores[count][0]:
        found = True
        result = cs_scores[count][exam_number]
        print(name+"'s resultfor exam", exam_number, "was", result )

if found == False:
    print(name, "cannot be found")
        
