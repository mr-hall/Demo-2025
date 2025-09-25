import pygame
screen = pygame.display.set_mode((600,600))
screen.fill((255,0,0))
drawing= False
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
    if drawing:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, (0, 255, 0), pos, 10)
    pygame.display.flip()

