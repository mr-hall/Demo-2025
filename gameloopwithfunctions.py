import pygame

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True


def update():
    pass


def draw(screen):
    #drawing on screen
    screen.fill((255,0,0))
    pygame.display.flip()


def main():
    #my main program
    pygame.init()
    screen = pygame.display.set_mode((200,200))
    done = False
    while not done:
        done = events()
        update()
        draw(screen)

main()
