from playsound import playsound

def sortingHat():

    playsound("HedwigsTheme.wav")
    
    GryffindorPoints = 0
    SlytherinPoints = 0
    RavenclawPoints = 0
    HufflePuffPoints = 0

    # Introduction

    print("\nWelcome to the Sorting Ceremony where we will determine which Hogwarts House you belong to... ")

    # Question 1
    print("\nQ1) Do you like Dawn or Dusk?\n")
    print("1) Dawn")
    print("2) Dusk")

    while True:
        answer = input("\nYour answer(1/2): ")

        if answer == '1':
            GryffindorPoints += 2
            RavenclawPoints += 2
            break
        elif answer == '2':
            SlytherinPoints += 2
            HufflePuffPoints += 2
            break
        else:
            print("\nInvalid Input. Please Enter either 1 or 2.")
            
    

    # Question 2
    print("\nQ2) Do you like Forest or River?\n")
    print("1) Forest")
    print("2) River")

    while True:
        answer = input("\nYour answer(1/2): ")

        if answer == '1':
            GryffindorPoints += 2
            RavenclawPoints += 2
            break
        elif answer == '2':
            SlytherinPoints += 2
            HufflePuffPoints += 2
            break
        else:
            print("\nInvalid Input. Please Enter either 1 or 2.")
        
    
    # Question 3
    print("\nQ3) Do you like Moon or Stars?\n")
    print("1) Moon")
    print("2) Stars")

    while True:
        answer = input("\nYour answer(1/2): ")

        if answer == '1':
            SlytherinPoints += 2
            RavenclawPoints += 2
            break
        elif answer == '2':
            HufflePuffPoints += 2
            GryffindorPoints += 2
            break
        else:
            print("\nInvalid Input. Please Enter either 1 or 2.")
        

    # Question 4
    print("\nQ4) Which of the following would you most hate people to call you?\n")
    print("1) Ordinary")
    print("2) Ignorant")
    print("3) Cowardly")
    print("4) Selfish")

    while True:
        answer = input("\nYour answer(1/2/3/4): ")

        if answer == '1':
            SlytherinPoints += 2
            break
        elif answer =='2':
            RavenclawPoints += 2
            break
        elif answer == '3':
            GryffindorPoints += 2
            break
        elif answer == '4':
            HufflePuffPoints += 2
            break
        else:
            print("\nInvalid Input. Please choose one of the valid options")


    # Question 5
    print("\nQ5) After you have died, what would you most like people to do when they hear your name?\n")
    print("1) Miss you, but smile.")
    print("2) Ask for more stories about your adventures")
    print("3) Think with admiration of your achievements")
    print("4) I don't care what people think of me after I'm dead, it's what they think of me while I'm alive that counts")

    answer = input("\nYour answer(1/2/3/4): ")

    if answer == '1':
        HufflePuffPoints += 2
    elif answer == '2':
        GryffindorPoints += 2
    elif answer == '3':
        RavenclawPoints += 2
    elif answer == '4':
        SlytherinPoints += 2
    else:
        print("\nInvalid Input. Please choose one of the valid options")
        return

    # Question 6
    print("\nQ6) How would you like to be known to history?\n")
    print("1) The Wise")
    print("2) The Good")
    print("3) The Great")
    print("4) The Bold")

    while True: 
        answer = input("\nYour answer(1/2/3/4): ")

        if answer == '1':
            RavenclawPoints += 2
            break
        elif answer == '2':
            HufflePuffPoints += 2
            break
        elif answer == '3':
            SlytherinPoints += 2
            break
        elif answer == '4':
            GryffindorPoints += 2
            break
        else:
            print("\nInvalid Input. Please choose one of the valid options")
        

    # Question 7
    print("\nQ7) Given the choice, would you rather invent a potion that would guarantee you:\n")
    print("1) Love?")
    print("2) Glory?")
    print("3) Wisdom?")
    print("4) Power?")

    while True:
        answer = input("\nYour answer(1/2/3/4): ")

        if answer == '1':
            HufflePuffPoints += 2
            break
        elif answer == '2':
            GryffindorPoints += 2
            break
        elif answer == '3':
            RavenclawPoints += 2
            break
        elif answer == '4':
            SlytherinPoints += 2
            break
        else:
            print("\nInvalid Input. Please choose one of the valid options")
        
    
    # Question 8
    print("\nQ8) Once every century, the Flutterby bush produces flowers that adapt their scent to attract the unwary. \n If it lured you, it would smell of:\n")
    print("1) A crackling log fire")
    print("2) The Sea")
    print("3) Fresh Parchment")
    print("4) Home")

    while True: 
        answer = input("\nYour answer(1/2/3/4): ")

        if answer == '1':
            GryffindorPoints += 2
            break
        elif answer == '2':
            SlytherinPoints += 2
            break
        elif answer == '3':
            RavenclawPoints += 2
            break
        elif answer == '4':
            HufflePuffPoints += 2
            break
        else:
            print("\nInvalid Input. Please choose one of the valid options")

    
    # Question 9
    print("\nQ9) Four goblets are placed before you. Which would you choose to drink?\n")
    print("1) The foaming, frothing, silvery liquid that sparkles as though containing ground diamonds.")
    print("2) The smooth, thick, richly purple drink that gives off a delicious smell of chocolate and plums.")
    print("3) The golden liquid so bright that it hurts the eye, and which makes sunspots dance all around the room. ")
    print("4) The mysterious black liquid that gleams like ink, and gives off fumes that make you see strange visions.")

    while True:
        answer = input("\nYour answer(1/2/3/4): ")

        if answer == '1':
            RavenclawPoints += 2
            break
        elif answer == '2':
            HufflePuffPoints += 2
            break
        elif answer == '3':
            GryffindorPoints += 2
            break
        elif answer == '4':
            SlytherinPoints += 2
            break
        else:
            print("\nInvalid Input. Please choose one of the valid options")

    house_points = {
        'Gryffindor': GryffindorPoints,
        'Slytherin': SlytherinPoints,
        'Ravenclaw': RavenclawPoints,
        'Hufflepuff': HufflePuffPoints
    }

    maxPoints = max(house_points, key=house_points.get)
    print(f"\nCongratulations! You belong to {maxPoints}!!")

if __name__ == "__main__":
    sortingHat()