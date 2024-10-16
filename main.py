import art
import random

game_images = [art.rock, art.paper, art.scissors]
game_list = ['rock', 'paper', 'scissors']
user_value = -1

user_choice = input("What do you choose? Type 'Rock', 'Paper' or 'Scissors'.\n").lower()
while user_choice not in game_list:
    user_choice = input("Your choice doesn't correct. Type 'Rock', 'Paper' or 'Scissors'.\n").lower()

for name in game_list:
    if name == user_choice:
        user_value = game_list.index(user_choice)

print(f"Your chose is {game_list[user_value]}.")
print(game_images[user_value])

computer_choice = random.randint(0, 2)
print(f"Computer chose is {game_list[computer_choice]}.")
print(game_images[computer_choice])


if user_value == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_value == 2:
    print("You lose!")
elif computer_choice > user_value:
    print("You lose!")
elif user_value > computer_choice:
    print("You win!")
elif computer_choice == user_value:
    print("It's a draw!")