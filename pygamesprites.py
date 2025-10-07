import pygame
import constants
import random

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemyShip.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,500)
        self.rect.y =random.randint(0,500)

def mainloop():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    player = Player()
    enemies = pygame.sprite.Group()
    for i in range(5):
        enemies.add(Enemy())
    running = True
    while running:
        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.update()
        pygame.sprite.spritecollide(player, enemies, True)
         # draw
        screen.fill(constants.RED)
        screen.blit(player.image, player.rect)
        enemies.draw(screen)
        pygame.display.flip()

mainloop()