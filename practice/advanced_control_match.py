#advanced control flow wit match statment

day = input("Please enter the day of the  week: ").capitalize()
match day:
    case "Monday":
        print("Monday morning disease")
    case "Tuesday":
        print("Here we go. The new week has started")
    case "Wednesday":
        print("The weekend is almost here")
    case "Thursday":
        print("Its time to prepare for the weekend")
    case "Friday":
        print("Thank God it is a Friday")
    case "Saturday":
        print("Monday is almost here again")
    case "Sunday":
        print("What a weekend it was, and what a new week its gonna be")
    case _:
        print("invalid option, day should be (Monday - Sunday)")
    