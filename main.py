import pygame
import random

# Initialize pygame
pygame.init()

# Set block size
block_size = 10

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title
pygame.display.set_caption("Snake")

# Set the frame rate
frame_rate = pygame.time.Clock()

# Set the colors
# black = (0, 0, 0)
# white = (255, 255, 255)

white = (255, 255, 255)
black = (0, 0, 200)

# Set the snake's starting position and velocity
snake_pos = [100, 50]
snake_body = [[100, 50], [80, 50], [60, 50]]
velocity = [1, 0]
x = 3

# Set the food position
food_pos = [random.randrange(1, (window_size[0]//10)) * 10, random.randrange(1, (window_size[1]//10)) * 10]
food_spawn = True

# Set the score
score = 0

# Set the game over flag
game_over = False

# Run the game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                velocity = [0, -1*x]
            if event.key == pygame.K_DOWN:
                velocity = [0, 1*x]
            if event.key == pygame.K_LEFT:
                velocity = [-1*x, 0]
            if event.key == pygame.K_RIGHT:
                velocity = [1*x, 0]

    # Update the snake's position
    snake_pos[0] += velocity[0]
    snake_pos[1] += velocity[1]

    # Check if the snake has collided with the boundary
    if snake_pos[0] < 0 or snake_pos[0] > window_size[0]-10:
        game_over = True
    if snake_pos[1] < 0 or snake_pos[1] > window_size[1]-10:
        game_over = True

    # Update the snake's body
    snake_body.insert(0, list(snake_pos))

    # Set the collision threshold
    threshold = 10

    # Calculate the distance between the snake and the food
    distance = ((snake_pos[0] - food_pos[0]) ** 2 + (snake_pos[1] - food_pos[1]) ** 2) ** 0.5

    if distance < threshold:
        score += 1
        food_spawn = False
        # Increase the size of the snake by adding an extra block to the end
        snake_body.append([0, 0])
    else:
        snake_body.pop()

    # Spawn food
    if not food_spawn:
        food_pos = [random.randrange(1, (window_size[0] // 10)) * 10,
                    random.randrange(1, (window_size[1] // 10)) * 10]
    food_spawn = True

    # Check if the snake has collided with itself
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    # Clear the screen
    screen.fill(black)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], block_size, block_size))

    # Draw the food
    pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], block_size, block_size))

    # Display the score
    font = pygame.font.Font('freesansbold.ttf', 18)
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (5, 10))

    # Update the display
    for y in range(0, window_size[1], 2):
        # Set the color for this row
        color = (128, 128, 128)
        pygame.draw.line(screen, color, (0, y), (window_size[0], y))

    # Update the display
    pygame.display.flip()

    # Update the display
    pygame.display.update()


    # Set the frame rate
    frame_rate.tick(60)

# Quit pygame
pygame.quit()
