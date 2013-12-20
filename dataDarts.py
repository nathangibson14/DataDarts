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
                playGame()
                
            elif option==0:
                sys.exit(1)
                
def playGame():
        
    game = raw_input("What game would you like to play? (Options: 501, Cricket): ")
    while game != "501" and game != "Cricket":
        game = raw_input("Input error.  (Options: 501, Cricket): ")

    if game == "501":
        games.play501()



print "Welcome to dataDarts! \n"

players.initializePlayers()
mainMenu()






