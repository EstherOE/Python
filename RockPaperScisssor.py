from random import randint
player = input("rock(r), paper(p), scissors(s)")
print(player,'vs', end = ' ')
choosen= randint(1,3)
if choosen == 1:
   computer = "Rock"
elif choosen == 2:
     computer == "Paper"
else:
    computer = "Scissors''
print(computer)

if player ==computer:
   print("Draw1")
elif player == 'r' and computer == 's':
    print('Player wins')
elif player =='r' and computer == 'p':
    print("Computer wins")
elif player == 'p' and computer == 'r':
    print('Player wins')
elif player =='p' and computer == 'p':
    print("Computer wins")
