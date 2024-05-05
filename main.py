import pygame

pygame.init()

SCREEN_WIDTH = 800 # переменная - ширина экрана
SCREEN_HEIGHT = 600 # переменная высота экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # переменная-создание экрана (двойные скобки - кортеж)
pygame.display.set_caption('Игра Тир') # заголовок окна
icon = pygame.image.load() # переменная для иконки

running = True
while running:
    pass

pygame.quit()