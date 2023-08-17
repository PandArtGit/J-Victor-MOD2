import pygame

 

from dino_runner.utils.constants import(
    GROUND,
    BG,
    ICON,
    FLAG_SELECT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    TITLE,FPS,
    DEFAULT_TYPE
)

from dino_runner.components.dinosaur import Dinosaur

from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

from dino_runner.utils.text_utils import draw_message_component

from dino_runner.components.powerups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.score = 0
        self.death_count = 0
        self.flag_select = 0

######## difficulty ###########
        self.game_speed = 0 
        self.speed_add = 0.1
        self.point_of_speed = 50
#-------------------------------

        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.x_pos_ground = 0
        self.y_pos_ground = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
    
    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                
                self.show_menu()
                self.handle_events_on_menu() 
                
        
        pygame.display.quit()
        pygame.quit()
    
    def run(self):
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 10
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)
    
    def update_score(self):
        self.score += 1
        if self.score % self.point_of_speed == 0:
            self.game_speed += self.speed_add
    
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill("black")
        
        self.draw_background()
        self.draw_ground()

        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed / 2
    
    def draw_ground(self):
        image_width = GROUND.get_width()
        self.screen.blit(GROUND, (self.x_pos_ground, self.y_pos_ground))
        self.screen.blit(GROUND, (image_width + self.x_pos_ground, self.y_pos_ground))
        if self.x_pos_ground <= -image_width/4:
            self.screen.blit(GROUND, (image_width + self.x_pos_ground, self.y_pos_ground))
            self.x_pos_ground = 0
        self.x_pos_ground -= self.game_speed

    def draw_score(self):
        draw_message_component(
            f"PONTUAÇÃO: {self.score}",
            self.screen,
            "white",
            pos_x_center= SCREEN_WIDTH/2,
            pos_y_center= SCREEN_HEIGHT - 20
        )
    
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"<{self.player.type.capitalize()} FALTAM {time_to_show} SEGUNDOS>",
                    self.screen,
                    "white",
                    font_size= 18,
                    pos_x_center= SCREEN_WIDTH/2,
                    pos_y_center= SCREEN_HEIGHT - 45
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
    
    def show_menu(self):
        self.screen.fill("grey")
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            draw_message_component("Aperte ESPAÇO para iniciar",
                self.screen,
                font_size= 24,
                pos_x_center= half_screen_width,
                pos_y_center= half_screen_height + 200
            )
            self.screen.blit(FLAG_SELECT[self.flag_select], (half_screen_width - (FLAG_SELECT[self.flag_select].get_width()/2), half_screen_height-150))
            self.screen.blit(ICON, (half_screen_width - (ICON.get_width()/2), half_screen_height-100))
            
        else:
            draw_message_component(
                "Aperte ESPAÇO para reiniciar",
                self.screen,
                font_size= 24,
                pos_x_center= half_screen_width,
                pos_y_center= half_screen_height - 200
            )
            draw_message_component(
                f"SUA PONTUAÇÃO: {self.score}",
                self.screen,
                pos_y_center= half_screen_width
            )
            draw_message_component(
                f"SUAS MORTES: {self.death_count}",
                self.screen,
                pos_y_center= half_screen_width - 50
            )
            self.screen.blit(FLAG_SELECT[self.flag_select], (half_screen_width - (FLAG_SELECT[self.flag_select].get_width()/2), half_screen_height-150))
            self.screen.blit(ICON, (half_screen_width - (ICON.get_width()/2), half_screen_height-100))
    
    def handle_events_on_menu(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: 
                    self.run()
                if event.key == pygame.K_RIGHT:
                    if self.flag_select < len(FLAG_SELECT) - 1:
                        self.flag_select += 1
                    else:
                        self.flag_select = 0
                if event.key == pygame.K_LEFT:
                    if self.flag_select > 0:
                        self.flag_select -= 1
                    else:
                        self.flag_select = len(FLAG_SELECT) - 1
                self.player.flag_select = self.flag_select
            
        pygame.display.flip()

    
            
