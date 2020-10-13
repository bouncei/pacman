This is a Pac-Man program that has Coins in every position of the rectangular board except for the positions that have `walls` and the `initial_position`. If Pac-Man is instructed to move into a wall (on the perimeter of the board or as defined by the `walls` input) it should have no effect (Pac-Man stays in place).

# Program Input
Your program will take as input the name of a text file (ie. "input.txt") residing in the same directory as your code, and that contains the following inputs:

1. `board_dimension` is given on the first line. It is defined by [X and Y coordinates](https://en.wikipedia.org/wiki/Cartesian_coordinate_system), identifying the top right corner of the room rectangle - that is to say, (0,0) is in the bottom left corner, and (X,Y) is in the top right corner. This board is divided up in a grid based on these dimensions; a board that has dimensions `X=5` and `Y=5` has 5 columns and 5 rows for 25 possible positions.
2. `initial_position` is given on the second line. It is the initial position of Pac-Man in (x,y) coordinates.
3. `movements` are given on the third line. They are instructions in [cardinal directions](https://en.wikipedia.org/wiki/Cardinal_direction) where e.g. N and E mean "go north" and "go east", respectively. The board is oriented facing north; thus, moving north from (0,0) lands Pac-Man at (0,1).
4. `walls` are given on the remaining lines. They are the positions of walls on the board in (x,y) coordinates. Pac-Man cannot move through walls. Note: Many modern text editors automatically add in a newline character to the end of the file. These trailing newline characters should be ignored.

For an input file to be valid, it must contain a `board_dimension`, an `initial_position` and at least one movement in `movements`.

Example input values:
```
5 5
1 2
NNESEESWNWW
1 0
2 2
2 3
```

The above input should inform your program that you have a 5 x 5 board with walls placed at positions `[(1,0),(2,2),(2,3)]`. Pac-Man will start at position `(1,2)` and will "attempt" to move in the following sequence: `N-N-E-S-E-E-S-W-N-W-W`.

# Program Output
Given the inputs described above, your program should have two outputs:

- Pac-Man's final location in (x,y)
- The number of coins that have been collected across all movements

Your program output should be in the form of returned values from your `pacman` function, and follow the format specified in the starter code files.

Example (matching the input above):  

Python:
```py
# finalXposition, finalYposition, totalCoins
return (1, 4, 7)
```




