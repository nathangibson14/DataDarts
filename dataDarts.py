#!/usr/bin/python

import games

print "Welcome to dataDarts! \n"

game = raw_input("What game would you like to play? (Options: 501, Cricket): ")
while game != "501" and game != "Cricket":
    game = raw_input("Input error.  (Options: 501, Cricket): ")

if game == "501":
    games.play501()
