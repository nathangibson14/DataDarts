#!/usr/bin/python

import games
import players
import sys

def mainMenu():
    while True:
    
        print """
Main Menu
1 -- Manage Players
2 -- Play Game
0 -- Exit dataDarts\n"""
        
        while True:
            option = input("Input option: ")

            if option==1:
                players.managePlayers()
                break
                
            elif option==2:
                games.setupGame()
                break
                
            elif option==0:
                sys.exit(1)


print "Welcome to dataDarts! \n"

players.initializePlayers()
mainMenu()






