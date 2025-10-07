import pygame
import constants
import sprites

def mainloop():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))

    #objects
    buttons = [sprites.Button(40, 40, "click here"),
               sprites.Button(180,180, "hfjh")]

    running = True
    while running:
        #check events
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                running = False
        #update
        for button in buttons:
            button.check_mouse()

        #draw
        screen.fill(constants.RED)
        for button in buttons:
            button.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    mainloop()