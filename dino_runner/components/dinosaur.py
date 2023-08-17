import pygame

from pygame.sprite import Sprite

from dino_runner.utils.constants import (
    RUNNING,
    DUCKING,
    DEFAULT_TYPE,
    SHIELD_TYPE,
    DUCKING_SHIELD,
    RUNNING_SHIELD,
    FLAG_TRACE,
    FPS,
    ANIM_FPS,
    GRAVITY_FORCE
)

 

DUCK_IMG = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}

RUN_IMG = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}

X_POS = 300

Y_POS = 310

Y_POS_DUCK = 360

JUMP_VEL = 5





class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.flag_select = 0
        self.flag_rect = FLAG_TRACE[self.flag_select].get_rect()
        self.flag_rect.x = -10 
        self.flag_rect.y = 0

        self.frameCount = 1  # cat anim
        self.nyanFrame = 0  # cat anim
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_vel = JUMP_VEL
        self.setup_state()
    
    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0
    
    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump(user_input)
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jump and self.dino_rect.y == Y_POS:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        elif not user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

        self.frameCount += 1  # cat anim
        if self.frameCount > FPS:  # cat anim
            self.frameCount = 1  # cat anim

        if self.nyanFrame > 5:  # cat anim
            self.nyanFrame = 0  # cat anim
            self.frameCount = 0  # cat anim
        
        
    
    def run(self):
        self.image = RUN_IMG[self.type][self.nyanFrame]  # cat anim (padrão: self.steep_index)
        
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS

        # a animação tem 6 frames, se quero passar a uma taxa de 14 FPS devo dividir o frame rate por 14
        if self.frameCount == (self.nyanFrame + 1) * ANIM_FPS:  # cat anim
            self.nyanFrame += 1  # cat anim
        
    
    def jump(self, user_input):
        
        if self.dino_jump and not user_input[pygame.K_DOWN]: # JUST JUMP

####################### JUST JUMP ##############################################
            self.image = RUN_IMG[self.type][self.nyanFrame]
            if self.frameCount == (self.nyanFrame + 1) * ANIM_FPS:  # cat anim
                self.nyanFrame += 1  # cat anim
############
            self.dino_rect.y -= self.jump_vel * ANIM_FPS
            self.jump_vel -= GRAVITY_FORCE/50
        
        
        elif self.dino_jump: # JUMP DUCK
####################### JUMP DUCK ##############################################
            self.image = DUCK_IMG[self.type][self.nyanFrame]
            if self.frameCount == (self.nyanFrame + 1) * ANIM_FPS:  # cat anim
                self.nyanFrame += 1  # cat anim
############ FEITO PARA O JOGADOR DESCER MAIS RAPIDO AO APERTAR PRA BAIXO
            self.dino_rect.y -= self.jump_vel * ANIM_FPS
            self.jump_vel -= GRAVITY_FORCE/25
        print(self.jump_vel)

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL
    
    def duck(self):
        self.image = DUCK_IMG[self.type][self.nyanFrame]  # cat anim (padrão: self.steep_index)
        
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK

        # a animação tem 6 frames, se quero passar a uma taxa de 14 FPS devo dividir o frame rate por 14
        if self.frameCount == (self.nyanFrame + 1) * ANIM_FPS:  # cat anim
            self.nyanFrame += 1  # cat anim

    def draw(self, screen):
        flagpos_x = self.dino_rect.x + self.flag_rect.x
        flagpos_y = self.dino_rect.y + self.flag_rect.y
        for i in range(7):
            screen.blit(FLAG_TRACE[self.flag_select], (-(i * 64) + flagpos_x, flagpos_y))
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))


            


