#!/usr/bin/env python3

import time
import os
from termcolor import colored


# Databases
username_PINS = {'david':'1234'}   # usernames & passwords
acc_balances = {'david':[0,0,0]}   # username:[chequing, savings, credit]
locked_accs = []                   # list of locked accs

def login():
    username = input('\nUsername: ')
    pin = input('\nPIN: ')
    try:
        if username_PINS[username] == pin:
            os.system('clear')
            time.sleep(1)
            print('\nWelcome ' + username + '!' + '\n')
            time.sleep(1.5)
    except:
        print('\nIncorrect username or password.')
        





if __name__ == "__main__":
    os.system('clear')
    login()