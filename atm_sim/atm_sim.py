#!/usr/bin/env python3

import time
import os
from termcolor import colored

def main():
    os.system('clear')
    user = login()
    os.system('clear')
    while True:
        #print(print_menu(user))
        selection = input(colored('\n\nPlease select an action: ', 'yellow'))
        if selection == "1":
            print_balances(user)
            input(colored("\nPress Enter to continue...", 'yellow'))
        elif selection == "2":
            print_balances(user)
            acc_withdraw = input(colored('\nSelect account to withdraw funds from: ', 'yellow'))
            os.system('clear')
            deposit_withdraw('withdraw', acc_withdraw, user)
        elif selection == "3":
            print_balances(user)
            acc_withdraw = input(colored('\nSelect account to withdraw funds from: ', 'yellow'))
            os.system('clear')
            deposit_withdraw('withdraw', acc_withdraw, user)
        elif selection == "4":
            print('DWADWAD')
        elif selection == "5":
            pass
        elif selection == "6":
            pass
        elif selection == "7":
            exit()
        else:
            print(colored('Invalid selection, please select again.', 'red'))


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
                    print(colored('\nWelcome ' + username.capitalize() + '!' + '\n', 'green'))
                    time.sleep(1)
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

def print_menu(user):
    print(colored('Welcome ' + user.capitalize() + '!', 'green'))
    print('''
    1) Account Balances
    2) Withdraw Funds
    3) Deposit Funds
    4) Change PIN
    5) Transfer Funds
    6) Recent Transactions
    7) Exit ''')

def print_balances(user):
        os.system('clear')
        balances = user_balances[user]
        print(colored('#### ACCOUNT BALANCES ####', 'green'))
        print(
        '\n\n1) CHEQUING: $', balances[0],
        '\n\n2) SAVINGS: $', balances[1],
        '\n\n3) CREDIT: $', balances[2]
        )

def deposit_withdraw(action, account, user):
    print(colored('##########################', 'green'))
    print(colored('##### ' + action.capitalize() + ' Funds #####', 'green'))
    print(colored('##########################', 'green'))
    balances = user_balances[user]
    print('\n\nAvailable Funds:', balances[int(account)-1])
    balance_change = input(colored('\n\nEnter ' + action + ' amount: ', 'yellow'))
    print('x')

def change_pin():
    pass

if __name__ == "__main__":
    # Databases
    username_PINS = {'david':'1234'}   # usernames & passwords
    user_balances = {'david':[100,200,300]}   # username:[chequing, savings, credit]
    locked_accs = []                   # list of locked accs
    main()