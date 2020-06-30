#!/usr/bin/env python3
import cmd
import textwrap
import sys
import os
import time
from random import randint

os.system("clear")

class colours:
    BLACK = "\u001b[30;1m"
    RED = "\u001b[31;1m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33;1m"
    BLUE = "\u001b[34;1m"
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"
    ENDC = "\u001b[0m]"

print(colours.GREEN + "000000000000" + colours.YELLOW + "111111111111111111" + colours.BLUE + "000000000000000000000000"
+ colours.YELLOW + "11111111111111" + """[[blue]]000000000000 [[yellow]]1111111[[blue]]00000000[[yellow]]11111111111
[[blue]]00000000000[[yellow]]1[[blue]]00
[[yellow]]11111111111[[blue]]00000[[yellow]]111111111[[blue]]00000[[yellow]]1111111111
[[blue]]0000000[[yellow]]11[[blue]]0000000[[yellow]]111111111[[blue]]000000[[yellow]]1[[blue]]00000000
[[yellow]]11[[blue]]000[[yellow]]11[[blue]]0[[yellow]]11111[[blue]]00000000000000000[[yellow]]1[[blue]]0[[yellow]]11111111
[[blue]]0000000000[[yellow]]111111[[blue]]000000000[[yellow]]1111[[blue]]0000000000[[yellow]]1
[[blue]]0000000000[[yellow]]111111[[blue]]000000000[[yellow]]1111[[blue]]00000000000
[[yellow]]111111111111111[[blue]]000[[yellow]]11111[[blue]]00[[yellow]]11111[[blue]]0000000000
[[yellow]]111111111111111[[blue]]00[[yellow]]1111111[[blue]]00[[yellow]]11111111111111
[[yellow]]11111111111111[[blue]]00[[yellow]]111111111[[blue]]0[[yellow]]11111111111111
[[yellow]]111111111111[[blue]]000[[yellow]]11111111111[[blue]]0000[[yellow]]1111111111
[[yellow]]1111111111[[blue]]000[[yellow]]11111111111111[[blue]]000[[yellow]]1111111111
[[yellow]]1111111111111111111111111111111111111111
[[yellow]]11111111111111[[blue]]0000000000000[[yellow]]1111111111111
[[yellow]]11111111[[blue]]00[[yellow]]1[[blue]]000000000000000000[[yellow]]11111111111
[[yellow]]1111111[[blue]]000000000000000000000000[[yellow]]111111111
[[yellow]]11111111111[[blue]]00000[[yellow]]1111[[blue]]0[[yellow]]11111[[blue]]0000[[yellow]]1111111111
[[yellow]]1111111111111111111111111111111111111111
[[yellow]]1111111111111111111111111111111111111111
[[yellow]]11111[[blue]]0[[yellow]]1111111111111111111111111111111111
[[blue]]0000000[[yellow]]11111[[blue]]0000[[yellow]]111[[blue]]00000000000[[yellow]]111[[blue]]00[[yellow]]11111
[[blue]]0000000000000000000000000000000000000[[yellow]]111
[[blue]]0000000000000000[[yellow]]111[[blue]]0000[[yellow]]11[[blue]]000000000000[[yellow]]111
[[blue]]00000000000000000[[yellow]]11[[blue]]000[[yellow]]1[[blue]]00000000000000[[yellow]]111
[[blue]]00000000000000000000[[yellow]]1111[[blue]]0000000[[yellow]]111111111
[[blue]]0000[[yellow]]111111[[blue]]0000000000000000000[[yellow]]11111111111
[[blue]]0000[[yellow]]111111[[blue]]000000000000000[[yellow]]111111111111111
[[yellow]]1[[blue]]000[[yellow]]1111111[[blue]]00000000000000[[yellow]]111111111111111
[[yellow]]111111111111111[[blue]]000000000[[yellow]]1111111111111111[[white]]""")

'''
f = open("binaryhartman2.txt","r")
ascii = "".join(f.readlines())
print(colourText(ascii))
'''

class character:
  def __init__(self):
    self.name = ""
    self.health = 1
    self.health_max = 1
  

class Player(character):
  def __init__(self):
    self.name = ''
    self.age = ''


class Enemy(character):
  def __init__(self):
    self.name = ''
    self.health = randint(1, 100)

def oneortwo():
    option = input()

    while option != "1" and option != "2":
      print("Please press 1 or 2")
      print("""
      1)Yes
      2)No
      """)
      option = input()
    
    if option == ("1"):
        print("Let's continue")
    elif option == ("2"):
        character_creation()

def confirm():
    
    print("""
    1)Yes   
    2)No
    """)
    oneortwo()

p = Player()
e = Enemy()


def character_creation():    
    p.name = input("What's your name? ")
    p.age =  input("How old are you? ")

    try:
        val = int(p.age)
    except ValueError:
        print("Your age must be an integer! (duh)")
        character_creation()
    else:
        print("Your name is {} and you are {} years old. Is this correct?".format(p.name,p.age))
        confirm()



### Main Menu ###
def menu_selections():
    option = input()
    while option != "1" and option != "2" and option != "3" and option != "4":
        print(colours.WHITE + "\n")
        print("##########################")
        print("# The Hartman Chronicles #")
        print("##########################")
        print("#       " + colours.RED + "1)" + colours.WHITE + "New Game       #")
        print("#       " + colours.RED + "2)" + colours.WHITE + "Load Game      #")
        print("#       " + colours.RED + "3)" + colours.WHITE + "Help           #")
        print("#       " + colours.RED + "4)" + colours.WHITE + "Quit           #")
        print("#Copyright 2020 Chensoft #")
        print("##########################")
        print("\nPlease press " + colours.RED + "1" + colours.WHITE + ", " + colours.RED + "2" + colours.WHITE + ", " + colours.RED + "3 " + colours.WHITE + "or " +colours.RED + "4" +colours.WHITE + "\n")
        option = input()
        
    if option == ("1"):
        character_creation()
    elif option == ("2"):
        character_creation()
    elif option == ("3"):
        main_menu()
    elif option == ("4"):
        print("Good Bye!")
        sys.exit()
    else:
        main_menu()
    
def main_menu():
    print(colours.WHITE + "\n")
    print("##########################")
    print("# The Hartman Chronicles #")
    print("##########################")
    print("#       " + colours.RED + "1)" + colours.WHITE + "New Game       #")
    print("#       " + colours.RED + "2)" + colours.WHITE + "Load Game      #")
    print("#       " + colours.RED + "3)" + colours.WHITE + "Help           #")
    print("#       " + colours.RED + "4)" + colours.WHITE + "Quit           #")
    print("#Copyright 2020 Chensoft #")
    print("##########################")
    print("\nPlease press " + colours.RED + "1" + colours.WHITE + ", " + colours.RED + "2" + colours.WHITE + ", " + colours.RED + "3 " + colours.WHITE + "or " +colours.RED + "4" +colours.WHITE + "\n")
    menu_selections()

main_menu()
input("Press any key to quit...")
