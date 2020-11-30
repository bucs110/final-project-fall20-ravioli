:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Ravioli Simulator
## CS 110 Final Project
### Fall, 2020
### [Assignment Description](https://drive.google.com/open?id=1HLIk-539N9KiAAG1224NWpFyEl4RsPVBwtBZ9KbjicE)

https://github.com/bucs110/final-project-fall20-ravioli.git

https://docs.google.com/presentation/d/1GAui5JCBEnaJ_AB3h4D5tnfH_YqFALjKpIkGhKZkrio/edit#slide=id.g33aee8826e_9_16

### Team: Ravioli
#### Emily Greene, Roman Raguso, Josef Schindler

***

## Project Description
Our project is an RPG with a combat and economy system. There are waves of enemies for the character to fight, dealing out melee and range attack. As time passes, the enemies become progressively harder to kill, and the character accumulates money in their bank account. The character can also deposit and withdraw money from the bank to buy different items from merchants. All of the features combine to create an entertaining story for the player.
***    

## User Interface Design
 *![gui design](assets/gui_design_screen.jpg)
 This is the screen the player sees when they begin the game.
*![gui design](assets/gui_design_main.jpg)
This the the screen the player sees while playing the game.
 *![gui design](assets/gui_design_lose.jpg)
 This is the screen the player sees if they lose the game.
 *![gui design](assets/gui_design_victory.jpg)
 This is the screen the player sees if they win the game.

* << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design
* Non-Standard libraries
    * Random
	    * https://docs.python.org/3/library/random.html
	    * The random module is a psuedo-random number generator.
	* Pygame
		* https://www.pygame.org/docs/
		* Pygame is a framework library that handles the view of a program and is designed for writing video games.
	* os
		* https://docs.python.org/3/library/os.html
		* os allows the usage of operating system dependent functionality.

		

* Class Interface Design
        * ![class diagram](assets/class_diagram.jpg) 
* Classes
    * Character- This is the player that the user controls. It can move around, get hit by an enemy and lose health, and get knocked back after being hit.
    * Enemy- This creates the enemies that the character fights. It can move within the boundaries, change direction, get hit and lose health, and get knocked back after being hit.
    * Melee- This creates the sword weapon which deals melee damage to the enemies. (not currently in use- left in for future repurpose)
    * Button- This creates a button that can be clicked to lead to other information to the player.
    * Merchant- This is a seller that the character can buy goods from.
    * Controller- This initializes the screen and creates sprite groups for all of the sprites and just the enemies. It establishes the key movements of "w," "a," "s," "d," and the spacebar, which signals for the sword to strike. This allows the enemies to get hit if the rectangles of the sword and the enemy overlap, and it allows the enemies to die. Also, it allows for the detection of the player being hit by the enemies.  If the player is hit, it loses health, and either stays alive and is knocked back or dies.

***

## Tasks and Responsibilities
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Emily Greene

<< Worked as integration specialist by... >>

### Front End Specialist - Roman Raguso

<< Front-end lead conducted significant research on... >>

### Back End Specialist - Josef Schindler

<< The back end specialist... >>

## Testing
* ****I tested the code at least once a week; however, whenever I saw that new code had been pushed, I pulled it and ran it to ensure it was working properly. I regularly went through the code to make sure I understood it all, that it was all dry, and that it made sense and worked together. As a team, we went through the code twice. I used an exploratory testing method to ensure optimization because it was the most time efficient and, in my opinion, the most true to life way of testing out our game. I mostly played the game to the extent that it was made at the moment and went through each action that was made then. I knew how the game was supposed to be played and the objective of it, so I would go through every action that the character could do, such as moving up/down/left/right, swinging its sword in thin air, swinging its sword to hit an enemy, killing enemies, and dying. I also went through every sound that could be made in the game while it was running to ensure that the sounds came across correctly.****

* Your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Press "W" key  | Knight moves up and stays within the screen  |          |
|  2  | Press "A" key  | Knight moves left and stays within screen |                 |
|  3  | Press "S" key  | Knight moves down and stays within the screen  |          |
|  4  | Press "D" key  | Knight moves right and stays within screen |                 |
|  5  | Press spacebar  | Knight swings sword and slashing sound is made  |          |
|  6  | Press "W" and "A" keys  | Knight moves to the upper left diagonal and stays within screen |                 |
|  7  | Press "W" and "D" keys  | Knight moves to the upper right diagonal and stays within the screen  |          |
|  8  | Press "S" and "A" keys  | Knight moves to the lower left diagonal and stays within screen |                 |
|  9  | Press "S" and "D" keys  | Knight moves to the lower right diagonal and stays within the screen  |          |
|  10  | Move to within BLANK pixels of enemy and press spacebar  | The sword swings, a slashing sound is made, the enemy makes a hissing noise, the enemy bounces back, and the enemy loses health. |                 |
|  11  | Enemy comes within BLANK pixels of the knight and spacebar is not pressed  | Knight bounces back, a hitting noise is made, a splash of purple appears, and the health count decreases by 10.  |          |
|  12  | Overlap knight with lever on screen with merchants and press "E" key  | The lever handle flips, makes a BLANK NOISE, and another round of gameplay with a new wave begins.  |                 |
|  13  | Move knight to within BLANK pixels of yellow wizard on merchant screen  | Button for exchange of money for BLANK power up appears  |          |
|  14  | Move knight to within BLANK pixels of Red wizard on merchant screen  | Button for exchange of money for an increase in health appears |                 |
|  15  | Move knight to within BLANK pixels of blue wizard on merchant screen  | Button for exchange of money for speed appears  |          |
|  16  | Click on button from yellow knight  | Money count decreases by 250 EXPAND |                 |
|  17  | Click on button from red knight  | Money count decreases by 10 and health count increases by 10.  |          |
|  18  | Click on button from red knight  | Money count decreases by 50 and knight is BLANK times faster in the next round of gameplay. EXPAND BC CHANGING AMOUNTS OF MONEY |                 |
|  3  | Press "S" key  | Knight moves down and stays within the screen  |          |
|  2  | Press "D" key  | Knight moves right and stays within screen |                 |
