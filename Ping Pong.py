# Import and initialize pygame
import pygame
pygame.init()

# Define some useful values
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)
BLUE     = (   0,   0, 255)
PI = 3.141592653

#Create the screen
size = (700, 500)
screen = pygame.display.set_mode(size)

#Change the window title
pygame.display.set_caption("Ping Pong")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
BallPos = [350,250]
BallMove = [-1, 1]
Play1Pos = [10,225]
Play1Move = 0
Play2Pos = [680, 225]
Play2Move = 0
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Play1Move = -1
            if event.key == pygame.K_s:
                Play1Move = 1
            if event.key == pygame.K_UP:
                Play2Move = -1
            if event.key == pygame.K_DOWN:
                Play2Move = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                Play1Move = 0
            if event.key == pygame.K_s:
                Play1Move = 0
            if event.key == pygame.K_UP:
                Play2Move = 0
            if event.key == pygame.K_DOWN:
                Play2Move = 0
 
    # --- Game logic should go here
    Play1Pos[1] += Play1Move * 5
    Play2Pos[1] += Play2Move * 5

    if Play1Pos[1] < 0:
        Play1Pos[1] = 0
    if Play1Pos[1] > 420:
        Play1Pos[1] = 420

    if Play2Pos[1] < 0:
        Play2Pos[1] = 0
    if Play2Pos[1] > 420:
        Play2Pos[1] = 420
    
    BallPos[0] += BallMove[0]
    BallPos[1] += BallMove[1]
    if BallPos[1] <= 0 or BallPos[1] >= 475:
        BallMove[1] = BallMove[1] * -1

    if BallPos[0] <= 20 and Play1Pos[1] <= BallPos[1] <= Play1Pos[1] + 80:
        BallMove[0] *= -1
        BallPos[0] = 20

    if BallPos[0] >= 655 and Play2Pos[1] <= BallPos[1] <= Play2Pos[1] + 80:
        BallMove[0] *= -1
        BallPos[0] = 655
        
 
    # --- Drawing code should go here
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [350,0], [350,500], 3)
    pygame.draw.ellipse(screen, WHITE, [BallPos[0], BallPos[1], 25, 25], 0)
    pygame.draw.rect(screen, WHITE, [Play1Pos[0], Play1Pos[1], 10, 80], 0)
    pygame.draw.rect(screen, WHITE, [Play2Pos[0], Play2Pos[1], 10, 80], 0)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

#Close pygame properly    
pygame.quit()
