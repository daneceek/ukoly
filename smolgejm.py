# Small game 
import pygame
import random


pygame.init()

score = 0
distance = 5
fps = 100
width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harry potter small game")

clock = pygame.time.Clock()

dyne_obr = pygame.image.load("IMG/heri potr.png")
dyne_rekt = dyne_obr.get_rect()
dyne_rekt.center = (width//2, height//2)

sovick_obr = pygame.image.load("IMG/sovicka.png")
sovicka_rekt = sovick_obr.get_rect()
sovicka_rekt.center = (100, 150)

hra_font = pygame.font.Font("fonts/Harry_potter_font.ttf", 40)
hra_text = hra_font.render("Harry Potter Game", True, "yellow")
hra_text_rekt = hra_text.get_rect()
hra_text_rekt.center = (width/2, 30)

pygame.mixer.music.load("soundy/instr.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

sound_carti = pygame.mixer.Sound("soundy/playgai.mp3")
sound_carti.set_volume(0.2)
pokracuj = True
while pokracuj:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pokracuj = False
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and dyne_rekt.top > 60:
        dyne_rekt.y -= distance 
    elif (keys[pygame.K_s] or keys[pygame.K_DOWN]) and dyne_rekt.bottom < height:
        dyne_rekt.y += distance
    elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and dyne_rekt.left > 0:
        dyne_rekt.x -= distance
    elif (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and dyne_rekt.right < width:
        dyne_rekt.x += distance


    score_font = pygame.font.Font("fonts/Harry_potter_font.ttf", 30)
    score_text = score_font.render(f"Score: {score}", True, "yellow")
    score_rect = score_text.get_rect()
    score_rect.center = (150, 30)


    screen.fill("black")
    screen.blit(dyne_obr, dyne_rekt)
    screen.blit(sovick_obr, sovicka_rekt)
    screen.blit(hra_text, hra_text_rekt)
    screen.blit(score_text, score_rect)
    pygame.draw.line(screen, "white", (0, 60), (width, 60), 2)
    clock.tick(fps)

    #Tvary
    
    # Kolize
    
    if dyne_rekt.colliderect(sovicka_rekt):
                sound_carti.play()
                score += 1
                sovicka_rekt.centerx = random.randint(0 + 18, width - 18)
                sovicka_rekt.centery = random.randint(60 + 18, height - 18)
                
    pygame.display.update()

pygame.quit()