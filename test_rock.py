import  random

print('WELCOME TO ROCK, PAPER, SCISSOR GAME\n')
user_choice = ['r','p','s']
system = ('rock','paper','scissor')
play_again = ('y','n')

def start():
    user = None
    while user not in user_choice:
        user = input('rock, paper or scissor?: ').lower()

    system_choice = random.choice((system))
    print(f'you choosed = {user} \ncomputer choosed = {system_choice}')


    if (user == 'r' and system == 'scissor') or (user == 'p' and system == 'rock') or (user == 's' and system == 'paper'):
        print('you won')
    else:
        print('you lose')

    repeat = None
    while repeat not in play_again:
        repeat = input('play again (y/n)? : ').lower()

        if repeat == 'y':
            print(start())

        else:
            break

start()
