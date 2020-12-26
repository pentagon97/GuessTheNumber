from random import randint
import datetime
top_range=int(input("Enter the top range for the guessing number : "))
num_range=0, 100
number=randint(*num_range)
current_date=datetime.datetime.now()
while True:
    try:
        user_num = int(
            input(f"Guess a number between {num_range[0]}-{num_range[1]}: "))
        if user_num > number:
            print("Too high,try again!")
        elif user_num < number:
            print("Too low,try again!")
        else:
            print("Correct guess!")
            f = open("GuessHistory", "a")
            f.write("\nCorrect guess! \t"+str(current_date))
            f.close()
            break
    except ValueError:
        print('Please input a valid number!')
    print()
