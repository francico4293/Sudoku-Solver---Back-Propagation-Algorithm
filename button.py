import pygame

from settings import *


class Button(object):
    def __init__(self, x, y, width, length, text=None):
        pygame.init()
        self.width = width
        self.length = length
        self.pos = (x, y)
        self.button = pygame.Surface((width, length))
        self.rect = self.button.get_rect()
        self.rect.topleft = self.pos
        self.color = GREY
        self.highlighted_color = LIGHT_GREY
        self.font = pygame.font.SysFont("ariel", 25)
        self.text = text
        self.run = False

    def update(self, mouse):
        if self.rect.collidepoint(mouse):
            self.color = self.highlighted_color
            self.run = True
        else:
            self.color = GREY
            self.run = False

    def draw(self, window):
        self.button.fill(self.color)
        window.blit(self.button, (self.pos[0], self.pos[1]))

        text = self.font.render(self.text, False, BLACK)
        window.blit(text, (self.pos[0] + (self.width - text.get_rect()[2]) // 2,
                           self.pos[1] + (self.length - text.get_rect()[3]) // 2))

    def click(self):
        if self.run:
            return True
        else:
            return False
