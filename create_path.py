import sys
import pygame

pygame.init()

size = width, height = 720, 640
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

pos_list = []

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos_list.append(event.pos)

    mouse_pos = pygame.mouse.get_pos()

    screen.fill(black)

    for pos in pos_list:
        pygame.draw.circle(screen, white, pos, 5)

    if pos_list:
        pos_list.append(mouse_pos)
        pygame.draw.lines(screen, white, False, pos_list)
        pos_list.pop()
    pygame.draw.circle(screen, white, mouse_pos, 5)
    pygame.display.flip()
