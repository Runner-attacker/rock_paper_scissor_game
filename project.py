import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

choice_option = """
Choose:
Rock,
Paper,
Scissor
"""
options = ["rock", "paper", "scissor"]

statement = {
    "user": 0,
    "computer": 0
}

def main():
    user_choice = input(choice_option).lower()
    print(f"\nUser Choice: {user_choice}")

    if user_choice == "rock":
        print(rock)
    elif user_choice == "paper":
        print(paper)
    elif user_choice == "scissor":
        print(scissor)
    else:
        print("Invalid choice! Please choose rock, paper, or scissor.")
        return  

    computer_choice = random.choice(options)
    print(f"\nComputer Choice: {computer_choice}")

    if computer_choice == "rock":
        print(rock)
    elif computer_choice == "paper":
        print(paper)
    else:
        print(scissor)

    # Determining the winner
    if user_choice == computer_choice:
        print(f"Both chose {user_choice}. It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "scissor" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print(f"You chose {user_choice}, computer chose {computer_choice}. You win!")
        statement["user"] += 1
    else:
        print(f"You chose {user_choice}, computer chose {computer_choice}. You lose!")
        statement["computer"] += 1

    # Displaying the Score
    print(f"\nScore -> You: {statement['user']} | Computer: {statement['computer']}")

# Looping the Game
continuity = True
while continuity:
    main()
    resume = input("Do you want to continue (y/n)? ").lower()
    if resume == 'n':
        continuity = False
        print("Final Score:")
        print(f"\nScore -> You: {statement['user']} | Computer: {statement['computer']}")
    elif resume != 'y':
        print("Invalid input! Please enter 'y' to continue or 'n' to quit.")
