number1=int(input("Enter Number: "))
match number1:
    case 1|3|5|7|8|10|12:
        print("31")
    case 2:
        print("28 or 29")
    case 4|6|9|11:
        print("30")
    case _:
        print("Invalid Number")