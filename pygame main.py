import pygame

class Button:
    def __init__(self, x, y, colour):
        self.text = "click here"
        self.colour = colour
        self.rect = pygame.Rect(x, y, 50, 50)

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)

    def check_mouse(self):
        pos =  pygame.mouse.get_pos()
        if self.rect.collidepoint(pos[0], pos[1]):
            print("mouse inside button")

def mainloop():
    screen = pygame.display.set_mode((500, 500))
    #objects
    button = Button(40, 40, (0,255,0))
    button2 = Button(180,180, (0,0,255))

    running = True
    while running:
        #check events
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                running = False
        #update
        button.check_mouse()
        #draw
        screen.fill((255,0,0))
        button.draw(screen)
        button2.draw(screen)
        pygame.display.flip()


mainloop()