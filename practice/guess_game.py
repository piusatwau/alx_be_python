#using match flow control to design guess game
# the user will guess which number I am thinking of

number = (input("I am thinking of a number betweeen 0 and 10. Guess which number it is: "))

match number:
    case "1":
        print("You are far away from the correct answer")
    case "2":
        print("Not yet")
    case "3":
        print("Got it, congratulatons")