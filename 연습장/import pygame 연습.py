import pygame

pygame.init()

backgroud=pygame.display.set_mode((480,360))
pygame.display.set_caption("SONOL")

play=True
while play:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            play=False