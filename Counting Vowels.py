#Counting Vowels
def vowel_counter(sentence):
    A = 0
    E = 0
    I = 0
    O = 0
    U = 0

    for count in range(len(sentence)):
        #The .upper() casts the current letter to an upper case
        #Without .upper(), we would write
        #if sentence[count] == "A" or sentence[count] == "a":

        if sentence[count].upper() == "A":
            A = A + 1
        elif sentence[count].upper() == "E":
            E = E + 1
        elif sentence[count].upper() == "I":
            I = I + 1
        elif sentence[count].upper() == "O":
            O = O + 1
        elif sentence[count].upper() == "U":
            U = U + 1

        #Using comma to concatenate in Python means we can cast
        #the integer value implicitly without using str()
    print("The number of A's:", A)
    print("The number of E's:", E)
    print("The number of I's:", I)
    print("The number of O's:", O)
    print("The number of U's:", U)

sentence = """Learning programming is similar to learning a musical
              musical instrument. Both involve practise and making lots
              of mistakes. Both also require perseverence to develop fluency.
              Keep going!"""

vowel_counter(sentence)
         
         
