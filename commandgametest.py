#!/usr/bin/env python3
import cmd
import textwrap
import sys
import os
import time
import random

os.system("cls")

COLOURS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
"red-background":"\u001b[41;1m",
}

def colourText(text):
    for colour in COLOURS:
        text = text.replace("[[" + colour + "]]", COLOURS[colour])
    return text
  

hartman = """[[blue]]000000000000[[yellow]]111111111111111111[[blue]]0000000000
00000000000000[[yellow]]11111111111111[[blue]]000000000000
[[yellow]]1111111[[blue]]00000000[[yellow]]11111111111[[blue]]00000000000[[yellow]]1[[blue]]00
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
[[yellow]]111111111111111[[blue]]000000000[[yellow]]1111111111111111[[white]]"""

print(colourText(hartman))

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
    self.health = randint(1, player.health)

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

def character_creation():    
    p.name = input("What's your name? ")
    p.age =  input("How old are you? ")
    print("Your name is {} and you are {} years old. Is this correct?".format(p.name,p.age))
    confirm()

### Main Menu ###
def menu_selections():
    option = input()
    while option != "1" and option != "2" and option != "3" and option != "4":
        print("##########################")
        print("# The Hartman Chronicles #")
        print("##########################")
        print("#       1) New Game      #")
        print("#       2) Load Game     #")
        print("#       3) Help          #")
        print("#       4) Quit          #")
        print("#Copyright 2020 Chensoft #")
        print("##########################")
        print("\nPlease press 1, 2, 3 or 4\n")
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
    print("\n")
    menu1 = "##########################"
    menu2 = "# The Hartman Chronicles #"
    menu3 = "##########################"
    menu4 = "#       [[red]]1) [[white]]New Game      #"
    menu5 = "#       [[red]]2) [[white]]Load Game     #"
    menu6 = "#       [[red]]3) [[white]]Help          #"
    menu7 = "#       [[red]]4) [[white]]Quit          #"
    menu8 = "#Copyright 2020 Chensoft #"
    menu9 = "##########################"
    menu10 = "\nPlease press [[red]]1[[white]], [[red]]2[[white]], [[red]]3 [[white]]or [[red]]4\n"
    print(colourText(menu1))
    print(colourText(menu2))
    print(colourText(menu3))
    print(colourText(menu4))
    print(colourText(menu5))
    print(colourText(menu6))
    print(colourText(menu7))
    print(colourText(menu8))
    print(colourText(menu9))
    print(colourText(menu10))
    menu_selections()

main_menu()
input("Press any key to quit...")
