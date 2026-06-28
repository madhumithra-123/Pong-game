import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

WHITE = (255,255,255)
BLACK = (0,0,0)

clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial",40)

# Paddle
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
BALL_SIZE = 20

left = pygame.Rect(30, HEIGHT//2-PADDLE_HEIGHT//2,
                   PADDLE_WIDTH, PADDLE_HEIGHT)

right = pygame.Rect(WIDTH-45, HEIGHT//2-PADDLE_HEIGHT//2,
                    PADDLE_WIDTH, PADDLE_HEIGHT)

ball = pygame.Rect(WIDTH//2-BALL_SIZE//2,
                   HEIGHT//2-BALL_SIZE//2,
                   BALL_SIZE,
                   BALL_SIZE)

ball_speed_x = random.choice([-6,6])
ball_speed_y = random.choice([-6,6])

left_score = 0
right_score = 0

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    keys = pygame.key.get_pressed()

    # Left Paddle
    if keys[pygame.K_w] and left.top>0:
        left.y -= 7
    if keys[pygame.K_s] and left.bottom<HEIGHT:
        left.y += 7

    # Right Paddle
    if keys[pygame.K_UP] and right.top>0:
        right.y -= 7
    if keys[pygame.K_DOWN] and right.bottom<HEIGHT:
        right.y += 7

    # Ball Movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Wall Collision
    if ball.top<=0 or ball.bottom>=HEIGHT:
        ball_speed_y *= -1

    # Paddle Collision
    if ball.colliderect(left) or ball.colliderect(right):
        ball_speed_x *= -1

    # Score
    if ball.left<=0:
        right_score +=1
        ball.center=(WIDTH//2,HEIGHT//2)
        ball_speed_x=random.choice([-6,6])
        ball_speed_y=random.choice([-6,6])

    if ball.right>=WIDTH:
        left_score +=1
        ball.center=(WIDTH//2,HEIGHT//2)
        ball_speed_x=random.choice([-6,6])
        ball_speed_y=random.choice([-6,6])

    screen.fill(BLACK)

    pygame.draw.rect(screen,WHITE,left)
    pygame.draw.rect(screen,WHITE,right)
    pygame.draw.ellipse(screen,WHITE,ball)

    pygame.draw.aaline(screen,WHITE,(WIDTH//2,0),(WIDTH//2,HEIGHT))

    score = font.render(f"{left_score}   {right_score}",True,WHITE)
    screen.blit(score,(WIDTH//2-score.get_width()//2,20))

    pygame.display.update()

pygame.quit()