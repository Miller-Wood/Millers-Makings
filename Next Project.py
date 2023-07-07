import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Connect Four but AWESOME!")
font = pygame.font.SysFont("comic sans", 20)
big_font = pygame.font.SysFont("comic sans", 50)
timer = pygame.time.Clock()
fps = 60
run = True

def draw_screen():
    pygame.draw.rect(screen, "light blue")
    
while run:
    draw_screen()