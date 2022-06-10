
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
stage = pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #스테이지의 높이 위에 캐릭터를 두기 위해 사용

#캐릭터
character = pygame.image.load(os.path.join(image_path,"player2 (3).png"))
character_size = character.get_rect().size
character_with = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_with/2)
character_y_pos = screen_height -character_height -stage_height


runnig = True
while runnig:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig= False
    

    #화면에 그림
    screen.blit(background,(0,0))
    screen.blit(stage,(0, screen_height - stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))
    
    pygame.display.update()

    
pygame.quit()