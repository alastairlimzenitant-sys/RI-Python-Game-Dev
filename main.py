import pygame
import random

pygame.init()
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()
fps = 100
score = 0
direction = "right"
save_direction = "right"
snake = [pygame.Rect(100,100,50,50)]
black = (0,0,0)
blue = (6, 90, 185)
red = (255,0,0)
yellow = (222,229,27)
green = (103,165,11)
running = True
apple = pygame.Rect(158,158,35,35)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if(keys[pygame.K_LEFT]):
        save_direction = "left"
    if(keys[pygame.K_RIGHT]):
        save_direction = "right"
    if(keys[pygame.K_UP]):
        save_direction = "up"
    if(keys[pygame.K_DOWN]):
        save_direction = "down"    
    if snake[0].x%50==0 and snake[0].y%50==0:
        direction = save_direction
    if pygame.Rect.colliderect(snake[0],apple):
        apple.x = random.randint(0,11)*50+8
        apple.y = random.randint(0,7)*50+8
        score += 1
        snake.append(pygame.Rect(random.randint(0,11)*50,random.randint(0,7)*50,50,50))
    screen.fill(green)
    pygame.draw.line(screen,yellow,(50,0),(50,400),5)
    pygame.draw.line(screen,yellow,(100,0),(100,400),5)
    pygame.draw.line(screen,yellow,(150,0),(150,400),5)
    pygame.draw.line(screen,yellow,(200,0),(200,400),5)
    pygame.draw.line(screen,yellow,(250,0),(250,400),5)
    pygame.draw.line(screen,yellow,(300,0),(300,400),5)
    pygame.draw.line(screen,yellow,(350,0),(350,400),5)
    pygame.draw.line(screen,yellow,(400,0),(400,400),5)
    pygame.draw.line(screen,yellow,(450,0),(450,400),5)
    pygame.draw.line(screen,yellow,(500,0),(500,400),5)
    pygame.draw.line(screen,yellow,(550,0),(550,400),5)
    pygame.draw.line(screen,yellow,(0,50),(600,50),5)
    pygame.draw.line(screen,yellow,(0,100),(600,100),5)
    pygame.draw.line(screen,yellow,(0,150),(600,150),5)
    pygame.draw.line(screen,yellow,(0,200),(600,200),5)
    pygame.draw.line(screen,yellow,(0,250),(600,250),5)
    pygame.draw.line(screen,yellow,(0,300),(600,300),5)
    pygame.draw.line(screen,yellow,(0,350),(600,350),5)
    for i in range(0,len(snake)):
        pygame.draw.rect(screen,blue,snake[i])
    pygame.draw.rect(screen,red,apple)
    myfont = pygame.font.SysFont('comic sans',50)
    textsurface = myfont.render("score=" +str(score),True,black)
    screen.blit(textsurface, (0,0))
    if direction == "left":
        snake[0].x -= 2
    if direction == "right":
        snake[0].x += 2
    if direction == "up":
        snake[0].y -= 2
    if direction == "down":
        snake[0].y += 2
    snake[0].clamp_ip(screen.get_rect())
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()