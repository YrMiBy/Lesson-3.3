import pygame
import random

pygame.init()

# Создание экрана
SCREEN_WIDTH = 800 # переменная - ширина экрана
SCREEN_HEIGHT = 600 # переменная высота экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # переменная-создание экрана (двойные скобки - кортеж)
pygame.display.set_caption('Игра Тир') # заголовок окна
icon = pygame.image.load('img/icons.png') # переменная для иконки в созданной директории img
pygame.display.set_icon(icon) # установка иконки

# Создание мишени
target_image = pygame.image.load('img/target.png') # переменная определяет мишень 
target_width = 80 # ширина мишени
target_height = 80 # высота мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)# перемещение мишени по ширине экрана
target_y = random.randint(0, SCREEN_HEIGHT - target_height)# перемещение мишени по высоте экрана
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))# изменеие цвета экрана

running = True
while running:
    pass

pygame.quit()