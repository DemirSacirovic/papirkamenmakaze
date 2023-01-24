import random

options=('rock', 'papper', 'scissors')

playing = True
while playing:

    player= None
    computer = random.choice(options)
    while player not in options:
      player = input('Enter a choice(rock,papper, scissors):')

    print(f'player:{player}')
    print(f'computer:{computer}')


    if player==computer:
        print ('Its a tie!')
    elif player=='rock' and computer=='scissors':
        print ("You win")
    elif player=='papper' and computer=='rock':
        print ("You win")
    elif player=='scissors' and computer=='papper':
        print ("You win")
    else :
        print ("You lose")

    if not input("Play again? (y/n):").lower()=="y":
        playing = False

print ("Thanks for playing")









