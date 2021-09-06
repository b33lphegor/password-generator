#!/usr/bin/python3
import sys, os
import random
from termcolor import colored
from string import digits, ascii_letters, punctuation


def main():
    print(colored('\t             ............          ', 'blue'))
    print(colored('\t      _______| Encrypted |______  ' , 'blue'))
    print(colored('\t     /..........................\\ ', 'blue'))
    print(colored('\t    ____| Password Generator |____ ', 'blue'))
    print(colored('\t   \\____________________________/', 'blue'))
    print()
    print(colored('\t\t\t\tALL CREDITS TO B33lphegor\n\n'))


if __name__ == '__main__':
    try:
        main()
        while True:
            try:
                _password_len = int(input(colored('[-] Enter Password Length : ', 'blue')))
                _symbols = digits + ascii_letters + punctuation
                _secure_random = random.SystemRandom()

                _secure_password = "".join(_secure_random.choice(_symbols) for i in range(_password_len))
                print(colored(f'[+] Secure Random Password : {_secure_password}', 'green'))
            except (EOFError, ValueError) as error:
                print(colored('\n[-] Invalid Input Enter An Integer', 'red'))
    except KeyboardInterrupt:
        print(colored('[-] Program Quiting...Goodbye', 'red'))
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
