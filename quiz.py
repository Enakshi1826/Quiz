questions = ("How many times India won the cricket World Cup?:",
             "Normal distribution is what kind of distribution?:",
             "Who has won the most Champions legue in Football history?:",
             "What is the most abundant gas in the Earth's atmosphere?:",
             "How many bones are in the human being?:")
options = (("A.2","B.4","C.6","D.None of these"),
           ("A.Leptokurtic","B.Mesokurtic","C.Symmetric","D.Doesn't exist"),
           ("A.Mbappe","B.Maldini","C.Messi","D.Ronaldo"),
           ("A.Nitrogen","B.Oxygen","C.Hydrogen","D.Carbon-DiOxide"),
           ("A.158","B.210","C.200","D.206"))
answers =("A","C","D","A","D")
guesses=[]
score=0
question_num=0

for question in questions:
    print("____________________")
    print(question)
    for option in options[question_num]:
        print (option)


    question_num += 1




