import pygame

pygame.init()   

screen=pygame.display.set_mode((640,640))
pygame.display.set_caption('Richards adventures 1')
character_img=pygame.image.load('character.png').convert()
running=True
clock=pygame.time.Clock()
sound=pygame.mixer.music.load("donuts.wav")
pygame.mixer.music.play(-1)
delta=0.1
speed =70
current_speed =speed
x=0
y=0
move_keys_down=0
move_right = False
move_down = False
move_left = False
move_up = False
while running:
    screen.fill("white")
    screen.blit(character_img,(x,y))
    if move_keys_down>1:
        current_speed=speed/2
    else:
        current_speed=speed   
    if move_right:
        x+=current_speed*delta
    if move_down:
        y+=current_speed*delta
    if move_left:
        x-=current_speed*delta
    if move_up:
        y-=current_speed*delta           
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:
                move_keys_down+=1
                move_right=True
            if event.key==pygame.K_s:
                move_keys_down+=1
                move_down=True     
            if event.key==pygame.K_a:
                move_keys_down+=1
                move_left=True
            if event.key==pygame.K_w:
                move_keys_down+=1
                move_up=True                         
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_d:
                move_keys_down-=1
                move_right=False
            if event.key==pygame.K_s:
                move_keys_down-=1
                move_down=False     
            if event.key==pygame.K_a:
                move_keys_down-=1
                move_left=False
            if event.key==pygame.K_w:
                move_keys_down-=1
                move_up=False                    
    pygame.display.flip()
    delta = clock.tick(60)/1000
    delta=max(0.001, min(0.1,delta))
pygame.quit()