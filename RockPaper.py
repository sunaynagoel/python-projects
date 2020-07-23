# Sunayna Goel
# July 23rd
# First Python project after completing freeCodeCamp
# beginner course on Youtube: https://www.youtube.com/watch?v=rfscVS0vtbw
# Rock Paper Scissors

# import random   # import random for use of random integer

# Print multi line instruction
# perform string concatenation of string
import random

print("Winning Rules of the Rock paper scissor game as follows: \n"
       "Rock vs paper --> paper wins \n"
       "Rock vs scissor --> Rock wins \n"
       "paper vs scissor --> Scissor wins \n")

def game():
    print("Enter choice \n 1. Rock \n 2. Paper \n 3. Scissor \n")
    # take the input from user
    choice = int(input("User turn: "))

    # looping until user enter invalid input
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input between 1 and 3: "))
        # initialize value of choice_name variable
        # corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'Scissor'

        # print user choice
    print("user choice is: " + choice_name)
    print("\nNow its computer's turn.......")

    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)
    # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'Scissor'

    print("Computer choice is: " + comp_choice_name)
    print(choice_name + " V/s " + comp_choice_name)
    ans = "yes"
    while ans == "yes":

        #if choice_name == comp_choice_name:
           # print("Its a Tie, Try Again!!")

        if ((choice == 1 and comp_choice == 2) or
              (choice == 2 and comp_choice == 1)):
              print ("Paper Wins")
              result = "Paper"
        elif ((choice == 1 and comp_choice == 3) or
               (choice == 3 and comp_choice == 1)):
               print("Rock Wins")
               result = "Rock"
        else :
               print("Scissor Wins")
               result = "Scissor"

        if   result == choice_name:
             print("<== User wins ==>")
        else :
            print("<== Computer wins, Try again ! ==>")


        ans = input("\nDo you want to play again? Enter Yes or No: ")

        if   ans.lower() == "no" or ans.lower() == "n":
            print("Thanks for playing !!")
            break
        elif ans.lower() == "yes" or ans.lower() == "y":
             game()
        else:
            print("Invalid Input !!")


game()

