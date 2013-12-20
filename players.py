import sqlite3 as lite

def initializePlayers():
    con = lite.connect('players.db')
    
    with con:
        c = con.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS Players(Id INTEGER PRIMARY KEY, Name TEXT)")


def displayPlayers():
    con = lite.connect('players.db')
    
    with con:
        
        c = con.cursor()
        c.execute("SELECT * FROM Players")
        while True:
            data = c.fetchone()
            
            if data == None:
                break
                
            print data[0], data[1]


def managePlayers():
    while True:
        
        print """
Player Menu
1 -- Display Players
2 -- Add Player
3 -- Remove Player
0 -- Main Menu
        """
    
        option = input("Input option: ")
        
        if option==0:
            break
            
        elif option==1:
            displayPlayers()
            
        elif option==2:
            addPlayer()
            
        elif option==3:
            removePlayer()
        
        else:
            continue
        
        
    
def addPlayer():    
    name = raw_input('Enter player name: ')
    name = name.strip()
    
    con = lite.connect('players.db')
    
    with con:
        c = con.cursor()
        
        c.execute("SELECT * FROM Players WHERE Name == '{0}'".format(name))
        while True:
            data = c.fetchone()
            
            if data == None:
                break
            
            print(name + " already in database.  Unique name is required for new players.")
            return
        
        sql = "INSERT INTO Players(Name) VALUES('" + name + "')"
        c.execute(sql)
        print "Player " + name + " added successfully."
    
    
def removePlayer():
    name = raw_input('Enter player name: ')
    name = name.strip()
    
    con = lite.connect('players.db')
    
    with con:
        c = con.cursor()
        
        c.execute("SELECT * FROM Players WHERE Name == '{0}'".format(name))
        while True:
            data = c.fetchone()
            
            if data == None:
                break
            
            confirm = raw_input("Are you sure you want to remove player {0}? (yes/no) ".format(name))
                
            if confirm=="yes" or confirm=="y" or confirm=="Y":
                c.execute("DELETE FROM Players WHERE Id={0}".format(data[0]))
                print "Player " + name + " removed successfully."
            
            return
        
        print "Player " + name + " not in database."
        
