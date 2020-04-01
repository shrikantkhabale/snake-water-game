# Snake Water Gun Game
# choose above value randomly
import random

user_count=0
comp_count=0
game=0
draw_count=0

while game<10:
    user_input=input("Please type s for snake,w for water,g for gun : ").lower()
    lst = ["s", "w", "g"]
    comp_choice = random.choice(lst)
    if user_input not in ("s","w","g"):
        print("please enter s/w/g only")
        continue
    elif user_input==comp_choice:
        print("Draw")
        draw_count+=1
    elif (user_input=="s" and comp_choice=="w") or (user_input=="w" and comp_choice=="g") or (user_input=="g" and comp_choice=="s"):
        print("You Win")
        user_count+=1
    elif (user_input=="w" and comp_choice=="s") or (user_input=="g" and comp_choice=="w") or (user_input=="s" and comp_choice=="g"):
        print("You lost")
        comp_count+=1
    game=game+1

if user_count> comp_count:
    print("you win the contest")
    print("Your win count: ",user_count,"Computer win count: ",comp_count)
elif user_count< comp_count:
    print("Computer win the Contest")
    print("Your win count: ", user_count, "Computer win count: ", comp_count,"Draw: ",draw_count)
else:
    print("Contest Draw")
    print("Your win count: ", user_count, "Computer win count: ", comp_count,"Draw: ",draw_count)

play_again=input("do you want to play this again y/n :")
if play_again=="y":
    pass
else :
    print("Thanks for playing")







