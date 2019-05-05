## Introduction

Hello, and welcome to your take home assignment for the Python Software Engineer @ the urge! First, thank you for your time and energy spent in this process, we fully understand that you probably have a million other things to do but this is an important screening step before moving into the advanced stages of interviews.

Your assignment is to write a program that navigates a 2-Dimensinoal board covered in coins which are picked up as you move over them, much like the game of PAC-MAN. Your program will take 4 inputs, `board_dimension`, `initial_position`, `movements`, and `walls`.

Coins are in every position of the rectangular board, except for the positions that have `walls` and the `initial_position`. If your PAC-MAN is instructed to move into a wall (on the perimeter of the board or as defined by the `walls` input) it should have no effect (the PAC-MAN stays in place).

## Program Input

Your program will take as an input the name of a text file (ie. "input.txt") residing in the same directory and that contains the following inputs:
1. `board_dimension` is defined by [X and Y coordinates](https://en.wikipedia.org/wiki/Cartesian_coordinate_system), identifying the top right corner of the room rectangle. This board is divided up in a grid based on these dimensions; a board that has dimensions X: 5 and Y: 5 has 5 columns and 5 rows, so 25 possible positions. The bottom left corner is defined by X: 0 and Y: 0.
2. `initial_position` is the initial position (in X/Y coordinates) of your PAC-MAN.
3. `movements` are instructions in [cardinal directions](https://en.wikipedia.org/wiki/Cardinal_direction) where e.g. N and E mean "go north" and "go east", respectively) 
4. `walls` are the X/Y positions of walls that are in your board, your PAC-MAN cannot move through walls. 


Example input values:

```
5 5
1 2
NNESEESWNWW
1 0
2 2
2 3
```

The above input should inform your program that you have a 5 x 5 board with walls placed at positions [[1,0],[2,2],[2,3]]. Your PAC-MAN will start at position [1,2] and will "attempt" to move the in the following sequence: N-N-E-S-E-E-S-W-N-W-W.


## Program Output


Given the inputs described above, your program should have two outputs:
1. The final location of the PAC-MAN (x,y)
2. The number of coins that have been collected across all movements

Your program output should be in the form of returned values from your pacman function and follow the format specified in the starter code files (linked below).

Example (*matching the input above*):

Python:
```
# finalXposition, finalYposition, totalCoins
return 1, 4, 7
```
Javascript:
```
// [finalXposition, finalYposition, totalCoins]
return [1, 4, 7]
```

We will be testing edge cases on your code, so if there are any problems with the inputs, execution of the instructions, or any other cases you can think of, have your pacman function return `[-1, -1, 0]`.

## Starter Code
Please use these starter code files to format your input and outputs. Don't change the name of the function, the input argument, or the order of the returned values. This is very important for us to easily test your code. Otherwise, code organization is very important to us, so you are free to add any additional files/functions/classes/etc. as you see fit.

```
"""
Write a module docstring here
"""

__author__ = "Your Name"


def pacman(input_file):
    """ Use this function to format your input/output arguments. Be sure not change the order of the output arguments. 
    Remember that code organization is very important to us, so we encourage the use of helper functions and classes as you see fit.
    
    Input:
        1. input_file (String) = contains the name of a text file you need to read that is in the same directory, includes the ".txt" extension
           (ie. "input.txt")
    Outputs:
        1. final_pos_x (int) = final x location of Pacman
        2. final_pos_y (int) = final y location of Pacman
        3. coins_collected (int) = the number of coins that have been collected by Pacman across all movements
    """

    # return final_pos_x, final_pos_y, coins_collected 
```


## Deliverable

The program:

* must run on Mac OS X, Linux (x86-64)
* can be written in any programming language, however we have a preference for Python || JavaScript. If you use another programming language, please still follow a similar format to the starter code files.
* can make use of any existing open source libraries that don't directly address the problem statement (use your best judgement).

Send us:

* The full source code, including any code written which is not part of the normal program run (scripts, tests)


## Evaluation Criteria

The point of the exercise is for us to see some of the code you wrote (and should be proud of). We believe we can learn a lot from how you approach a small challenge like this and think it can be fun to write as well!

We will especially consider:

* Code organization
* Quality, including tests
* Readability
* Actually solving the problem (edge cases included)