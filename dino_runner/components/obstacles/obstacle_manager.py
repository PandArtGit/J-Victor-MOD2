import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.dog import Dog

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
    
    def update(self, game):
        obstacle_type = [
            Cactus(),
            Dog(),
        ]
        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0, 1)])
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.death_count += 1
                    game.playing = False
                    
                    break
                else:
                    self.obstacles.remove(obstacle)


    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
 