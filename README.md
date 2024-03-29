# Draughts-Game
Minimax + alpha-beta pruning
To play open the notebook and run all cells. Alternatively if you prefer cmd line pip install [runipy](https://pypi.org/project/runipy/) and run the .ipynb with that package.

This project entailed building a Draughts game using the object-oriented programming paradigm. This comprised of creating the game's back-end processes as well as its Graphical User Interface (GUI), to provide an interactive display with a board and also AI and player move-able pieces. This project was written in Python using Pygame, which provided the graphics libraries required to complete this task. The finished game is shown below.

![](https://raw.githubusercontent.com/LordLean/Draughts-Game/main/images/Introduction_image.png)

The bulk of the code is split into four main classes and also a collection of functions to handle events whilst the game is running. The four classes are Piece, GameBoard, GameManager, AI\_Player. The Piece class holds all information about a particular piece such as its colour, the shape it draws on a board, and the direction that piece will move in. GameBoard stores information of a Draught's board in instance variables such as the sum of a player's pieces and their positions on a board. This class is also responsible for determining the legal moves of any particular piece and contains the heuristic evaluation functions for determining the desirability of a game state. The GameManager was created to handle functionality relating to a player's interaction with the game. For example, its methods control the selection and move process of a piece and the passing of that information down to its GameBoard instance variable and all subsequent Pieces, for drawing them on the draughts board. Contained within this class is also the functionality relating to the scorepanel (the rectangular break-away portion seen on the right the board), such as the methods which control the changing of information internally, by way of the buttons. The AI\_Player class is used to create an opponent AI player and contains the help feature, where the object uses one of it's algorithms to provide hints for potential good moves, based off the current game state and future states. This class stores the opponent difficulty level the player selects to play against.

Valid Moves            |  Valid Moves with Opponent
:-------------------------:|:-------------------------:
![](https://raw.githubusercontent.com/LordLean/Draughts-Game/main/images/noopponent.png)  |  ![](https://raw.githubusercontent.com/LordLean/Draughts-Game/main/images/opponent.png)

![](https://raw.githubusercontent.com/LordLean/Draughts-Game/main/images/rules.png)
 
