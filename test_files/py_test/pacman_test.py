"""
Write a module docstring here
"""

__author__ = "Your Name"

class Game:
    def __init__(self, input_file):
        self.input_file = input_file
        self.dimension = [],
        self.pos_x = 0,
        self.pos_y = 0,
        self.walls = [],
        self.moves = '',
        self.coins_collected = int(0),
        self.memory = []

    def get_data(self):
        "Retrieve The Data From The Input File"
        # reading data from .txt file
        with open(f"{self.input_file}", "r") as file:
            data = file.readlines()

        #Sharing Data
        self.dimension = data[0].split() 
        initial_position = data[1].split()
        self.moves = data[2].split()[0]
        self.walls = [i.split() for i in data[3::]]
        
        #Change the postion order
        self.pos_x = int(initial_position[0])
        self.pos_y = int(initial_position[1])

        self.coins_collected = 0
        self.memory.append([self.pos_x, self.pos_y])
        return len(self.moves)

    def memory_check(self):
        "Memory check for existing positions to prevent coin addition"

        if [self.pos_x, self.pos_y] in self.memory:
            self.coins_collected -= 1
        else:
            self.memory.append([self.pos_x, self.pos_y])

    def wall_check(self):
        "Wall/Grid cordinates check so point does not go outside the grid or run into a wall"

        for wall in self.walls:
            #Grid Check
            if int(self.pos_x) >= (int(self.dimension[0]) - 1) or int(self.pos_y) >= (int(self.dimension[1]) - 1):
                return True

            elif int(self.pos_x) <= 0 or int(self.pos_y) <= 0:
                return True
                
            # Wall check
            elif [self.pos_x, self.pos_y] == wall:
                return True

            else:
                return False

    def move_north(self):
        "Move North"
        self.pos_y += 1
        # Wall Check
        result = self.wall_check()

        if result == False:
            self.coins_collected += 1
            self.walls.append([self.pos_x, self.pos_y])
            
        else:
            self.pos_y -= 1
        
    def move_south(self):
        "Move South"
        self.pos_y -= 1
        # Wall Check
        result = self.wall_check()
    
        if result == False:
            self.coins_collected += 1
            self.walls.append([self.pos_x, self.pos_y])
            
        else:
            self.pos_y += 1

    def move_west(self):
        "Move West"
        self.pos_x -= 1
        # Wall Check
        result = self.wall_check()
    
        if result == False:
            self.coins_collected += 1
            self.walls.append([self.pos_x, self.pos_y])
            
        else:
            self.pos_x += 1

    def move_east(self):
        "Move East"
        self.pos_x += 1
        # Wall Check
        result = self.wall_check()
    
        if result == False:
            self.coins_collected += 1
            self.walls.append([self.pos_x, self.pos_y])
            
        else:
            self.pos_x -= 1

    def make_move(self, i):
        "Make The Move Increment Action"
        if self.moves[i] == "N":
            self.move_north()
        
        elif self.moves[i] == "S":
            self.move_south()

        elif self.moves[i] == "E":
            self.move_east()

        elif self.moves[i] == "W":
            self.move_west()
        else:
            pass


    def get_results(self):
        "Checks for memory count corresponding to coins collected to remove extra added cause of non-parallel indexing"
        return self.pos_x, self.pos_y, self.coins_collected






def pacman(input_file):
    """ Use this function to format your input/output arguments. Be sure not to change the order of the output arguments. 
    Remember that code organization is very important to us, so we encourage the use of helper fuctions and classes as you see fit.
    
    Input:
        1. input_file (String) = contains the name of a text file you need to read that is in the same directory, includes the ".txt" extension
           (ie. "input.txt")
    Outputs:
        1. final_pos_x (int) = final x location of Pacman
        2. final_pos_y (int) = final y location of Pacman
        3. coins_collected (int) = the number of coins that have been collected by Pacman across all movements
    """
    
    try:
        pacman = Game(input_file)
        
        # This return the index number of moves
        count = pacman.get_data()

        for i in range(count):
            pacman.make_move(i)

            pacman.memory_check()
        
        if pacman.coins_collected <= 0:
            return (-1, -1, 0)


        final_pos_x, final_pos_y, coins_collected = pacman.get_results()
        return (final_pos_x, final_pos_y, coins_collected)

    # Handling any form of errors
    except Exception as e:
        return (-1, -1, 0)


