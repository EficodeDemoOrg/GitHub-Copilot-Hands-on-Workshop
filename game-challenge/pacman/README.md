# Pacman - eat all you can

The model solution and the prompts are just one solution. The given prompts are not the only way to solve the problem and as Copilot is just an AI, the same prompts does not work everytime and to everyone. The prompts uses mainly the chat and you can also use the inline Copilot to get different solutions. 

## How to get started

### Thinking piece by piece

- Tell Copilot where you would like to run your Pacman game. If you already know, tell also the programming language you would like to use or you can ask recommendations from Copilot.
- You can also ask for the game framework you would like to use. Copilot can suggest you for example Phaser, React, or plain JavaScript.
- Then start to think the problem piece by piece:
  - How to create the game area and the maze?
  - How to create the dots for the Pacman to eat?
  - How to create the Pacman and the ghosts?
  - How to move the Pacman and the ghosts?
  - How to detect the collision between the Pacman and the ghosts?
  - How to detect the collision between the ghosts and the walls?
  - How to detect the collision between the ghosts and the other ghosts?
  - How to detect the winning condition?
  - How to detect the game over condition?

### Tips

- You can use the image assets from the assets folder for ghosts, pacman, tiles, and dots
- When getting bigger pieces of code at once, you more probably need to fix the code by hand
- When you get a piece of code that is not working, you can ask Copilot to fix it easier by giving a hint what is wrong

## Prompting the Pacman game

### Demo 1 (about 25 minutes)

1. Chat: I want to make a Pacman game that is running in a browser. Which programming language you suggest?
2. Chat: Is React or plain JavaScript better for this purpose?

3. Chat: Use Javascript and Phaser to create a Pacman game. The playing area will be on the left side of the screen and it will take 80% of the width of the screen. The right side of the screen will be 20% of the width of the screen and there will be the points the player has received. The whole background of the screen will be black. The playing maze is a square and will be on the playing area side. The player can move Pacman in the maze. The maze has small dot's that the Pacman can eat and receive points. Locations of the walls are defined in maze.json file. All images are in assets folder. Set velocity value into a variable.

- Note! Check that the filenames of the images are correct!
- Fix also the layer names if needed, open from browser the console to see the errors

4. Chat: How can I create the maze where the Pacman is moving?

5. Chat: The dots should be placed to each tile where there is no wall in it. Add dots by going through the walls layer
   and place a dot on each tile where there is no walls

6. Chat: How can I now run the app?

```
npm install -g http-server
cd /path/to/your/project
http-server
```

7. Chat: The dots are now quite big, can you make the dots smaller? Dots could be 30% of the size it is now

8. Pacman seems to be too big, add comment after Pacman creation: "Adjust player size to 80% of the original size"

9. Inline Copilot is demonstrated more in the next phase of the demo, but show simple example. Write a comment to preload() "Load ghost image" and after enter, accept the code with TAB


### Demo 2 (about 20 minutes)

1. Add variables ghosts, ghosthome, ghostdoor, directions, and tileSize=32 by hand
``` 
// Add moving directions to an array. Direction can be up, down, left and right, but use numbers for x and y

let directions = [
    { x: 0, y: -1 }, // Up
    { x: 0, y: 1 }, // Down
    { x: -1, y: 0 }, // Left
    { x: 1, y: 0 } // Right
];
```

2. In create()-function add values to the variables, add comments 
"Define ghosthome area and where is the door to the ghosthome by using the tileSize. Ghosthome is in the middle of the maze"
"Ghostdoor is in top of the ghosthome area in the middle of the edge of the area"
- Check that the values are correct:
- ghosthome = new Phaser.Geom.Rectangle(12 * tileSize, 12 * tileSize, 5 * tileSize, 3 * tileSize);
- ghostdoor = new Phaser.Geom.Rectangle(14 * tileSize, 11 * tileSize, 1 * tileSize, 1 * tileSize);

3. Chat: Do not add dots to ghosthome area
- May not work at one shot, paint the code and tell in the chat that this is not working
- May still need to be fixed by hand

4. Continue in create()-function by adding a comment: "Create ghosts so that they will spawn to their ghosthome area next to eachother into two rows. Create four ghosts and set its size to 10% of the original size of the ghost image. Use tileSize when positioning the ghosts to make sure they are next to eachother"

5. Then add comment "Add collider between ghosts and pacman. Ghosts will eat the player if they collide and eatPacman will be called"

6. Start writing function **eatPacman** in the end of the file and implement the eatPacman-function
- Add comment "Reset the position of player" should produce code: pacman.disableBody(true, true);
- There should be also a code for reseting the score
- Chat: "Add a notification to the user that the game is over and ask to play again.
  Create first the notification and then add a button into the notification to play again.
  There is a box around the notification and the button. Button's bachground is black and text is white.
  Place the notification box to the middle of the screen"
- Chat: "The styling should be in styles.css file"
- Add comment to button click handler: "Restart the game". Code added should be game.scene.start("pacman"); and also a key field with value "pacman" should be added to scene variable.

7. **Colliders**: Go to the end of the create()-function and add a comment "Add collider between the ghosts and the walls. When a ghost hits a wall, change it's direction randomly in the collider function". Move walls variable out from the function if needed.

8. Add a comment in create()-function: "Add collider between the ghosts and ghosts. When a ghost hits another ghost, change their direction to opposite direction in the collider function"

9. **Ghosts moving**: Add comment to end of update() function: "Move ghosts towards ghostdoor if they are inside the ghosthome. If they are outside the ghosthome, move them randomly"

10. The ghosts will block the ghosthome door. Add comment to the ghosts moving code inside the condition that the ghost is in the ghosthome: "At 10% probability, change the direction of the ghost towads the pacman"

11. **Winning the game**: Add to eatDot a comment: "When all dots are eaten, the game is over and the player wins"


### More you could also try

1. Chat: How can I write test cases to this application?
2. Chat: Could you refactor the code so that all ghosts related code is in separate file?
3. Chat: Explain the code 
4. Chat: Create Dockerfile
5. Chat: How to run the app in container
6. Chat: Create documentation to a README.md-file
7. Chat: Is my code secure?
8. Chat: Create draw.io diagram of the game