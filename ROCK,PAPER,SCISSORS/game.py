rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
play = [rock,paper,scissors]
opt = int(input("enter 1 for rock,2 for paper and 3 for scissors: "))
print(f"you choose {play[opt-1]}")
rand = random.choice(play)
print(f"computer choose {rand}")
if play[opt-1] == rand :
    print("It's a tie ")
elif play[opt-1] == rock and rand == scissors:
    print("You Win")
elif play[opt-1] == paper and rand == rock:
    print("You Win")
elif play[opt-1] == scissors and rand == paper:
    print("You Win")
else:
    print("You Lose")
