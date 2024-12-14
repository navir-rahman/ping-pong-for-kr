import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Load images
player_bar = pygame.image.load("player_bar.png")
computer_bar = pygame.image.load("computer_bar.png")
ball_image = pygame.image.load("ball.png")

# Resize the images if needed
player_bar = pygame.transform.scale(player_bar, (100, 20))
computer_bar = pygame.transform.scale(computer_bar, (100, 20))
ball_image = pygame.transform.scale(ball_image, (20, 20))

# Initial positions
player_x = WIDTH // 2 - player_bar.get_width() // 2
player_y = HEIGHT - 40

computer_x = WIDTH // 2 - computer_bar.get_width() // 2
computer_y = 20

ball_x = WIDTH // 2 - ball_image.get_width() // 2
ball_y = HEIGHT // 2 - ball_image.get_height() // 2
ball_dx = random.choice([-5, 5])  # Ball speed in x-direction
ball_dy = random.choice([-5, 5])  # Ball speed in y-direction

# Score tracking
player_score = 0
computer_score = 0

# Font for displaying score and winner message
font = pygame.font.SysFont("Arial", 30)

# Clock to control the game frame rate
clock = pygame.time.Clock()
running = True

while running:
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed by the player
    keys = pygame.key.get_pressed()

    # Player movement (left and right)
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 10
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_bar.get_width():
        player_x += 10

    # Computer AI movement (simple AI to follow the ball)
    if computer_x + computer_bar.get_width() // 2 < ball_x + ball_image.get_width() // 2:
        computer_x += 5
    if computer_x + computer_bar.get_width() // 2 > ball_x + ball_image.get_width() // 2:
        computer_x -= 5

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

    # Ball collision with top/bottom
    if ball_y <= 0:
        ball_dy *= -1  # Reverse the direction
        # Computer scores a point
        computer_score += 1
        ball_x = WIDTH // 2 - ball_image.get_width() // 2
        ball_y = HEIGHT // 2 - ball_image.get_height() // 2
        ball_dx = random.choice([-5, 5])
        ball_dy = random.choice([-5, 5])
    elif ball_y >= HEIGHT - ball_image.get_height():
        ball_dy *= -1  # Reverse the direction
        # Player scores a point
        player_score += 1
        ball_x = WIDTH // 2 - ball_image.get_width() // 2
        ball_y = HEIGHT // 2 - ball_image.get_height() // 2
        ball_dx = random.choice([-5, 5])
        ball_dy = random.choice([-5, 5])

    # Ball collision with player and computer paddles
    if (ball_y + ball_image.get_height() >= player_y and
        player_x <= ball_x + ball_image.get_width() // 2 <= player_x + player_bar.get_width()):
        ball_dy *= -1  # Reverse the ball's y direction

    if (ball_y <= computer_y + computer_bar.get_height() and
        computer_x <= ball_x + ball_image.get_width() // 2 <= computer_x + computer_bar.get_width()):
        ball_dy *= -1  # Reverse the ball's y direction

    # Ball collision with left and right walls
    if ball_x <= 0 or ball_x >= WIDTH - ball_image.get_width():
        ball_dx *= -1  # Reverse the direction

    # Draw paddles and ball
    screen.blit(player_bar, (player_x, player_y))
    screen.blit(computer_bar, (computer_x, computer_y))
    screen.blit(ball_image, (ball_x, ball_y))

    # Display the score
    player_score_text = font.render(f"Player: {player_score}", True, (255, 255, 255))
    computer_score_text = font.render(f"Computer: {computer_score}", True, (255, 255, 255))
    screen.blit(player_score_text, (WIDTH // 4, 10))
    screen.blit(computer_score_text, (WIDTH // 2 + WIDTH // 4, 10))

    # Check if either player or computer has won (e.g., 10 points)
    if player_score >= 10:
        winner_text = font.render("Player Wins!", True, (0, 255, 0))
        screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(2000)  # Wait for 2 seconds before quitting
        running = False
    elif computer_score >= 10:
        winner_text = font.render("Computer Wins!", True, (255, 0, 0))
        screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        pygame.time.delay(2000)  # Wait for 2 seconds before quitting
        running = False

    pygame.display.update()  # Update the display

    # Set the frames per second (FPS)
    clock.tick(60)

# Quit Pygame
pygame.quit()
