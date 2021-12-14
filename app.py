import math
import random
#print('Hello World!! \nI am Pasindu Herah...')
#print("\n*\n"*10)

#price = 10
#print(price)

#name = input('What is your name? ')
#colour=input("What is the favourite colour? ")
#print("My name is  " + name + ". My favourite colour is " + colour)

#birth_year = input("What is your birth year? ")
#current_year = input("What is the current Year? ")
#Age = int(current_year) - int(birth_year)

#print("Your Age: "+ str(Age))

#pounds = input("What is your weight?(in pounds) ")
#kg=float(pounds)/2.20462
#print("Your weight: "+str(kg)+"kg")

#course = '''
#Hi Pasindu,

#This is aoutamted mail. Don't respond this.

#Thank you.
#Supporting Staff.'''
#print(course)

#course="Python for beginnerss"
#index_Out=input("Index of character that you want to retrieview: ")
#print(course[int(index_Out)])

#list =[]
#course = "Python for beginers."
#course2 = "Jennifer"
#print(course2[1:4])
#for i in range(0,2):
 #   if(i == 1):
      #  ele=int(input("Enter the end index of the range: "))
    #else:
  #      ele = int(input("Enter the start index of the range: "))

    #list.append(ele)

#print(course[list[0]:list[1]])

#first='Pasindu'
#last='Herath'
#msg = f'{first} [{last}] is a coder.'
#print(msg)

#print(len("Pasindu"))

#print(10**10)
#print(10%2)

#x=10
#x=x+3
#print(x)

#x=10
#x += 3
#print(x)

#x=(3+2)*10-3
#print(x)

#print(math.ceil(2.4))

#is_hot=False
#if is_hot:
#    print("It's a hot day")
#print("Enjoy your day.")

#is_hot=False
#is_cold=False

#if is_hot:
#    print("It's a hot day.")
#    print("Drink plenty of water.")
#elif is_cold:
 #   print("It's a cold day.")
 #   print("Wear warm clothes.")
#else:
 #   print("It's a lovely day.")
#print("Enjoy your day.")

#price=1000000
#is_goodCredit = True

#if is_goodCredit:
#    downpayment=(price/100)*10
#else:
#   downpayment=(price/100)*20
#print(f"Your down payment: Rs.{downpayment}")

#has_high_incom=True
#has_good_credt=False

#if has_high_incom and has_good_credt:
#      print("Eligible for loan.")
#else:
#    print("Not Eligible for the loan.")

#name = input("Enter the name : ")
#if len(name) < 3:
#    print("Name must be at least 3 characters.")
#elif len(name) > 50:
#    print("Name can be a maximum of 50 characters.")
#else:
#    print("Name looks good !!")

#weight=float(input("Enter weight : "))

#measure=input("(L)lbs or (K)kg : ")

#if measure == "L" or measure == "l":
#    kilos=weight/2.205
#    print(f"You are {math.ceil(kilos)} Kg.")
#elif measure == "K" or measure == "k":
#    lbs=weight*2.205
#    print(f"You are {math.ceil(lbs)} lbs.")
#else:
#    print("Please,recheck the inserted value.")
#    exit()

#i=1
#while i <= 5:
#    print(i)
#    i=i+1
#print("Done")

#i=0
#print("Guess the random number...")
#randomNum = random.randrange(1,10)
#print(randomNum)
#guessNumber = int(input("Write the guessed number: "))
#if guessNumber != math.ceil(randomNum):
#    print("You have guessed the wrong number")
#    while i < 2:
#        guessNumber = int(input("Write the guessed number: "))
#        if guessNumber == math.ceil(randomNum):
#            print(f"****** You have guessed the correct number ******\n\t\t\tCorrect Number is {randomNum}")
#        else:
#            print("You have guessed the wrong number")
#        i +=1
#    print("\n***** You have taken all three attempts ******\n\t\t\tTry Again Later....")
#else:
#    print(f"****** You have guessed the correct number ******\n\t\t\tCorrect Number is {randomNum}")

print("NFS Hot Pursuit")
command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "help":
        print("Start - to start the car\nStop - to stop the car\nQuit - to exit ")
    elif command == "start":
        print("Car is started... Ready to go!")
    elif command == "stop":
        print("Car is stopped!")
print("See you later !!")

