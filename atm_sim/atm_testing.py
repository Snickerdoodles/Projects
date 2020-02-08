#!/usr/bin/env python3

import time
import os
from termcolor import colored

def main():
    login()

def login():
    while True:
        username = input('Please enter username: ')
        pin = input('Please enter your pin: ')

if __name__ == "__main__":
    user_pins = {'david':'1234'}
    locked_accs = []
    acc_balances = {'david':[100,200,300]}
    user_login_attempts = {}
    login()
