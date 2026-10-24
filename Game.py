#Import and initialize pygame
import pygame
import random

#Some useful values
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)
BLUE     = (   0,   0, 255)
PI = 3.141592653

class Pipes(object):
    def __init__(self, x=700):
        self.x = x
        self.y = random.randint(50,250)
    def draw(self):
        pygame.draw.rect(screen, GREEN, [self.x, -1, 50, self.y], 0)
        pygame.draw.rect(screen, GREEN, [self.x, self.y + 200, 50, 500], 0)
    def move(self):
        self.x = self.x - 2
        if self.x <= -50:
            self.__init__()
    def collide(self, other):
        coll = True
        if self.x > other.x + 50 or self.x + 50 < other.x:
            coll = False
        if self.y < other.y and self.y + 200 > other.y + 50:
            coll = False
        return coll
        

class Flappy(object):
    def __init__(self):
        self.x = 50
        self.y = 200
        self.fall = 0
    def draw(self):
        pygame.draw.rect(screen, RED, [self.x, self.y, 50, 50], 0)
    def move(self):
        self.y = self.y + self.fall
        self.fall = self.fall + 1
        if self.fall > 10:
            self.fall = 10
    def flap(self):
        self.fall = -10

#Set the screen up
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

pipes = []
pipes.append(Pipes(700))
pipes.append(Pipes(950))
pipes.append(Pipes(1200))

flappy = Flappy()


# -------- Main Program Loop -----------
playing = True
while playing:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flappy.flap()
 
    # Game logic
    for pipe in pipes:
        pipe.move()
        if pipe.collide(flappy):
            playing = False
    flappy.move()
    if flappy.y < 0 or flappy.y > 450:
        playing = False
    
    # Draw the frame
    screen.fill(BLACK)
    for pipe in pipes:
         pipe.draw()
    flappy.draw()
    # 
    # Flip the screen and limit the frame rate
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

