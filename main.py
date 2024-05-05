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
    screen.fill(color)
    for event in pygame.event.get(): # event - переменная, в которой сохраняются все события
        if event.type == pygame.QUIT: # событие - выход из игры при нажатии крестика
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN: # событие - нажатие кнопки мыши
            mouse_x, mouse_y = pygame.mouse.get_pos() # коодинаты на экране нажатия мыши
            # проверка попадания клика мыши по мишени
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width) #необходимость движения мишени после клика мыши
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_image, (target_x, target_y)) # отрисовка мишени на экране
    pygame.display.update() # обновление экрана после события
pygame.quit()