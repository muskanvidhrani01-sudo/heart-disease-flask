def question():
    Questions={"what is the full form of HTML":"c","What is the symbol used for defining Dictionary in python":"d","What is the symbol used for defining List in python":"b","What is the symbol used for defining tuple in python":"a"}
    Answers=[
        ["a. HTML","b. html","c. Hyper Text Markup Language","d. Hyper Test Management Language"],
        ["a. ()","b. []","c. <>","d. {}"],
        ["a. ()","b. []","c. <>","d. {}"],
        ["a. ()","b. []","c. <>","d. {}"]
    ]

    Count=1
    Score=0

    for Q,A in Questions.items():
        print(f"{Count}.{Q}")
        for i in Answers[Count-1]:
            print(f"{i}")
            

        choice=input("Enter Your Choice: ")
        if choice==A:
            Score=Score+1
        print("-------------------------------------------")
        Count=Count+1
    print(f"Your total Score is: {Score}")
    Reattempt=input("Do you want to reattempt? ")
    Reattempt=Reattempt.lower()
    if Reattempt=="yes":
        question()
    else:
        print("Bye!!!")

question()



