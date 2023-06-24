import random
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
u = int(input("What do you want to choose, press 0 for rock, press 1 for paper or press 2 for scissors? "))
if u == 0:
    print("You  chose ", rock)
elif u == 1:
    print("You chose ", paper)
else:
    print("You chose ", scissors)

m = random.randint(0, 2)
if m == 0:
    print("Machine  chos\n ", rock)
elif m == 1:
    print("Machine chose\n", paper)
else:
    print("Machine chose\n", scissors)


if u == m:
    print("Game Tied, Try Again")
elif (u == 0 and m == 2) or (u == 1 and m == 0) or (u == 2 and m == 1):
    print("congrats!! You Win")
elif (m == 0 and u == 2) or (m == 1 and u == 0) or (m == 2 and u == 1):
    print("bam!! You Lose")
