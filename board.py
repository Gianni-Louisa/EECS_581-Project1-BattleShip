""" 
    Program name: board.py
    Description: 
    Inputs: 
    Outputs: 
    Sources of code: 
    Authors: Connor Bennudriti, Brinley Hull, Gianni Louisa, Kyle Moore, Ben Renner
    Creation Date: 
"""
from os import system, name #sets the system name to name
from Ship import Ship
from Player import Player


columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
rows = range(1, 11)
str_rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9', "10"] # Defining the number of rows of the board for easy string operations. Team authored
header = '    ' + ' '.join(columns)

player_zero = Player(0, 'green', header, columns, rows)
player_one = Player(1, 'blue', header, columns, rows)

        

def checkHit(shot: str, enemy: Player) -> None:
    """
        checkHit(shot: str, enemy: PLayer)

        Sources: Team authored

        Checks whether a shot is a hit or miss and prints the correct message. 
        
        Returns nothing

        Parameters
            shot: a string representing the coordinate of the shot
            enemy: enemy Player object
    """
    hit = False  # Initialize hit as False to prevent issues with the loop

    for enemy_ship in enemy.ships: # Loop through all of the other player's ships
        if shot in enemy_ship.locations:  # Check if the shot hit one of the coordinates held in ship locations
            enemy_ship.hit_segments.append(shot)  # Add the section of the ship that was hit to the Ship object's list of hit segments
            print("\nHIT!\n")  # Print HIT to the console
            hit = True  # Set hit to True

            # Check if all segments of the enemy ship have been hit
            if sorted(enemy_ship.hit_segments) == sorted(enemy_ship.locations):
                enemy_ship.destroyed = True  # Set the destroyed ship's bool to true to signify that it was sunk
                print("SHIP DESTROYED!\n")  # Print that the ship was destroyed
            break  # Break the loop after a hit

    if not hit:  # If no hit was detected, print MISS
        print("\nMISS!\n")

    
def shootShip() -> str: 
    """
        shootShip(ship_locations: list)

        Sources: Team authored

        Allows a player to input their desired shot coordinates an6d returns a string representing the coordinates

        Parameters
            None
    """

    print("Choose your coordinate to shoot!") # Print a guiding statement to the user

    while True: # Loop to validate the input coordinate
        shot = input("Coordinate: ").upper() # Player inputs coordinate
        if 2 <= len(shot) <= 3 and shot[0] in columns and shot[1] in str_rows: # If the coordinate is 2 or 3 characters long and the first character is a valid column and the second character is a valid row
            if len(shot) == 3 and (shot[1] + shot[2] not in str_rows): # If the coordinate is three characters long and the two characters at the end aren't in the list of valid rows
                continue # Stay in the loop
            break # Break out of the loop

    return shot # Return the coordinate of the shot as a string

    

    
checkWinFlag = True  
def checkWin():
    """
        checkWin()

        Checks whether any player has won by destroying all the opponent's ships.
        
        Returns True if the game should continue (no one has won), 
        or False if any player has won (all opponent's ships are destroyed).
    """
    # Check if all ships of player_zero are destroyed
    if all(ship.destroyed for ship in player_zero.ships):
        print("======================================")
        print("🎉🎉🎉  CONGRATULATIONS!  🎉🎉🎉")
        print("======================================")
        print("      🚢💥 Player 1 Wins! 💥🚢")
        print("======================================")
        print("    All enemy ships have been sunk!")
        print("======================================\n")
        checkWinFlag = False
        printFinalBoards()
        return False  # The game ends when player 1 wins
    
    # Check if all ships of player_one are destroyed
    if all(ship.destroyed for ship in player_one.ships):
        print("======================================")
        print("🎉🎉🎉  CONGRATULATIONS!  🎉🎉🎉")
        print("======================================")
        print("      🚢💥 Player 0 Wins! 💥🚢")
        print("======================================")
        print("    All enemy ships have been sunk!")
        print("======================================\n")
        checkWinFlag = False
        printFinalBoards()
        return False  # The game ends when player 0 wins
    
    return True  # The game continues if neither player has won yet

#prints the final boards for each player after the game is over
def printFinalBoards():
    print("player 0's board")
    player_zero.printStrikeBoard(player_one)
    player_zero.printBoard(player_one) 
    print("\nplayer 1's board\n ")
    player_one.printStrikeBoard(player_zero)
    player_one.printBoard(player_zero)

def takeTurn(player: Player, opponent: Player) -> None:
    """
        takeTurn(player: Player)

        Sources: Team authored

        Prints the board and allows the player to take their shot
        
        Returns nothing

        Parameters
            player: a Player instance whose turn it is
    """

    enemy = player_one if player.number == 0 else player_zero # Determine the other player
    player.printStrikeBoard(enemy) # Print the player's strike board
    print() # Print just a new line for formatting
    player.printBoard(opponent) # Print the player's board
    print(f"\nPlayer {player.number}'s turn!") # Print which player's turn it is

    enemy_ship_locations = enemy.getShipLocations() # Determine the ship locations of the other player

    while True: # Perform a while loop to avoid duplicate shots
        shot = shootShip() # Allow the player to choose a coordinate to shoot
        if shot not in player.strike_attempts: # If the shot has not already been taken
            break # Break out of the loop
        print("Shot already taken.\n") # Notify player that the shot was a duplicate
    checkHit(shot, enemy) # Check to see whether the shot was a hit or miss
    player.strike_attempts.append(shot) # Add the shot taken to the player's strike attempts

    input("Press Enter and pass to the next player...\n") # Print a continue game line to the console
    clearAndPass()
    input("Next player press enter to continue")
    '''Team Authored End'''
    
#//start Chat GPT authored
def create_grid(x_size=10, y_size=10): #function that creates a grid filled with '.'
    return [['.' for _ in range(y_size)] for _ in range(x_size)] #fills the grid filled with '.'

def add_line_to_grid(grid, line_pos_x, line_pos_y, size, horizontal=True): #function that adds a line of '#' characters to the grid temporarily to represent a ship
    temp_grid = [row[:] for row in grid]  #used to make a copy of the grid
    for i in range(size): #given a certian size of ship, enter a line into the grid
        if horizontal: #if the line is horizontal, input in this fashion
            temp_grid[line_pos_x][line_pos_y + i] = '#'
        else: #the line is vertical, input in in this fashion
            temp_grid[line_pos_x + i][line_pos_y] = '#'
    return temp_grid #return the updated grid
#//stop Chat GPT authored
#//start team authored
def add_confirm_to_grid(grid, line_pos_x, line_pos_y, size, horizontal=True): #function that adds a line of '+' to the grid to represent a confirmed ship placement
    for i in range(size): #runs for the total size of the ship
        if horizontal: #if the line is horizontal, input in this fashion
            grid[line_pos_x][line_pos_y + i] = '+'
        else: #the line is vertial, input in this fashion
            grid[line_pos_x + i][line_pos_y] = '+'
    return grid #return the updated grid
#//stop team authored
#//start Chat GPT authored
def get_line_coordinates(line_pos_x, line_pos_y, size, horizontal=True): #function that returns each coord the ship is on
    coordinates = [] #initialize a list to hold the ship cords
    for i in range(size): #runs for the total ship size
        if horizontal: #if the ship is horizontal, append in this fashion
            coordinates.append((line_pos_x, line_pos_y + i))
        else: #the ship is vertical, append in this fashion
            coordinates.append((line_pos_x + i, line_pos_y))
    return coordinates #return the finished list

def check_overlap(grid, line_pos_x, line_pos_y, size, horizontal=True): #function that check if a ship is overlapping a previously confirmed ship
    for i in range(size): #check for the entire length of the ship
        if horizontal: #if the ship is horizontal, check in this fashion
            if grid[line_pos_x][line_pos_y + i] == '+': #if there is a plus in this position, return true
                return True  #overlap detected
        else: #the ship is horizontal, check in the fashion
            if grid[line_pos_x + i][line_pos_y] == '+': #if there is a plus in this position, return true
                return True  #overlap detected
    return False #there is no overlap, return false

def display_grid(grid): #prints out the current grid
    for row in grid: #prints a row
        print(" ".join(row)) #prints each element in a row
    print()

def move_line(grid, size, p1_selection): #moves and places a line of a given size on the grid
    x_size, y_size = len(grid), len(grid[0]) #gives the demensions of the grid to x_size and y_size
    horizontal = True  #start with a horizontal line

    #Puts the line in the center of the grid
    line_pos_x = x_size // 2
    line_pos_y = (y_size - size) // 2

    while True: #runs until the line is confirmed
        temp_grid = add_line_to_grid(grid, line_pos_x, line_pos_y, size, horizontal)  #creates a temproary version of the grid with the current line's position
        if p1_selection == False:#checks to see if p1 has confirmed a final board
            print("Player 1 Ship Placement Selection!")#they havent
        else:#me
            print("Player 2 Ship Placement Selection!")#they have
        display_grid(temp_grid)#print the grid

        move = input("Move (W=up, A=left, S=down, D=right, R=rotate, C=confirm, Q=quit): ").upper() #gets the users input and converts it to an uppercase char
        if move == 'W' and line_pos_x > 0:  #if input is w and the player wont go out of bounds, move the line up
            line_pos_x -= 1 #moves the line up
        elif move == 'S' and (line_pos_x < x_size - 1 if horizontal else line_pos_x + size - 1 < x_size - 1): #if input is s and the player wont go out of bounds, move the line down
            line_pos_x += 1 #moves the line down
        elif move == 'A' and line_pos_y > 0: #if input is a and the player wont go out of bounds, move the line left
            line_pos_y -= 1 #moves the line left
        elif move == 'D' and (line_pos_y < y_size - 1 if not horizontal else line_pos_y + size - 1 < y_size - 1): #if input is d and the player wont go out of bounds, move the line right
            line_pos_y += 1 #moves the line right
        elif move == 'R': #if input is r and the player wont go out of bounds, rotate the line
            mid_offset = size // 2  #rotates the line around its center

            if horizontal: #if the line is horizontal, rotate it to be vertical
                new_pos_x = line_pos_x - mid_offset
                new_pos_y = line_pos_y + mid_offset

                if new_pos_x >= 0 and new_pos_x + size <= x_size: #checks to see if the new line position is in bounds
                    line_pos_x = new_pos_x #it is, continue
                    line_pos_y = new_pos_y
                    horizontal = False
                else: #its not, error
                    print("Not enough space to rotate!")
            else: #if the line is vertical, rotate it to be horizontal
                new_pos_x = line_pos_x + mid_offset
                new_pos_y = line_pos_y - mid_offset

                if new_pos_y >= 0 and new_pos_y + size <= y_size: #checks to see if the new line position is in bounds
                    line_pos_x = new_pos_x #it is, continue
                    line_pos_y = new_pos_y
                    horizontal = True
                else: #its not, error
                    print("Not enough space to rotate!")
        elif move == 'C': #if the input is c, confirm the line
            if check_overlap(grid, line_pos_x, line_pos_y, size, horizontal): #checks to make sure this line will not overlap with any other already confirmed lnes
                print("Overlap detected! Move the line to a new position.")
            else:
                grid = add_confirm_to_grid(grid, line_pos_x, line_pos_y, size, horizontal) #add the confirmed line to the grid
                coordinates = get_line_coordinates(line_pos_x, line_pos_y, size, horizontal) #adds the line cords to coordinates
                print("Line confirmed at position!") 
                return (grid, coordinates)  #returns the updated grid and the coordinates of the line
        elif move == 'Q': #if the input is q, quit the game
            return (None, None) #return none to exit the loop
        else: #invalid input, error
            print("Invalid move! Please use W, A, S, D, R, C, or Q.")
#//stop Chat GPT authored
def translateCoordinates(ship_tuples: list) -> list:
    """
        translateCoordinates(ship_tuples)

        Sources: Team authored

        Translates ship coordinates from integer tuples to string coordinates, e.g. A3

        Returns a list of lists that contain ship locations in the form of string coordinates

        Parameters
            ship_tuples: a list of lists that contain ship location integer tuples
    """
    all_ship_coordinates = [] # Initialize a list to hold the translated ship coordinates

    for ship in ship_tuples: # For each list of ship locations inside the ships list
        ship_coordinates = [] # Initialize a list to hold individual ships translated coordinates
        for tup in ship: # For each tuple representing a coordinate inside the ship locations
            coordinate = columns[tup[1]] + str_rows[tup[0]] # Convert the integer tuple to a column and row
            ship_coordinates.append(coordinate) # Add the coordinate to the list of ship coordinates
        all_ship_coordinates.append(ship_coordinates) # Add the list of ship coordinates to the list of ships
    
    return all_ship_coordinates # Return the translated ship coordinates
#//start team authored
def goodInput(): #runs until the user inputs a valid number of ships, then returns
    valid_num_ships = ['1','2','3','4','5'] #used to check if user chose the correct number of ships
    goodIn = False #used for while loop to check for a correct input num of ships
    print("Welcome to Battle Ship!") #prints statement 
    while goodIn == False: #runs until we get a good input
        numofShips = input("Choose the number of ships you wish to play with! (1-5): ") #inputted number of ships for the game
        if numofShips in valid_num_ships: #used to break the loop if numofShips in valid_num_ships
            goodIn = True #break loop
            numofShips = int(numofShips) #turns numofShips into an int
        else:
            print("Error! Please input a valid number of ships to start.") #print error and try again
    return numofShips #returns numofShips
#//stop team authored
#//start team and ChatGPT authored
def shipPlacement(nShips): #lets each player choose where they want there ships to be placed, and returns each players confirmed coordinates
    p1_cords = [] #initializes p1's cords
    p2_cords = [] #initializes p2's cords
    p1_selection = False #sets p1_selection to false
    both_selections = False #sets both_selections to false
    
    while both_selections == False: #runs until both p1 and p2's cords are confirmed
        x_size, y_size = 10, 10 #sets to temp board's width and height
        grid = create_grid(x_size, y_size) #initializes a 10x10 grid
        confirmed_coordinates = []  #temporary list to store a players confirmed cords
        temp_numShips = nShips #creats a temporary number of ships for itiration
        while temp_numShips > 0:  # runs until there are no more ships to place
            grid, line_coordinates = move_line(grid, temp_numShips, p1_selection)  #calls move_line wich returns an updated grid and the cord's of the moved line
            if grid is None:  # checks to see if the player wishes to quit
                print("Game quit.") #print statement
                return  None# return none to quit the game
            confirmed_coordinates.append(line_coordinates)  #input the confirmed coordinates into the confirmed list
            temp_numShips -= 1  #decrement temp_numShips by 1

        #print the final board after all lines have been placed
        print("Final board:")#print statement
        display_grid(grid)#calls display_grid which will print the final grid
        if p1_selection == False:#checks to see if p1's cordinates have been fully confirmed
            for line_coords in confirmed_coordinates:# it hasnt, input coords into p1
                p1_cords.append(line_coords)#adds the cords into p1
            p1_selection = True#sets p1_selection to true
        else:#p1 has already confirmed there cords
            for line_coords in confirmed_coordinates:#input the cords into p2
                p2_cords.append(line_coords)#adds the cords into p2
            both_selections = True#sets both_selections to false to break the while loop
        input('Press Enter and pass to the next player') #move on to the next step
        clearAndPass()
        input('Press Enter to continue')
    return p1_cords, p2_cords #returns both players ship coordinates

#inspiration from geek for geeks
def clearAndPass():
    # for windows
    if name == 'nt': #name is the name of the os the game is running on
        _ = system('cls') #clear the terminal if on windows
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear') #clear the terminal if on mac or linux

#//stop team and ChatGPT authored
def main():
    
    #//start team authored
    p1_confirmed_coordinates = [] #initialize p1's cords
    p2_confirmed_coordinates = [] #initialize p2's cords
    numShips = goodInput() #calls goodInput and returns a valid number of ships for the game.
    result = shipPlacement(numShips) #calls shipPlacement and returns two lists containing each players ship coordinates or None if the player decides to quit
    if result is None: #checks if the player quit
        return #quit the game
    p1_confirmed_coordinates, p2_confirmed_coordinates = result
    
    for ship_location in translateCoordinates(p1_confirmed_coordinates): # For each ship in player zero's ship placement coordinate list
        player_zero.ships.append(Ship(ship_location)) # Add each ship to the player's ship list

    for ship_location in translateCoordinates(p2_confirmed_coordinates): # For each ship in player zero's ship placement coordinate list
        player_one.ships.append(Ship(ship_location)) # Add each ship to the player's ship list

    while(checkWinFlag):

        # Player 0 turn
        takeTurn(player_zero, player_one) # Player zero takes his turn. Team authored
        if not checkWin():  # Check if Player 0 wins
            break
        takeTurn(player_one, player_zero) # Player one takes his turn. Team authored
        if not checkWin():  # Check if Player 1 wins
            break
    #//stop team authored
    
main()

