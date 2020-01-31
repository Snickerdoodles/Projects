#!/usr/bin/env python3

import time
import os
from termcolor import colored


# Databases
username_PINS = {'david':'1234'}   # usernames & passwords
acc_balances = {'david':[100,200,300]}   # username:[chequing, savings, credit]
locked_accs = []                   # list of locked accs
username = ''

def login():
    print(colored('#### LOGIN ####', 'green'))
    user_login_attempts = {}
    while True:
        username = input('\nUsername: ')
        pin = input('\nPIN: ')
        os.system('clear')
        # START ATTEMPT COUNTER
        if username not in user_login_attempts.keys():
            user_login_attempts[username] = 3
        # CHECK IF ACC LOCKED
        if username not in locked_accs:
            # VALID CREDENTIALS
            try:
                if username_PINS[username] == pin:
                    os.system('clear')
                    time.sleep(1)
                    print(colored('\nWelcome ' + username + '!' + '\n', 'green'))
                    time.sleep(1.5)
                    break
            # INVALID CREDENTIALS
            except:
                print(colored('\nIncorrect username or password.', 'red'))
                user_login_attempts[username] -= 1
                if user_login_attempts[username] == 0:
                    locked_accs.append(username)
        # LOCK ACCOUNT
        else:
            print(colored('\nThis account has been locked due to too many failed login attempts.', 'red'))
            # RETRY/EXIT
            retry_exit = input('\nWould you like to try a different account? Enter no to exit program. (y/n): ')
            if retry_exit == 'n':
                exit()
    return username

def menu(user):
    while True:
        os.system('clear')
        print(colored('Welcome ' + user + "!", 'green'))
        print(
        '\n1) Account Balances' +
        '\n2) Cash Withdrawal' +
        '\n3) Deposit' +
        '\n4) Change PIN' +
        '\n5) Transfer Funds' +
        '\n6) Recent Transactions'
        '\n7) Exit')
        action = input(colored('\nPlease select action: ', 'yellow'))

        # ACCOUNT BALANCES
        if action == '1':
            os.system('clear')
            balances = acc_balances[user]
            print(colored('#### ACCOUNT BALANCES ####', 'green'))
            print(
            '\n\nCHEQUING: ', balances[0],
            '\n\nSAVINGS: ', balances[1],
            '\n\nCREDIT: ', balances[2]
            )
            input("\n\nPress Enter to return to menu")

        # CASH WITHDRAW
        

        # DEPOSIT

        # CHANGE PIN

        # TRANSFER FUNDS

        # RECENT TRANSACTIONS

        # EXIT
        if action == '7':
            exit()

        





if __name__ == "__main__":
    os.system('clear')
    user = login()
    menu(user)