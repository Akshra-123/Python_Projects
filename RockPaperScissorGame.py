import random
choice=["rock","paper","scissor"]

while True:
    user_choice=input("Enter a choice (rock,paper,scissor):")
    possible_actions=["rock","paper","scissor"]
    computer_choice=random.choice(possible_actions)
    print("Your choice is:" + user_choice + "\n" + "Computer Choice is:" + computer_choice)
    
    if (user_choice==computer_choice):
        print("Both players selected" + user_choice + "It is a Tie!!")
    elif (user_choice=="rock"):
        if computer_choice=="scissor":
            print("rock smashes scissor...You Win!!!")
        else:
            print("Paper covers rock...Computer Wins!!!")
    elif (user_choice=="paper"):
        if computer_choice=="scissor":
            print("Scissor cuts paper...Computer Wins!!!")
        else:
            print("Paper covers rock...You win!!!")
    elif (user_choice=="Scissor".lower()):
        if (computer_choice=="paper"):
            print("Scissor cuts paper...You win!!!")
        else:
            print("Rock smashes Scissor...Computer wins!!!")

    play_again=input("want to play again? (y/n):")
    if play_again.lower() !="y":
        break