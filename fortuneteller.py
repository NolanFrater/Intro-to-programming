import random
print("It is I, the great and powerful Zuchinni, here to tell you your fortune!")

def Questions():
    try:
        number = int(input("What is you lucky number?\n"))
        future_sight = float(input("How many years into the future would you like to see?\n"))
        gamble = bool(input("Do you like to gamble? (yes/no)\n").strip().lower() == "yes")
        pets = int(input("How many pets do you have?\n"))
        game_time = float(input("How many hours do you spend playing video games per week?\n"))
        random_number = random.randint(1, 100)
        if gamble == True:
            stupid_number = (random_number * number + pets - game_time // future_sight) * 2
        else:
            stupid_number = (random_number * number + pets - game_time / future_sight) // 2

        if stupid_number > 1000:
            print("Your future is looking dim.")
        elif stupid_number > 900:
            print("You will have many hardsips in the nearby future.")
        elif stupid_number > 800:
            print("You will have many trials and tribulations in the nearby future, but you will persevere.")
        elif stupid_number > 700:
            print("You will face some challenges, but they will make you stronger.")
        elif stupid_number > 600:
            print("You will have a period of reflection and personal growth.")
        elif stupid_number > 500:
            print("You will have a period of stability and contentment.")
        elif stupid_number > 400:
            print("You will find peace and happiness in the simple things.")
        elif stupid_number > 300:
            print("You will have a period of good fortune and success.")
        elif stupid_number > 200:
            print("You have a bright future ahead of you, filled with opportunities and growth.")
        elif stupid_number > 100:
            print("You will have an exciting and adventurous future, full of new experiences and discoveries.")
        else:
            print("You will have a future filled with love, joy, and happiness, surrounded by friends and family.")

    except ValueError:
        print("Invalid input. Please enter the correct data type.")
        Questions()


Questions()