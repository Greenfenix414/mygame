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
        self.speed =140
        self.current_speed =self.speed
        self.x=0
        self.y=0
        self.move_keys_down=0
        self.move_right = False
        self.move_down = False
        self.move_left = False
        self.move_up = False
        self.running=True     
              
            
    def run(self):

        while self.running:
            self.screen.fill("white")
            self.screen.blit(self.character_img,(self.x,self.y))
            if self.move_keys_down>1:
                self.current_speed=self.speed/2
            else:
                self.current_speed=self.speed   
            if self.move_right:
                self.x+=self.current_speed*delta
            if self.move_down:
                self.y+=self.current_speed*delta
            if self.move_left:
                self.x-=self.current_speed*delta
            if self.move_up:
                self.y-=self.current_speed*delta           
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_d:
                        self.move_keys_down+=1
                        self.move_right=True
                    if event.key==pygame.K_s:
                        self.move_keys_down+=1
                        self.move_down=True     
                    if event.key==pygame.K_a:
                        self.move_keys_down+=1
                        self.move_left=True
                    if event.key==pygame.K_w:
                        self.move_keys_down+=1
                        self.move_up=True                         
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_d:
                        self.move_keys_down-=1
                        self.move_right=False
                    if event.key==pygame.K_s:
                        self.move_keys_down-=1
                        self.move_down=False     
                    if event.key==pygame.K_a:
                        self.move_keys_down-=1
                        self.move_left=False
                    if event.key==pygame.K_w:
                        self.move_keys_down-=1
                        self.move_up=False                    
            pygame.display.flip()
            delta = self.clock.tick(60)/1000
            delta=max(0.001, min(0.1,delta))
        pygame.quit()
        
game().run()        