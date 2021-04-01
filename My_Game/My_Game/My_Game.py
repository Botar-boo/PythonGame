import pygame
import random

# Основные настройки
WIDTH = 360
HEIGHT = 480
FPS = 60
currentFPS = 0
score = 0
whiteSpace = 17
buttonWidth = 99
worker = [0, 0, 0]

# Задаем цвета
WHITE = (255, 255, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
buttonImage = pygame.image.load('Button.png')
background = pygame.image.load('Background.jpg')
    
# Объекты : Кнопки и Клик
class Button(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = buttonImage
        self.rect = self.image.get_rect()
        self.rect.center = pos

class Touch(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 1, 1)
        self.rect.center = (x, y)

# Цикл игры
running = True
all_sprites = pygame.sprite.Group()
button1 = Button((buttonWidth / 2 + 14, 400))
button2 = Button((3 * buttonWidth / 2 + 14 + whiteSpace, 400))
button3 = Button((5 * buttonWidth / 2 + 14 + 2 * whiteSpace, 400))
sprites = [button1, button2, button3]
all_sprites.add(sprites)
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    currentFPS += 1
    # Ввод процесса (события)
    if currentFPS % 60 == 0:
        score += worker[0] * 1
        score += worker[1] * 3
        score += worker[2] * 9
    for event in pygame.event.get():
        if score >= 100000 or event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score += 1
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            Click = Touch(pos[0], pos[1])
            if score >= 100  and pygame.sprite.collide_rect(sprites[0], Click):
                worker[0] += 1
                score -= 100
            if score >= 200  and pygame.sprite.collide_rect(sprites[1], Click):
                worker[1]  += 1
                score -= 200
            if score >= 500  and pygame.sprite.collide_rect(sprites[2], Click):
                worker[2]  += 1
                score -= 500

    # Рендеринг
    f1 = pygame.font.Font(None, 36)
    f2 = pygame.font.Font(None, 15)
    text1 = f1.render('Your leaves : ' + str(score), 1, WHITE)
    buttonText = [[0, 0], [0, 0], [0, 0]]
    buttonText[0][0] = f2.render('Price: 100 Leaves', 1, WHITE)
    buttonText[0][1] = f2.render('1 Leaf / Second', 1, WHITE)
    buttonText[1][0] = f2.render('Price: 200 Leaves', 1, WHITE)
    buttonText[1][1] = f2.render('3 Leaves / Second', 1, WHITE)
    buttonText[2][0] = f2.render('Price: 500 Leaves', 1, WHITE)
    buttonText[2][1] = f2.render('9 Leaves / Second', 1, WHITE)
    screen.blit(background, (0, 0))
    screen.blit(text1, (90, 50))
    all_sprites.draw(screen)
    screen.blit(buttonText[0][0], (button1.rect.x + 4, button1.rect.y + 4))
    screen.blit(buttonText[0][1], (button1.rect.x + 10, button1.rect.y + 15 + 4))
    screen.blit(buttonText[1][0], (button2.rect.x + 4, button2.rect.y + 4))
    screen.blit(buttonText[1][1], (button2.rect.x + 4, button2.rect.y + 15 + 4))
    screen.blit(buttonText[2][0], (button3.rect.x + 4, button3.rect.y + 4))
    screen.blit(buttonText[2][1], (button3.rect.x + 4, button3.rect.y + 15 + 4))
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
print("Hurrey!")