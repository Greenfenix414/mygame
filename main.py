import pygame

class game:
    def __init__(self):
        pygame.init()   
        self.screen=pygame.display.set_mode((640,640))
        pygame.display.set_caption('Richards adventures 1')
        pygame.display.set_icon(pygame.image.load("data/richard.png"))
        self.clock=pygame.time.Clock()
        self.running=True
        self.character_img=pygame.image.load('data/richard.png').convert()
        self.sound=pygame.mixer.music.load("data/donuts.wav")
        pygame.mixer.music.play(-1)
        self.delta=0.1
        speed =140
        self.current_speed =speed
        self.x=0
        self.y=0
        self.move_keys_down=0
        self.move_right = False
        self.move_down = False
        self.move_left = False
        self.move_up = False           
            
    def run(self):

        while running:
            self.screen.fill("white")
            self.screen.blit(self.character_img,(x,y))
            if move_keys_down>1:
                current_speed=self.speed/2
            else:
                current_speed=self.speed   
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
            delta = self.clock.tick(60)/1000
            delta=max(0.001, min(0.1,delta))
        pygame.quit()