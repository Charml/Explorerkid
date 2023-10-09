import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = (1200, 600)

# Create the game window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Eclipse Education Game")

# Load the PNG background image
background_image = pygame.image.load("background.png")

# Get the rect of the loaded background image
background_rect = background_image.get_rect()

# Load the "play.png" image
play_image = pygame.image.load("play.png")

# Get the rect of the loaded "play.png" image
play_rect = play_image.get_rect()

# Calculate the center position of the window
window_center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)

# Set the center of the "play.png" image to match the center of the window
play_rect.center = window_center

# Animation variables
clicked = False
scale_factor = 1.0

# Level templates
LEVEL1 = pygame.Surface(WINDOW_SIZE)  # Create an empty template for LEVEL1
LEVEL1.fill((255, 255, 255))  # Fill LEVEL1 with a white background

# Load the "background2.png" image for LEVEL1
background2_image = pygame.image.load("background2.png")
background2_image = pygame.transform.scale(background2_image, WINDOW_SIZE)
LEVEL1.blit(background2_image, (0, 0))  # Set the background image for LEVEL1

# Load and position the Sun, Earth, and Moon images
sun_image = pygame.image.load("sun.png")
earth_image = pygame.image.load("earth.png")
moon_image = pygame.image.load("moon.png")

# Calculate the new sizes (1/2 of the original sizes) for Earth and Moon
new_earth_size = (earth_image.get_width() // 2, earth_image.get_height() // 2)
new_moon_size = (moon_image.get_width() // 2, moon_image.get_height() // 2)

# Scale the Earth and Moon images to the new sizes
earth_image = pygame.transform.scale(earth_image, new_earth_size)
moon_image = pygame.transform.scale(moon_image, new_moon_size)

# Calculate the new size (slightly larger) for the Sun
new_sun_size = (int(sun_image.get_width() * 1.1), int(sun_image.get_height() * 1.1))

# Scale the Sun image to the new size
sun_image = pygame.transform.scale(sun_image, new_sun_size)

# Calculate the positions with increased spacing (x2)
sun_rect = sun_image.get_rect(center=(window_center[0] - 400, window_center[1]))
earth_rect = earth_image.get_rect(center=window_center)
moon_rect = moon_image.get_rect(center=(window_center[0] + 400, window_center[1]))

# Load font for text rendering
font = pygame.font.Font(None, 36)

current_template = "MENU"  # Start with the MENU template

# Maze template
maze_template = pygame.Surface(WINDOW_SIZE)
maze_background_image = pygame.image.load("mazebackground.png")
maze_template.blit(maze_background_image, (0, 0))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_template == "MENU" and play_rect.collidepoint(event.pos):
                clicked = True
                current_template = "LEVEL1"  # Transition to LEVEL1
                
            elif current_template == "LEVEL1" and sun_rect.collidepoint(event.pos):
                # Add your action function for the Sun button here
                # For example, you can print a message when the Sun is clicked:
              import pygame
              
              import random

              # Initialize Pygame
              pygame.init()

              # Constants
              WIDTH, HEIGHT = 400, 400
              WHITE = (255, 255, 255)
              BLACK = (0, 0, 0)
              RED = (255, 0, 0)
              GREEN = (0, 255, 0)  # Green color for exit point
              LIGHT_BLUE = (173, 216, 230)  # Light Blue color
              BLOCK_SIZE = 20

              # Create the screen
              screen = pygame.display.set_mode((WIDTH, HEIGHT))
              pygame.display.set_caption("Maze Game")

              # Define maze dimensions
              maze_width = WIDTH // BLOCK_SIZE
              maze_height = HEIGHT // BLOCK_SIZE

              # Create a maze grid (0 for open path, 1 for wall)
              maze = [[1 for _ in range(maze_width)] for _ in range(maze_height)]

              # Randomly generate maze walls using a recursive algorithm
              def generate_maze(x, y):
                  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                  random.shuffle(directions)
                  
                  for dx, dy in directions:
                      nx, ny = x + dx * 2, y + dy * 2
                      
                      if 0 <= nx < maze_width and 0 <= ny < maze_height and maze[ny][nx] == 1:
                          maze[ny][nx] = 0
                          maze[y + dy][x + dx] = 0
                          generate_maze(nx, ny)

              generate_maze(1, 1)  # Start maze generation from the top-left corner

              # Define entrance and exit points
              entrance_x, entrance_y = 0, 0
              exit_x, exit_y = maze_width - 1, maze_height - 1

              # Load the sun image and resize it to the size of the ball
              sun_image = pygame.image.load("sun.png")
              sun_image = pygame.transform.scale(sun_image, (BLOCK_SIZE, BLOCK_SIZE))

              # Initialize player's position and dragging variables
              player_x, player_y = entrance_x, entrance_y
              dragging = False
              offset_x, offset_y = 0, 0

              # Define a list of letters to place in the maze
              letters = ["E", "C", "L", "I", "P", "S", "E"]

              # Store the positions of the letters in the maze
              letter_positions = {}

              # Place letters on random open path positions
              for letter in letters:
                  placed = False
                  while not placed:
                      x, y = random.randint(0, maze_width - 1), random.randint(0, maze_height - 1)
                      if maze[y][x] == 0 and (x, y) not in letter_positions.values():
                          maze[y][x] = letter
                          letter_positions[letter] = (x, y)
                          placed = True

              # Function to check if a move is valid (within the open path)
              def is_valid_move(x, y):
                  return 0 <= x < maze_width and 0 <= y < maze_height and maze[y][x] == 0

              # Function to check if there is a wall in the path between two points
              def is_path_clear(x1, y1, x2, y2):
                  if x1 == x2:  # Vertical movement
                      min_y, max_y = min(y1, y2), max(y1, y2)
                      for y in range(min_y + 1, max_y):
                          if maze[y][x1] == 1:
                              return False
                  elif y1 == y2:  # Horizontal movement
                      min_x, max_x = min(x1, x2), max(x1, x2)
                      for x in range(min_x + 1, max_x):
                          if maze[y1][x] == 1:
                              return False
                  return True

              # Load the "eclipse.png" image for the message
              eclipse_message = pygame.image.load("eclipse.png")

              # Load the "next.png" image for the next button
              next_button = pygame.image.load("next.png")

              # Position of the "eclipse" message in the center of the maze
              eclipse_x = (WIDTH - eclipse_message.get_width()) // 2
              eclipse_y = (HEIGHT - eclipse_message.get_height()) // 2

              # Position of the "next" button
              next_x = (WIDTH - next_button.get_width()) // 2
              next_y = HEIGHT - next_button.get_height() - 20  # Position just above the bottom

              # Variable to track if the player has won
              won = False

              # Main game loop
              running = True
              while running:
                  for event in pygame.event.get():
                      if event.type == pygame.QUIT:
                          running = False
                      
                      if event.type == pygame.MOUSEBUTTONDOWN:
                          if event.button == 1:  # Left mouse button is clicked
                              if not won:
                                  mouse_x, mouse_y = pygame.mouse.get_pos()
                                  if (player_x * BLOCK_SIZE <= mouse_x <= (player_x + 1) * BLOCK_SIZE and
                                      player_y * BLOCK_SIZE <= mouse_y <= (player_y + 1) * BLOCK_SIZE):
                                      dragging = True
                                      offset_x = mouse_x - (player_x * BLOCK_SIZE)
                                      offset_y = mouse_y - (player_y * BLOCK_SIZE)
                      
                      elif event.type == pygame.MOUSEBUTTONUP:
                          if event.button == 1:
                              dragging = False
                              if (player_x, player_y) == (exit_x, exit_y):
                                  won = True

                  if dragging and not won:
                      mouse_x, mouse_y = pygame.mouse.get_pos()
                      new_player_x = (mouse_x - offset_x) // BLOCK_SIZE
                      new_player_y = (mouse_y - offset_y) // BLOCK_SIZE

                      if is_valid_move(new_player_x, new_player_y) and is_path_clear(player_x, player_y, new_player_x, new_player_y):
                          player_x, player_y = new_player_x, new_player_y

                  screen.fill(WHITE)

                  # Draw the maze
                  for row in range(maze_height):
                      for col in range(maze_width):
                          if maze[row][col] == 1:
                              pygame.draw.rect(screen, BLACK, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                          elif maze[row][col] != 0:
                              font = pygame.font.Font(None, 36)
                              text = font.render(maze[row][col], True, LIGHT_BLUE)  # Use light blue color for letters
                              screen.blit(text, (col * BLOCK_SIZE + 5, row * BLOCK_SIZE + 5))

                  # Draw entrance and exit points
                  pygame.draw.rect(screen, RED, (entrance_x * BLOCK_SIZE, entrance_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                  pygame.draw.rect(screen, GREEN, (exit_x * BLOCK_SIZE, exit_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))  # Exit point in green

                  # Draw the player (sun) image
                  screen.blit(sun_image, (player_x * BLOCK_SIZE, player_y * BLOCK_SIZE))

                  if won:
                      # Draw the "eclipse.png" message
                      screen.blit(eclipse_message, (eclipse_x, eclipse_y))
                      
                      # Draw the "next" button
                      screen.blit(next_button, (next_x, next_y))

                  pygame.display.update()

              # Quit Pygame
              pygame.quit()
              sys.exit()



    # Clear the screen
    screen.fill((0, 0, 0))

    if current_template == "MENU":
        # Draw the background image
        screen.blit(background_image, background_rect)

        # Check if the button is clicked
        if clicked:
            # Scale the button image slightly to create a simple animation effect
            scale_factor = 1.1
        else:
            scale_factor = 1.0

        # Resize and draw the "play.png" image with the animation effect
        play_scaled = pygame.transform.scale(play_image, (int(play_rect.width * scale_factor), int(play_rect.height * scale_factor)))
        play_scaled_rect = play_scaled.get_rect(center=window_center)
        screen.blit(play_scaled, play_scaled_rect)

    elif current_template == "LEVEL1":
        # Draw LEVEL1
        screen.blit(LEVEL1, (0, 0))

        # Draw the Sun, Earth, and Moon images with increased spacing (x2)
        screen.blit(sun_image, sun_rect.topleft)
        screen.blit(earth_image, earth_rect.topleft)
        screen.blit(moon_image, moon_rect.topleft)

        # Render and draw the text labels for levels in blue
        level1_label = font.render("Level 1", True, (0, 0, 255))  # Blue color
        level2_label = font.render("Level 2", True, (0, 0, 255))  # Blue color
        level3_label = font.render("Level 3", True, (0, 0, 255))  # Blue color

        # Position the text labels under the respective objects
        level1_rect = level1_label.get_rect(center=(sun_rect.centerx, sun_rect.bottom + 10))
        level2_rect = level2_label.get_rect(center=(earth_rect.centerx, earth_rect.bottom + 10))
        level3_rect = level3_label.get_rect(center=(moon_rect.centerx, moon_rect.bottom + 10))

        # Draw the text labels
        screen.blit(level1_label, level1_rect)
        screen.blit(level2_label, level2_rect)
        screen.blit(level3_label, level3_rect)

    elif current_template == "MAZE":
        # Draw the maze template
        screen.blit(maze_template, (0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
