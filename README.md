# Tic_Tac_Toe_Game
Python program for simple Tic Tac Toe Game

Instructions:

* 2 players should be able to play the game (at the same computer)

* The board should be printed out everytime a player makes a move

*You should be able to accept input of the player position and then place a symbol on the board.

* Here we will use the 'numpad' to match numbers to the grid on a tic tac toe board.
          Like 
          
          | 7 || 8 || 9 |
          | 4 || 5 || 6 |
          | 1 || 2 || 3 |
 
   This program will ask user .."Hey where would you like to  place your X or O
   And if the user provided the number 1 then we will print an X over there at location 1
          | - || - || - |
          | - || - || - |
          | X || - || - |
          
 then next user will input the number 8 and then a O is printed at location 8.
          | - || O || - |
          | - || - || - |
          | X || - || - |
          
 Alternate between X and O
 
 
 ------------Game Interface----------
 
 Welcome to Tic Tac Toe!
 
 Player 1: Do you want to be X or 0?
 X                  # User 1 input is X
 
 Player 1 will go first.
 
 Are you ready to play? Enter Yes or No.
 Yes
 #Player 1 game starts
 Choose your next position:(1-9)
    |     |                                          |     |
    |     |                                        7 |  8  |  9
    |     |                                          |     |
---------------                                  ---------------
    |     |                                          |     |
    |     |                                        4 |  5  | 6
    |     |                                          |     |
----------------                                  ----------------
    |     |                                          |     |
    |     |                                        1 |   2 |  3
    |     |                                          |     |
    
   Figure 01:                                    Figure 02:
   This is how it looks on the game              This is the actual representation
   
 
 In figure 01:
 
 In the middle of each ,there will be empty curly braces which are not visible now(because they are empty) and those curly braces corresponds to the index positions of some list
 
 Now, Player 01 chooses the position as 01
  Choose your next position:(1-9) 
  1
  
    |     |                                         
    |     |                                       
    |     |                                          
---------------                                  
    |     |                                         
    |     |                                       
    |     |                                         
----------------                                 
    |     |                                         
  X |     |                                       
    |     |    
  
  #Now the next player has to choose 
  
    Choose your next position:(1-9)
    8
    
    
    And like this the game goes on .......
    
    When obtain 3 X or 3 O in a row 
    like     X  |  X  |  X      
    
   Do you want to play again ? Enter Yes or No:
   NO

    
   Congratulations ! You have won the game!
   Do you want to play again ? Enter Yes or No: No
   
    
   
  
 
