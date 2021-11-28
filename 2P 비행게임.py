import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("C:\dksrywns\shot.wav")
pygame.mixer.music.load("C:/dksrywns/08-boss-_heavy-long_.wav")
pygame.mixer.music.play()
screen_width=460
screen_height=660
screen=pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("2인용게임")

clock = pygame.time.Clock()

background=pygame.image.load("C:/dksrywns/123.png")

player1=pygame.image.load("C:/dksrywns/2.png")
player1_size= player1.get_rect().size
player1_width= player1_size[0]
player1_height= player1_size[1]
player1_x_pos= (screen_width/2)-(player1_width/2)
player1_y_pos= screen_height-player1_height

player2=pygame.image.load("C:/dksrywns/1.png")
player2_size= player2.get_rect().size
player2_width= player2_size[0]
player2_height= player2_size[1]
player2_x_pos= (screen_width/2)-(player2_width/2)
player2_y_pos=0

weapon1 =pygame.image.load("C:/dksrywns/6.png")
weapon1_size= weapon1.get_rect().size
weapon1_width= weapon1_size[0]

weapon2=pygame.image.load("C:/dksrywns/제목 없음.png")
weapon2_size= weapon2.get_rect().size
weapon2_width= weapon2_size[0]

weapons=[]
weapon=[]

p_x=0
p_y=0
s_x=0
s_y=0

weapon1_speed=7
weapon2_speed=7               
player1_speed=0.8
player2_speed=0.8

game_font = pygame.font.Font(None, 50)
total_time = 20
start_ticks = pygame.time.get_ticks()

weapon1_remove= -1
weapon2_remove= -1

sound = pygame.mixer.Sound("C:\dksrywns\shot.wav")

running  = True
while running:
    dt=clock.tick(60)
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
            
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_UP:
                 p_y -= player1_speed
             elif event.key == pygame.K_RIGHT:
                 p_x += player1_speed
             elif event.key == pygame.K_LEFT:
                 p_x -= player1_speed
             elif event.key == pygame.K_DOWN:
                 p_y += player1_speed
             elif event.key == pygame.K_SLASH:                  
                 weapon1_x_pos = player1_x_pos + (player1_width/2) - (weapon1_width/2)
                 weapon1_y_pos = player1_y_pos
                 weapons.append([weapon1_x_pos, weapon1_y_pos])
                 sound.play()

        if event.type == pygame.KEYUP:
             if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                p_x=0
             elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                p_y=0

        if event.type == pygame.KEYDOWN:
             if event.key ==pygame.K_w:
                 s_y -=player2_speed
             elif event.key ==pygame.K_d:
                 s_x +=player2_speed
             elif event.key ==pygame.K_a:
                 s_x -=player2_speed
             elif event.key ==pygame.K_s:
                 s_y +=player2_speed 
             elif event.key == pygame.K_SPACE:                  
                 weapon2_x_pos = player2_x_pos + (player2_width/2) - (weapon2_width/2)
                 weapon2_y_pos = player2_y_pos
                 weapon.append([weapon2_x_pos, weapon2_y_pos])
                 sound.play()
                 
        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_d or event.key ==pygame.K_a:
                s_x=0
            elif event.key ==pygame.K_w or event.key ==pygame.K_s:
                s_y=0

    player1_x_pos += p_x*dt
    player1_y_pos += p_y*dt      
    player2_x_pos += s_x*dt
    player2_y_pos += s_y*dt

    if player1_x_pos < 0:
        player1_x_pos = 0
    elif player1_x_pos > screen_width - player1_width:
        player1_x_pos = screen_width - player1_width
       
    if player1_y_pos < 0:
        player1_y_pos = 0
    elif player1_y_pos > screen_height - player1_height:    
        player1_y_pos = screen_height - player1_height
   
    if player2_x_pos < 0:
        player2_x_pos = 0
    elif player2_x_pos > screen_width - player1_width:
        player2_x_pos = screen_width - player1_width
       
    if player2_y_pos < 0:
        player2_y_pos = 0
    elif player2_y_pos > screen_height - player1_height:    
        player2_y_pos = screen_height - player1_height

        
    weapons = [ [w[0],w[1] - weapon1_speed] for w in weapons]
    weapon = [ [i[0],i[1] + weapon2_speed] for i in weapon]
    
    player1_rect = player1.get_rect()
    player1_rect.left = player1_x_pos
    player1_rect.top = player1_y_pos
    
    player2_rect = player1.get_rect()
    player2_rect.left = player2_x_pos
    player2_rect.top = player2_y_pos


    if player1_rect.colliderect(player2_rect):
        pygame.mixer.music.stop()
        game_result2 = "game over"
        running = False
        break
    
  
    for weapon2_idx, weapon2_val in enumerate(weapon):
            weapon2_x_pos = weapon2_val[0]
            weapon2_y_pos = weapon2_val[1]

            weapon2_rect = weapon2.get_rect()
            weapon2_rect.left = weapon2_x_pos
            weapon2_rect.top = weapon2_y_pos  

            if player1_rect.colliderect(weapon2_rect):    
                weapon2_remove = weapon2_idx
                pygame.mixer.music.stop()
                game_result2 = "game over"   
                running = False
                break

    for weapon1_idx, weapon1_val in enumerate(weapons):
        weapon1_x_pos = weapon1_val[0]
        weapon1_y_pos = weapon1_val[1]

        weapon1_rect = weapon1.get_rect()
        weapon1_rect.left = weapon1_x_pos
        weapon1_rect.top = weapon1_y_pos    

        if player2_rect.colliderect(weapon1_rect):
            weapon1_remove = weapon1_idx
            pygame.mixer.music.stop()
            game_result2 = "game over"
            running = False
            break

    for weapon2_idx, weapon2_val in enumerate(weapon):
        weapon2_x_pos = weapon2_val[0]
        weapon2_y_pos = weapon2_val[1]

        weapon2_rect = weapon2.get_rect()
        weapon2_rect.left = weapon2_x_pos
        weapon2_rect.top = weapon2_y_pos

        for weapon1_idx, weapon1_val in enumerate(weapons):
            weapon1_x_pos = weapon1_val[0]
            weapon1_y_pos = weapon1_val[1]

            weapon1_rect = weapon1.get_rect()
            weapon1_rect.left = weapon1_x_pos
            weapon1_rect.top = weapon1_y_pos    

            if weapon1_rect.colliderect(weapon2_rect):
                weapon1_remove = weapon1_idx
                weapon2_remove = weapon2_idx
        

    if weapon1_remove > -1:
        del weapons[weapon1_remove]
        weapon1_remove=-1

    if weapon2_remove > -1:
        del weapon[weapon2_remove]
        weapon2_remove=-1      
 
 
 

    screen.blit(background, (0,0))
    for weapon1_x_pos, weapon1_y_pos in weapons:
        screen.blit(weapon1, (weapon1_x_pos, weapon1_y_pos))
    screen.blit(player1, (player1_x_pos, player1_y_pos ))

    for weapon2_x_pos, weapon2_y_pos in weapon:
        screen.blit(weapon2, (weapon2_x_pos, weapon2_y_pos))   
    screen.blit(player2, (player2_x_pos, player2_y_pos ))
               

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer=game_font.render(str(int(total_time-elapsed_time)), True, (0, 255, 225))
    screen.blit(timer, (10,10))

    if total_time - elapsed_time <= 0:
        game_result2 = "time over"
        running = False

    pygame.display.update()

msg = game_font.render(game_result2, True, (255, 0, 255)) 
msg_rect = msg.get_rect(center=(int(screen_width/2), int(screen_height/2)))
screen.blit(msg, msg_rect)

pygame.display.update()

pygame.time.delay(2000)
pygame.mixer.quit()
pygame.quit()