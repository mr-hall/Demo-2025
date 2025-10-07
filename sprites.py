import pygame
import constants


class Button:
    def __init__(self, x, y, text):
        self.text = text
        self.non_hover_colour = constants.GREEN
        self.hover_colour =  constants.BLUE
        self.current_colour = self.non_hover_colour
        self.rect = pygame.Rect(x, y, 200, 50)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        self.text_image = font.render(self.text, True, (0,0,0))

    def draw(self, screen):
        pygame.draw.rect(screen, self.current_colour, self.rect)
        screen.blit(self.text_image, [self.rect.x, self.rect.y])

    def check_mouse(self):
        pos =  pygame.mouse.get_pos()
        if self.rect.collidepoint(pos[0], pos[1]):
            self.current_colour =self.hover_colour
        else:
            self.current_colour = self.non_hover_colour