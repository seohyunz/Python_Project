
import os
import pygame
pygame.init()

screen_width =640
screen_height =480
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("PYGAME")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path,"image")



#배경
background = pygame.image.load(os.path.join(image_path,"background.png"))

#스테이지
stage = pygame.image.load(os.path.join(image_path,"stage2.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지의 높이 위에 캐릭터를 두기 위해 사용

#캐릭터
character = pygame.image.load(os.path.join(image_path,"player2 (3).png"))
character_size = character.get_rect().size
character_with = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_with/2)
character_y_pos = screen_height -character_height -stage_height
character_to_x = 0
character_speed =5

#무기  weapon3
weapon = pygame.image.load(os.path.join(image_path, "wea (1).png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기 여러번 발사 가능
weapons=[]
weapon_speed =10




runnig = True
while runnig:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig= False
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  #캐릭터 왼쪽
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                 character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos +(character_with/2)-(weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])

        if event.type == pygame.KEYUP:
              if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  character_to_x=0

    character_x_pos += character_to_x
                
    if  character_x_pos <0: 
         character_x_pos=0
    elif  character_x_pos> screen_width -  character_with:
         character_x_pos= screen_width -  character_with

    weapons = [[w[0], w[1]- weapon_speed] for w in weapons] #무기 위치를 위로
    #천장에 닿은 무기 사라지기
    weapons = [[w[0], w[1]]for w in weapons if w[1]>0]



    #화면에 그림
    screen.blit(background,(0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))

    screen.blit(stage,(0, screen_height - stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update()

    
pygame.quit()