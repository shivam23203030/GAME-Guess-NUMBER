import random
def guess_number(computer_number,name):
    user_number=int(input("Guess the number :: "))
    attempt=1
    while user_number!=computer_number:
        if user_number<computer_number:
            print("Too low !")
            attempt=attempt+1
            user_number=int(input(f"Hi {name},Please enter the number Again :: "))
        else:
            print("Too high !")
            attempt=attempt+1
            user_number=int(input(f"Hi {name}, Please enter the number Again :: "))
    print(f"CONGRATULATION {name} you got the number & You are very smart")
    print(f"You found this number in {attempt} attempt")
name=input("Enter Player Name :: ")
computer_number=random.randint(1,100)
print(f"----------Hi {name} WELCOME TO THE GAME----------")
print(f"---I am ROBOT,I have choosen one number between 1 & 100--- ")
guess_number(computer_number,name)