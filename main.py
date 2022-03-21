#Basic Concepts
'''
# a = ord("k")
# print(ord("k"))
# print(bin(a))
# print(int("1101011",2))
# print(chr(100))

'''

import platform
import os
import colorama
from colorama import Fore, Back , Style
import pyperclip

colorama.init()

logo = Fore.GREEN+'''    ____     ______   ______                           __           
   / __ )   /_  __/  / ____/___  ____ _   _____  _____/ /____  _____
  / __  |    / /    / /   / __ \/ __ \ | / / _ \/ ___/ __/ _ \/ ___/
 / /_/ /    / /    / /___/ /_/ / / / / |/ /  __/ /  / /_/  __/ /    
/_____/    /_/     \____/\____/_/ /_/|___/\___/_/   \__/\___/_/     
                                                                    

'''+Fore.RESET

def encrypt(text):
    text = str(text)
    ords = []
    for letter in text:
        ords.append(ord(letter))

    bins = []
    for o in ords:
        bins.append(bin(o))

    pr_bins = []
    for i in bins:
        i = i[2:]
        pr_bins.append(i)

    binary_output = " ".join(pr_bins)
    pyperclip.copy(binary_output)
    print(f"\n The Binary is : \n{Fore.GREEN+binary_output+Fore.RESET}")



def decrypt(binary):
    binary = binary.split(" ")

    ints = []
    for b in binary:
        ints.append(int(b,2))

    chars = []
    for i in ints:
        chars.append(chr(i))

    text_output = ''.join(chars)
    pyperclip.copy(text_output)
    print(f"\n The decoded text is : {Fore.BLUE+text_output.title()+Fore.RESET}")



if __name__ == '__main__':

    should_continue = True
    while should_continue:
        if platform.system() == "Linux":
            os.system('clear')
        else:
            os.system('cls')
        print(logo)
        direction = input(Fore.LIGHTBLUE_EX+" Type 'e' to encrypt, type 'd' to decrypt:\n "+Fore.RESET)
        text = input(Fore.GREEN+" Type your message:\n "+Fore.RESET).lower()
    

        if direction == 'd':
            decrypt(text)
        elif direction == 'e':
            encrypt(text)

        choice = input("\n\n Type 'y' if you want to go again. Otherwise, type 'n'  >> ")
        if choice =="n":
            print(" GoodByee")
            break
