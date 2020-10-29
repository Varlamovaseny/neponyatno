import pygame
pygame.init()
blue = (0, 0, 255)

pygame.display.set_caption("Текст")
pygame.mouse.set_visible(False)
sc = pygame.display.set_mode((800, 600))

f1 = pygame.font.Font(None, 60)
text1 = f1.render('Всем привет', 1, (255, 255, 255))
f2 = pygame.font.SysFont('serif', 30)
text2 = f2.render("задание на урок", 0, (225, 225, 0))

sc.blit(text1, (270, 250))
sc.blit(text2, (290, 300))

pygame.display.update()

pygame.draw.rect(sc, (255, 0, 0), (370, 170, 50, 50))

pygame.display.update()

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
