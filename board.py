""" 
    Program name: board.py
    Description: 
    Inputs: 
    Outputs: 
    Sources of code: 
    Authors: Connor Bennudriti, Brinley Hull, Gianni Louisa, Kyle Moore, Ben Renner
    Creation Date: 
"""
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

    for enemy_ship in enemy.ships:
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
        return False  # The game ends when player 0 wins
    
    return True  # The game continues if neither player has won yet


def takeTurn(player: Player) -> None:
    """
        takeTurn(player: Player)

        Sources: Team authored and ?

        Prints the board and allows the player to take their shot
        
        Returns nothing

        Parameters
            player: a Player instance whose turn it is
    """

    '''This section needs comments and sources'''

    enemy = player_one if player.number == 0 else player_zero # Determine the other player
    player.printStrikeBoard(enemy)
    print()
    player.printBoard()
    print(f"\nPlayer {player.number}'s turn!")

    '''Team Authored Start'''

    enemy_ship_locations = enemy.getShipLocations() # Determine the ship locations of the other player

    while True: # Perform a while loop to avoid duplicate shots
        shot = shootShip(enemy_ship_locations) # Allow the player to choose a coordinate to shoot
        if shot not in player.strike_attempts: # If the shot has not already been taken
            break # Break out of the loop
        print("Shot already taken.\n") # Notify player that the shot was a duplicate
    checkHit(shot, enemy) # Check to see whether the shot was a hit or miss
    player.strike_attempts.append(shot) # Add the shot taken to the player's strike attempts

    input("Press Enter to continue...\n") # Print a continue game line to the console

    '''Team Authored End'''
    
#//Ben R start   
def create_grid(x_size=10, y_size=10): #chat gpt
    # Create a grid filled with '.'
    return [['.' for _ in range(y_size)] for _ in range(x_size)]

def add_line_to_grid(grid, line_pos_x, line_pos_y, size, horizontal=True): #chat gpt
    # Add a line of 'size' '#' characters to the grid temporarily
    temp_grid = [row[:] for row in grid]  # Make a copy of the grid
    for i in range(size):
        if horizontal:
            temp_grid[line_pos_x][line_pos_y + i] = '#'
        else:
            temp_grid[line_pos_x + i][line_pos_y] = '#'
    return temp_grid

def add_confirm_to_grid(grid, line_pos_x, line_pos_y, size, horizontal=True): #me
    # Add a line of 'size' '+' characters permanently to the grid
    for i in range(size):
        if horizontal:
            grid[line_pos_x][line_pos_y + i] = '+'
        else:
            grid[line_pos_x + i][line_pos_y] = '+'
    return grid

def get_line_coordinates(line_pos_x, line_pos_y, size, horizontal=True): #chat gpt
    # Generate a list of coordinates for the line
    coordinates = []
    for i in range(size):
        if horizontal:
            coordinates.append((line_pos_x, line_pos_y + i))
        else:
            coordinates.append((line_pos_x + i, line_pos_y))
    return coordinates

def check_overlap(grid, line_pos_x, line_pos_y, size, horizontal=True): #chat gpt
    # Check if the new line overlaps with any '+' on the grid
    for i in range(size):
        if horizontal:
            if grid[line_pos_x][line_pos_y + i] == '+':
                return True  # Overlap detected
        else:
            if grid[line_pos_x + i][line_pos_y] == '+':
                return True  # Overlap detected
    return False  # No overlap

def display_grid(grid): #chat gpt
    # Display the current state of the grid
    for row in grid:
        print(" ".join(row))
    print()

def move_line(grid, size, p1_selection): #chat gpt
    x_size, y_size = len(grid), len(grid[0])
    horizontal = True  # Start with a horizontal line

    # Start the line in the center of the grid
    line_pos_x = x_size // 2
    line_pos_y = (y_size - size) // 2

    while True:
        # Display the grid with the current line
        temp_grid = add_line_to_grid(grid, line_pos_x, line_pos_y, size, horizontal)  # Temporary grid with current line
        if p1_selection == False:#me
            print("Player 1 Ship Placement Selection!")#me
        else:#me
            print("Player 2 Ship Placement Selection!")#me
        display_grid(temp_grid)

        # Get user input for movement
        move = input("Move (W=up, A=left, S=down, D=right, R=rotate, C=confirm, Q=quit): ").upper()

        # Handle movement with bounds checking
        if move == 'W' and line_pos_x > 0:  # Move up
            line_pos_x -= 1
        elif move == 'S' and (line_pos_x < x_size - 1 if horizontal else line_pos_x + size - 1 < x_size - 1):  # Move down
            line_pos_x += 1
        elif move == 'A' and line_pos_y > 0:  # Move left
            line_pos_y -= 1
        elif move == 'D' and (line_pos_y < y_size - 1 if not horizontal else line_pos_y + size - 1 < y_size - 1):  # Move right
            line_pos_y += 1
        elif move == 'R':  # Rotate the line around its center
            mid_offset = size // 2  # Offset from the start to the center of the line

            if horizontal:  # Rotate to vertical
                new_pos_x = line_pos_x - mid_offset
                new_pos_y = line_pos_y + mid_offset

                # Ensure the vertical line fits in bounds
                if new_pos_x >= 0 and new_pos_x + size <= x_size:
                    line_pos_x = new_pos_x
                    line_pos_y = new_pos_y
                    horizontal = False
                else:
                    print("Not enough space to rotate!")
            else:  # Rotate to horizontal
                new_pos_x = line_pos_x + mid_offset
                new_pos_y = line_pos_y - mid_offset

                # Ensure the horizontal line fits in bounds
                if new_pos_y >= 0 and new_pos_y + size <= y_size:
                    line_pos_x = new_pos_x
                    line_pos_y = new_pos_y
                    horizontal = True
                else:
                    print("Not enough space to rotate!")
        elif move == 'C':  # Confirm and save current line
            if check_overlap(grid, line_pos_x, line_pos_y, size, horizontal):
                print("Overlap detected! Move the line to a new position.")
            else:
                grid = add_confirm_to_grid(grid, line_pos_x, line_pos_y, size, horizontal)
                coordinates = get_line_coordinates(line_pos_x, line_pos_y, size, horizontal)
                print("Line confirmed at position!")
                return (grid, coordinates)  # Return the updated grid and the coordinates of the line
        elif move == 'Q':  # Quit the game
            return (None, None)  # Return None to exit the loop
        else:
            print("Invalid move! Please use W, A, S, D, R, C, or Q.")

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
#//start of team and ChatGPT authored
def shipPlacement(nShips):
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
        input('Press anything to continue: ') #move on to the next step
    return p1_cords, p2_cords #returns both players ship coordinates
#//stop of team and ChatGPT authored
def main():
    
    #//start of team authored
    p1_confirmed_coordinates = [] #initialize p1's cords
    p2_confirmed_coordinates = [] #initialize p2's cords
    numShips = goodInput() #calls goodInput and returns a valid number of ships for the game.
    result = shipPlacement(numShips) #calls shipPlacement and returns two lists containing each players ship coordinates or None if the player decides to quit
    if result is None: #checks if the player quit
        return #quit the game
    p1_confirmed_coordinates, p2_confirmed_coordinates = result
    #//stop of team authored
    
    for ship_location in translateCoordinates(p1_confirmed_coordinates): # For each ship in player zero's ship placement coordinate list
        player_zero.ships.append(Ship(ship_location)) # Add each ship to the player's ship list

    for ship_location in translateCoordinates(p2_confirmed_coordinates): # For each ship in player zero's ship placement coordinate list
        player_one.ships.append(Ship(ship_location)) # Add each ship to the player's ship list

    '''Team Authored End'''

    #//Ben R end
          
    while(checkWinFlag):

        # Player 0 turn
        takeTurn(player_zero) # Player zero takes his turn. Team authored
        if not checkWin():  # Check if Player 0 wins
            break
        takeTurn(player_one) # Player one takes his turn. Team authored
        if not checkWin():  # Check if Player 1 wins
            break

    
main()

