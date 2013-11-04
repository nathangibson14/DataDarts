def play501():
    print "\nPlaying 501"
    num_players = input("Enter number of players: ")

    players = []    
    for i in range(num_players):
        players.append( raw_input("Enter player {0} email: ".format(i+1)) )
    

    print

    score = [501 for i in range(num_players)] 

    while min(score) != 0:
        for i in range(num_players):
            displayScore(players,score)
            total = input( "Player {0}: ".format(players[i]) )
            while total < 0 or total > 180:
                total = input( "Invalid entry.  Player {0}: ".format(players[i]) )
            
            if total <= score[i]:
                score[i] = score[i] - total

            else:
                print "  Bust."

            if score[i] == 0:
                print "{0} wins!".format(players[i])
                break



#===============================================================================
def displayScore(names,score):
    print "\nScore:"
    for i in range(len(score)):
        print "  {0}: {1}".format(names[i],score[i])
    print

#===============================================================================
