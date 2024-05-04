def sortingCeremony():
    
    GryffindorPoints = 0
    SlytherinPoints = 0
    RavenclawPoints = 0
    HufflePuffPoints = 0

    # Question 1
    print("Q1) Do you like Dawn or Dusk?")
    print("1) Dawn")
    print("2) Dusk")

    answer = int (input ("Your answer(1/2): "))

    if answer == 1:
        GryffindorPoints += 2
        RavenclawPoints += 2
    elif answer == 2:
        SlytherinPoints += 2
        HufflePuffPoints += 2
    else:
        print("Wrong Input")
        return
    

    # Question 2
    print("Q2) Do you like Forest or River?")
    print("1) Forest")
    print("2) River")

    answer = int (input ("Your answer(1/2): "))

    if answer == 1:
        GryffindorPoints += 2
        RavenclawPoints += 2
    elif answer == 2:
        SlytherinPoints += 2
        HufflePuffPoints += 2
    else:
        print("Wrong Input")
        return
    
    # Question 3
    print("Q3) Do you like Moon or Stars?")
    print("1) Moon")
    print("2) Stars")

    answer = int (input ("Your answer(1/2): "))

    if answer == 1:
        SlytherinPoints += 2
        RavenclawPoints += 2
    elif answer == 2:
        HufflePuffPoints += 2
        GryffindorPoints += 2
    else:
        print("Wrong Input")
        return

    # Question 4
    print("Q4) Which of the following would you most hate people to call you?")
    print("1) Ordinary")
    print("2) Ignorant")
    print("3) Cowardly")
    print("4) Selfish")

    answer = int (input ("Your answer(1/2/3/4): "))

    if answer == 1:
        SlytherinPoints += 2
    elif answer == 2:
        RavenclawPoints += 2
    elif answer == 3:
        GryffindorPoints + 2
    elif answer == 4:
        HufflePuffPoints += 2
    else:
        print("Wrong Input")
        return

