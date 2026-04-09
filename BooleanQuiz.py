print("welcome to the Boolean Expressions Quiz!") #I was having a little trouble with some of the typing because some idiot switched the m and n keys.

quiz_1 = input("enter a whole number that is greater than 10:\n")
quiz_1 = int(quiz_1) > 10
quiz_2 = input("enter a whole number that is less than 5:\n")
quiz_2 = int(quiz_2) < 5
quiz_3 = input("enter a whole number that is greater than 873:\n")
quiz_3 = int(quiz_3) > 873
quiz_4 = input("enter a whole number that is less than 78:\n")
quiz_4 = int(quiz_4) < 78
quiz_5 = input("enter a whole number that is greater than 1000:\n")
quiz_5 = int(quiz_5) > 1000

quiz_6 = input("enter a whole number that is less than 100 and greater than 50:\n")
quiz_6 = int(quiz_6) < 100 and int(quiz_6) > 50
quiz_7 = input("enter a whole number that is greater than 385 or less than 239:\n")
quiz_7 = int(quiz_7) > 385 or int(quiz_7) < 239
quiz_8 = input("enter a whole number that is not less than 8989 or greater than 7986:\n")
quiz_8 = int(quiz_8) >= 8989 or int(quiz_8) <= 7986

correct = 0
if quiz_1 == True:
    correct += 1
if quiz_2 == True:
    correct += 1
if quiz_3 == True:
    correct += 1
if quiz_4 == True:
    correct += 1
if quiz_5 == True:
    correct += 1
if quiz_6 == True:
    correct += 1
if quiz_7 == True:
    correct += 1
if quiz_8 == True:
    correct += 1

print("you got " + str(correct) + "/8 correct!")