import pygame
import constants
import random

class Circle:
    def __init__(self):
        self.radius = 20
        self.x = random.randint(0,500)
        self. y = random.randint(0,500)

    def draw(self, screen):
        pygame.draw.circle(screen, constants.BLUE, (self.x, self.y), self.radius)

def mainloop():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))

    #objects
    circles = []
    for i in range(10):
        circles.append(Circle())
    running = True
    while running:
        #check events
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                running = False
        #update

        #draw
        screen.fill(constants.RED)
        for circle in circles:
            circle.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    mainloop()