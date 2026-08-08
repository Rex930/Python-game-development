quiz = (
    ("1. WHich function is used to display output in pyton"
    "A. input()"
    "B. display()"
    "C. print()"
    "D. Show()"
    "C"),

    (2. "Which symbol is used to write a comment in python?",
     "A. //",
     "B. #",
     "C. /*",
     "D. --",
     "B"),

    ("3. Which function is used to take input from the user?",
     "A. print()",
     "B. scan()",
     "C. input()",
     "D. read()",
     "C")

     ("4. WHich data type stores whole numbers?,"
     "A. float",
     "B. str",
     "C. int",
     "D. bool",
     "C")

     ("5. WHich operator is used for multiplication?",
     "A. +",
     "B *",
     "C. /",
     "D. -",
     "B"),

     ("6. Which keyword is used to create a function?",
      "A. function",
      "B. define",
      "C. fun",
      "D. def",
      "D"),

    ("7. Which loop is used to repeat a block of code a fixed number of times?",
     "A. if",
     "B. while",
     "C. for",
     "D. else",
     "C"),

     ("8. Which braclets are used to create a tuple?",
      "A. []",
      "B. {}",
      "C. ()",
      "D. <>",
      "C"),

      ("9. Which of the following is a Boolean value?",
       "A. Hello",
       "B. 100",
       "C. True",
       "D. 3.14",
       "C"),

       ("10. Which keyword is used to make decisions in python?",
        "A. if",
        "B. repeat",
        "C. loop",
        "D. switch",
        "A")
)

score = 0
print ("===== PYTHONBASICS QUIZ=====")

for question in quiz:
    print("\n" + question[0])
    print(question[1])
    print(question[2])
    print(question[3])
    print(question[4])
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == question[5]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct Answer:", question[5])

print("\n========= QUIZ OVER =========")
print("Your Score:", score, "/" , len(quiz))

percentage = (score / len(quiz)) * 100
print("Percentage:", percentage, "%")

if percentage == 100:
    print("Excellent! You got a perfect score!")
    elif

print(f"\nYour final score is: {score}/{len(quiz)}")