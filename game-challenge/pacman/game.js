const config = {
    type: Phaser.AUTO,
    width: window.innerWidth * 0.8,
    height: window.innerHeight,
    backgroundColor: '#000000',
    parent: 'game-container',
    physics: {
        default: 'arcade',
        arcade: {
            debug: false
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    }
};

const velocity = 160;
let pacman;
let cursors;
let score = 0;
let scoreText;
let ghosts;
let ghosthome;
let ghostdoor;
let tileSize = 32;
// Direction can be up, down, left and right, but use numbers for x and y
let directions = [
    { x: 0, y: -1 }, // Up
    { x: 0, y: 1 }, // Down
    { x: -1, y: 0 }, // Left
    { x: 1, y: 0 } // Right
];

const game = new Phaser.Game(config);

function preload() {
    this.load.image('pacman', 'assets/pacman.png');
    this.load.image('dot', 'assets/dot.png');
    this.load.image('tile', 'assets/tile.png');
    this.load.tilemapTiledJSON("maze", "assets/maze.json");
    // Load ghost image
    this.load.image('ghost', 'assets/ghost.png');
}

function create() {
  const map = this.make.tilemap({ key: "maze" });
  const tileset = map.addTilesetImage("tileset", "tile");
  const walls = map.createLayer("walls", tileset, 0, 0);

  pacman = this.physics.add.sprite(50, 50, "pacman");
  // Adjust player size to 80% of the original size
  pacman.setScale(0.8);
  pacman.setCollideWorldBounds(true);

  cursors = this.input.keyboard.createCursorKeys();

  // Define ghosthome area and where is the door to the ghosthome by using the tileSize. Ghosthome is in the middle of the maze
  ghosthome = new Phaser.Geom.Rectangle(
    12 * tileSize,
    12 * tileSize,
    5 * tileSize,
    3 * tileSize
  );
  // Ghostdoor is in top of the ghosthome area in the middle of the edge of the area
  ghostdoor = new Phaser.Geom.Rectangle(
    14 * tileSize,
    11 * tileSize,
    tileSize,
    tileSize
  );

  // Create dots
  this.dots = this.physics.add.group();

  // Iterate through the walls layer and place dots where there are no walls
  walls.forEachTile((tile) => {
    if (tile.index === -1) {
      // -1 indicates no tile (empty space)
      const x = tile.getCenterX();
      const y = tile.getCenterY();
      const tileRect = new Phaser.Geom.Rectangle(x, y, tileSize, tileSize);

      // Check if the tile is within the ghosthome area
      if (!Phaser.Geom.Rectangle.Overlaps(tileRect, ghosthome)) {
        const dot = this.dots.create(x, y, "dot");
        dot.setScale(0.3);
      }
    }
  });

  // Create ghosts so that they will spawn to their ghosthome area next to eachother into two rows.
  // Create four ghosts and set its size to 10% of the original size of the ghost image.
  // Use tileSize when positioning the ghosts to make sure they are next to eachother
  ghosts = this.physics.add.group();
  for (let i = 0; i < 4; i++) {
    const x = ghosthome.x + (i % 2) * tileSize + tileSize / 2;
    const y = ghosthome.y + Math.floor(i / 2) * tileSize + tileSize / 2;
    const ghost = ghosts.create(x, y, "ghost");
    ghost.setScale(0.1);
  }

  // Add collider between the ghosts and the walls.
  // When a ghost hits a wall, change it's direction randomly in the collider function
  this.physics.add.collider(ghosts, walls, (ghost) => {
    const randomDirection = Phaser.Utils.Array.GetRandom(directions);
    ghost.setVelocity(
      randomDirection.x * velocity,
      randomDirection.y * velocity
    );
  });

  // Add collider between the ghosts and ghosts. When a ghost hits another ghost,
  // change their direction to opposite direction in the collider function
  this.physics.add.collider(ghosts, ghosts, (ghost1, ghost2) => {
    const dx = ghost1.x - ghost2.x;
    const dy = ghost1.y - ghost2.y;
    const direction = { x: Math.sign(dx), y: Math.sign(dy) };
    ghost1.setVelocity(direction.x * velocity, direction.y * velocity);
    ghost2.setVelocity(-direction.x * velocity, -direction.y * velocity);
  });

  // Add collider between pacman and ghosts. If pacman collides with a ghost, the game is over. Ghosts will
  // eat pacman and eatPacman function will be called.
  this.physics.add.overlap(pacman, ghosts, eatPacman, null, this);

  this.physics.add.overlap(pacman, this.dots, eatDot, null, this);

  scoreText = document.getElementById("score");

  // Set collision between Pacman and the maze
  walls.setCollisionByExclusion([-1]);
  this.physics.add.collider(pacman, walls);
}

function update() {
  pacman.setVelocity(0);

  if (cursors.left.isDown) {
    pacman.setVelocityX(-velocity);
  } else if (cursors.right.isDown) {
    pacman.setVelocityX(velocity);
  }

  if (cursors.up.isDown) {
    pacman.setVelocityY(-velocity);
  } else if (cursors.down.isDown) {
    pacman.setVelocityY(velocity);
  }

  // Move ghosts towards ghostdoor if they are inside the ghosthome. If they are outside the ghosthome, move them randomly
  ghosts.children.iterate((ghost) => {

    if (Phaser.Geom.Rectangle.Overlaps(ghost.getBounds(), ghosthome)) {
      this.physics.moveTo(ghost, ghostdoor.x, ghostdoor.y, velocity);
      // At 10% probability, change the direction of the ghost towads the pacman
      if (Math.random() < 0.1) {
        this.physics.moveTo(ghost, pacman.x, pacman.y, velocity);
      }
    } 
    else if (ghost.body.velocity.x === 0 && ghost.body.velocity.y === 0) {
      const randomDirection = Phaser.Utils.Array.GetRandom(directions);
      ghost.setVelocity(
        randomDirection.x * velocity,
        randomDirection.y * velocity
      );
    }
  });
}

function eatDot(pacman, dot) {
    dot.disableBody(true, true);
    score += 10;
    scoreText.innerText = score;

    // When all dots are eaten, the game is over and the player wins
    if (this.dots.countActive(true) === 0) {
        alert("You won!");
        location.reload();
    }
}

function eatPacman(pacman, ghost) {
    pacman.disableBody(true, true);
    ghost.disableBody(true, true);
    alert("Game over!");
    location.reload();
}