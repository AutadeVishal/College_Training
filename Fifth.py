import random
from datetime import datetime

class WrongTypeError(Exception):
    def __init__(self, message="Wrong Type"):
        super().__init__(message)

name = input("Enter Your Name: ")
starttime=datetime.now()
print(starttime)
continueTheGame = True
score = 0
while continueTheGame:
    print(f"{name}'s Score is : {score}")
    random_integer = random.randint(1, 100)
    print(f"Total Time is : {total_time}")
    which_question=random.randint(1,2)
    if(which_question==1):
        question_time=datetime.now()
        sqrt = int(input(f'What is Square Root of : {random_integer}? '))
        answer_time=datetime.now()
        total_time+=answer_time-question_time

        if sqrt * sqrt == random_integer :
            score += 10
        else:
             score -= 5
    else:
        random_number=random.randint(1,100)
        perfect_square=random_number*random_number
        sqrt=int(input(f"What is Squared Root of the Number:{perfect_square}"))
        if(sqrt==random_number):
            print("correct")
        else:
            score-=5
       
    choice = input("Want to Continue? (1 for Yes / 0 for No): ")
    if choice == "1":
        continueTheGame = True
    else:
        continueTheGame = False
if(score<50):
    print("LOSER")
else :
    print("WINNER")


