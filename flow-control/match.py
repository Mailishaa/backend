day = str(input ("Enter Day: "))
match day:
    case " Monday":
        print("Start of the week")
    case "Friday":
        print("End of week")
    case "Tuesday":
        print("Second day")

    case _:
        print("Regular Day")