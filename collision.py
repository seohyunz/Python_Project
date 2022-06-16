
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

#공 만들기
ball_images =[
    pygame.image.load(os.path.join(image_path,"ball1.png")),
    pygame.image.load(os.path.join(image_path,"ball2.png")),
    pygame.image.load(os.path.join(image_path,"ball3.png")),
    pygame.image.load(os.path.join(image_path,"ball4.png"))
]

#공 크기에 따른 스피드
ball_speed_y =[-18,-15,-12,-9]
balls =[]
balls.append({
    "pos_x" : 50,
    "pos_y" : 50, 
    "img_idx" : 0, #공 이미지
    "to_x" : 3, #x축 이동방향
    "to_y" : -6, #y축 이동방향
    "init_spd_y" : ball_speed_y[0] #최초 속도
})


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

    #공 위치 
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        #가로벽에 닿았을 때 공 이동 위치 변경(튕기기)
        if ball_pos_x<0 or ball_pos_x> screen_width-ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        #세로
        #튕겨서 올라오기
        if ball_pos_y >= screen_height-stage_height-ball_height:
            ball_val["to_y"]= ball_val["init_spd_y"]
        else: # 그 외 속도 증가
            ball_val["to_y"]+=0.5

        ball_val["pos_x"]+= ball_val["to_x"]
        ball_val["pos_y"]+= ball_val["to_y"]

    #충돌 처리 
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

    ball_rect = ball_images[ball_img_idx].get_rect()
    ball_rect.left = ball_pos_x
    ball_rect.top = ball_pos_y

    if character_rect.collidedict(ball_rect):
        runnig = False
        break


    #화면에 그림
    screen.blit(background,(0,0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))

    for idx,val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx= val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x,ball_pos_y))



    screen.blit(stage,(0, screen_height - stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))

    pygame.display.update()

    
pygame.quit()