import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")
icon = pygame.image.load("img/5555.jpeg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/klipartz.com.png")
target_width = 80
target_height = 80

target_x = random.randint(0, 800 - target_width)
target_y = random.randint(0, 600 - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

score = 0
font = pygame.font.Font(None, 36)

start_time = pygame.time.get_ticks()

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # target hit check
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # hit = change color
                target_x = random.randint(0, 800 - target_width)
                target_y = random.randint(0, 600 - target_height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


                score += 1

    # display score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # time count
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    remaining_time = max(60 - elapsed_time, 0)
    time_text = font.render(f"Time: {remaining_time}", True, (255, 255, 255))
    screen.blit(time_text, (10, 50))

    # end game
    if remaining_time == 0:
        running = False

    # display target
    screen.blit(target_image, (target_x, target_y))

    pygame.display.update()

pygame.quit()


