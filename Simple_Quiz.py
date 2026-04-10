def tally_score(answer, correct_answer):
    if answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect.")

print( "Welcome to the Simple Quiz, please answer the following questions to the best of your ability:")

Geography_1 =input("What is the capital of South Sudan?\n a) Juba\n b) Malakal\n c) Wau\n d) Bor\n")

tally_score(Geography_1, "a")
#1
Geography_2 =input("What is the capital of Sweden?\n a) Oslo\n b) Helsinki\n c) Copenhagen\n d) Stockholm\n")
#initially bad question, but I fixed it by changing the country to Sweden.
tally_score(Geography_2, "d")
#2
Science_1 =input("What type of element is zirconium?\n a) Metal\n b) Non-metal\n c) Metalloid\n d) Noble Gas\n")

tally_score(Science_1, "a")
#3
Science_2 =input("What is the chemical symbol for potassium?\n a) P\n b) K\n c) Po\n d) Pt\n")

tally_score(Science_2, "b")
#4
History_1 =input("Who signed the Magna Carta?\n a) King John\n b) King Richard\n c) King Henry\n d) King Edward\n")

tally_score(History_1, "a")
#5
History_2 =input("When was Spain under a dictatorship?\n a) 1920-1930\n b) 1950-1980\n c) 1939-1975\n d) 1900-1920\n")

tally_score(History_2, "c")
#6
Math_1 =input("What is the square root of 576?\n a) 24\n b) 25\n c) 26\n d) 27\n")

tally_score(Math_1, "a")
#7
Math_2 =input("What is the value of pi to 5 decimal places?\n a) 3.14159\n b) 3.14160\n c) 3.14161\n d) 3.14162\n")

tally_score(Math_2, "a")
#8
Ian_1 = input("How many hours on Minecraft does Ian have as of 4/10/2026?\n a) 10000\n b) 20000\n c) 13000\n d) 15000\n")

tally_score(Ian_1, "c")
#9
Ian_2 = input("How many cats does Ian have?\n a) 1\n b) 2\n c) 3\n d) 6487.8\n")

tally_score(Ian_2, "a")
#10

count = 0
if Geography_1 == "a":
    count += 1
if Geography_2 == "d":
    count += 1
if Science_1 == "a":
    count += 1
if Science_2 == "b":
    count += 1
if History_1 == "a":
    count += 1
if History_2 == "c":
    count += 1
if Math_1 == "a":
    count += 1
if Math_2 == "a":
    count += 1
if Ian_1 == "c":
    count += 1
if Ian_2 == "a":
    count += 1

print("You got " + str(count) + " out of 10 questions correct.")