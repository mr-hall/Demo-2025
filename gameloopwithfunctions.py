import pygame

def events():
    pass


def update():
    pass


def draw(screen):
    screen.fill((255,0,0))
    pygame.display.flip()


def main():
    screen = pygame.display.set_mode((200,200))
    while True:
        events()
        update()
        draw(screen)

main()
