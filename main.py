import pygame


# inicializace pygame
pygame.init()

# vytvoření obrazovky 

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Harry potter game")


distance = 4
fps = 144
clock = pygame.time.Clock()

# Definujeme barvy 
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#barva pozadí


#Tvary
#- Čára


# Obrázky
harry_potter_image = pygame.image.load("IMG/heri potr.png")
harry_potter_rect = harry_potter_image.get_rect()
harry_potter_rect.midleft = (10, height//2)

coin_image = pygame.image.load("IMG/koin.png")
coin_rect = coin_image.get_rect()
coin_rect.center = (width//2, height//2)


# Systémové fonty
# fonts = pygame.font.get_fonts()
# for one_font in fonts:
#      print(one_font)

# mvboli

# Nastavení fontu
#system_font = pygame.font.SysFont("mvboli", 41)
custom_font = pygame.font.Font("fonts/Harry_potter_font.ttf", 60)
# Font a text
# system_text = system_font.render("Harry potter", True, "yellow")
# system_text_rect = system_text.get_rect()
# system_text_rect.center = (width//2, height//2)
custom_text = custom_font.render("Harry Potter", True, "green")
custom_text_rect = custom_text.get_rect()
custom_text_rect.midtop = (width//2, 5)
pygame.draw.line(screen, "orange", (0, 70), (width, 70), 5)
# Hlavní herní cyklus
lets_continue = True
# system_font = pygame.font.SysFont("nirmalaui", 30)

# font_style = system_font.render("Albus brumbál", True, "yellow")
# font_style_rect = font_style.get_rect()
# font_style_rect.midleft = (width//2, height//2)


# Hudba v pozadí
pygame.mixer.music.load("soundy/bgmusic.wav")
pygame.mixer.music.set_volume(0.2)
# Přehrání hudby v pozadí
pygame.mixer.music.play(-1)


# Nahrání zvuku 
sound_carti = pygame.mixer.Sound("soundy/playgai.mp3")
sound_carti.set_volume(0.1)
# Přehrání zvuku
sound_carti.play()


while lets_continue:
     #sbirani eventu 
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
                lets_continue = False 
        #event.type je kod událostí na obrazovce
          if (event.type == pygame.MOUSEMOTION) and (event.buttons[0] == 1):
               harry_potter_rect.center = event.pos
          # Posouvani po jednom 
          # if event.type == pygame.KEYDOWN:
          #   print(pygame.key.name(event.key))
          #   if event.key == pygame.K_UP:
          #        harry_potter_rect.y -= distance
          #   elif event.key == pygame.K_DOWN:
          #        harry_potter_rect.y += distance
          #   elif event.key == pygame.K_RIGHT:
          #        harry_potter_rect.x += distance
          #   elif event.key == pygame.K_LEFT:
          #        harry_potter_rect.x -= distance


     # Výpis všech kláves
     keys = pygame.key.get_pressed()
     if (keys[pygame.K_UP] or keys[pygame.K_w]) and harry_potter_rect.top > 70:
          harry_potter_rect.y -= distance
     elif (keys[pygame.K_DOWN] or keys[pygame.K_s]) and harry_potter_rect.bottom < height:
          harry_potter_rect.y += distance
     elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and harry_potter_rect.right < width:
          harry_potter_rect.x += distance
     elif (keys[pygame.K_LEFT] or keys[pygame.K_a]) and harry_potter_rect.left > 0:
          harry_potter_rect.x -= distance
     # Vyplnění obrazovky černou barvou
     screen.fill(black)
    
     

     
     # Přidání textu 
     #screen.blit(system_text, system_text_rect)
     screen.blit(custom_text, custom_text_rect)
    
     pygame.draw.line(screen, green, (0, 70), (width, 70), 2)
     # # - Kružnice 
     # pygame.draw.circle(screen, yellow, (width/2, height/2), 100, 8)
     # # - Kruh
     # pygame.draw.circle(screen, white, (width/2, height/2), 90, 0)
     # # - Čtverec
     # pygame.draw.rect(screen, blue, (width//2 - 50, height//2 - 50, 100, 100))


     # Přidání obrázku
     screen.blit(harry_potter_image, harry_potter_rect)
     
     screen.blit(coin_image, coin_rect)
     pygame.display.update()  

     # Tikání hodin
     clock.tick(fps)

# Ukončení pygame
pygame.quit()




