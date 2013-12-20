import players

#===============================================================================
def play501(people):
    print "\nPlaying 501"    
    num_people = len(people)

    score = [501 for i in range(num_people)] 

    while min(score) != 0:
        for i in range(num_people):
            displayScore(people,score)
            total = input( "Player {0}: ".format(people[i]) )
            while total < 0 or total > 180:
                total = input( "Invalid entry.  Player {0}: ".format(people[i]) )
            
            if total <= score[i]:
                score[i] = score[i] - total

            else:
                print "  Bust."

            if score[i] == 0:
                print "{0} wins!".format(people[i])
                break



#===============================================================================
def displayScore(names,score):
    print "\nScore:"
    for i in range(len(score)):
        print "  {0}: {1}".format(names[i],score[i])
    print

#===============================================================================
def setupGame():
    people = []
    num_people = 0
    game = '501'
    sets = 1
    legs = 1
    
    while True:
        
        print """
Game Menu

Current Game: {0}
Match: race to {1} sets
Set: race to {2} legs
Players:""".format(game,sets,legs)

        if num_people==0:
            print "    None"

        for p in people:
            print "    {0}".format(p) 

        print """
1 -- Play Game
2 -- Change Game 
3 -- Change Sets/Legs
4 -- Manage Game Players
0 -- Main Menu
        """
        
        
        option = input("Input option: ")
        
        if option==0:
            break
            
        elif option==1:
            if num_people==0:
                print "Error!  At least one player is required."
                continue
            
            play501(people)
            break
            
        elif option==2:
            print "501 is the only available game."
            
        elif option==3:
            sets = input("Match: Race to X sets: ")
            legs = input("Set: Race to X legs: ")
            
        elif option==4:
            people = manageGamePlayers(people)
            num_people = len(people)
            
        else:
            break
            
            
            
            
def manageGamePlayers(people):
    while True:
        print "\nCurrent players:"
        for p in people:
            print "    {0}".format(p)
        if len(people)==0:
            print "    None"
            
        print """
1 -- Add Player
2 -- Remove Player
0 -- Back
"""

        option = input("Input option: ")
        
        if option==0:
            break
            
        elif option==1:
            name = raw_input("Input name: ")
            exists = players.playerExists(name)
            if exists:
                people.append(name)
                
            else:
                print "Error!  Player {0} not in database.".format(name)
                
    return people
        
        
        

