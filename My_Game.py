import pygame

# Основные настройки
WIDTH = 360
HEIGHT = 480
FPS = 60
currentFPS = 0
score = 0
whiteSpace = 17
littleSpace = 4
midSpace = 10
bigSpace = 15
buttonSpace = 14
buttonWidth = 99
buttonY = 400
fontScoreSize = 36
fontButtonSize = 15
winScore = 100000
worker = [0, 0, 0]
workerPrice = [100, 200, 500]
workerProd = [1, 3, 9]
text1Coord = [90, 50]
global WHITE
WHITE = (255, 255, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
buttonImage = pygame.image.load('Button.png')
background = pygame.image.load('Background.jpg')
fontScore = pygame.font.Font(None, fontScoreSize)
fontButton = pygame.font.Font(None, fontButtonSize)


# Классы : Кнопки и Клик
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


def checkTouch(score, sprites, Click, worker):
    if score >= workerPrice[0] and pygame.sprite.collide_rect(sprites[0], Click):
        worker[0] += 1
        score -= workerPrice[0]
    if score >= workerPrice[1] and pygame.sprite.collide_rect(sprites[1], Click):
        worker[1] += 1
        score -= workerPrice[1]
    if score >= workerPrice[2] and pygame.sprite.collide_rect(sprites[2], Click):
        worker[2] += 1
        score -= workerPrice[2]
    return score


def blitAll(background, text1, screen, buttonText, button1, button2, button3):
    screen.blit(background, (0, 0))
    screen.blit(text1, (text1Coord[0], text1Coord[1]))
    all_sprites.draw(screen)
    screen.blit(buttonText[0][0], (button1.rect.x + littleSpace, button1.rect.y + littleSpace))
    screen.blit(buttonText[0][1], (button1.rect.x + midSpace,
                button1.rect.y + bigSpace + littleSpace))
    screen.blit(buttonText[1][0], (button2.rect.x + littleSpace, button2.rect.y + littleSpace))
    screen.blit(buttonText[1][1], (button2.rect.x + littleSpace,
                button2.rect.y + bigSpace + littleSpace))
    screen.blit(buttonText[2][0], (button3.rect.x + littleSpace, button3.rect.y + littleSpace))
    screen.blit(buttonText[2][1], (button3.rect.x + littleSpace,
                button3.rect.y + bigSpace + littleSpace))


def renderALL(buttonText):
    buttonText[0][0] = fontButton.render('Price: 100 Leaves', 1, WHITE)
    buttonText[0][1] = fontButton.render('1 Leaf / Second', 1, WHITE)
    buttonText[1][0] = fontButton.render('Price: 200 Leaves', 1, WHITE)
    buttonText[1][1] = fontButton.render('3 Leaves / Second', 1, WHITE)
    buttonText[2][0] = fontButton.render('Price: 500 Leaves', 1, WHITE)
    buttonText[2][1] = fontButton.render('9 Leaves / Second', 1, WHITE)

# Подготовка к циклу игры
running = True
all_sprites = pygame.sprite.Group()
button1 = Button((buttonWidth / 2 + buttonSpace, buttonY))
button2 = Button((3 * buttonWidth / 2 + buttonSpace + whiteSpace, buttonY))
button3 = Button((5 * buttonWidth / 2 + buttonSpace + 2 * whiteSpace, buttonY))
sprites = [button1, button2, button3]
all_sprites.add(sprites)
buttonText = [[0, 0], [0, 0], [0, 0]]

# Цикл игры
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # Поддерживаем работу автокликеров
    currentFPS += 1
    if currentFPS % FPS == 0:
        score += worker[0] * workerProd[0]
        score += worker[1] * workerProd[1]
        score += worker[2] * workerProd[2]

    # Ввод процесса (события)
    for event in pygame.event.get():
        if score >= winScore or event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    score += 1
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            Click = Touch(pos[0], pos[1])
            score = checkTouch(score, sprites, Click, worker)

    # Рендеринг
    text1 = fontScore.render('Your leaves : ' + str(score), 1, WHITE)
    renderALL(buttonText)
    blitAll(background, text1, screen, buttonText, button1, button2, button3)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
print("Hurrey!")
