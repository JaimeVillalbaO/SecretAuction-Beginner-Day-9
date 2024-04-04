from acsi_day9 import logo
import os

print(logo)
print('\nWelcome to the secret auction program.\n')
dicc = {}


def highest_bid(dicc):
    
    bid_winner = 0
    name_winner = ''
    for k in dicc:
        if dicc[k] > bid_winner:
            bid_winner = dicc[k]
            name_winner = k

    print(f'The winner is {name_winner} with a bid of ${bid_winner}.  ')


start = 'yes'
while start == 'yes':
    name = input('What is your name? : ')
    bid = int(input('What\'s your bid? : $'))

    dicc[name] = bid

    start_again =input('Are there any other bidders? Type "yes" or "no". ').lower()
    
    if start_again == 'yes':
        start = 'yes'
        os.system('cls') 
    else: 
        start = 'no' 
        os.system('cls') 
        highest_bid(dicc)
    
    



