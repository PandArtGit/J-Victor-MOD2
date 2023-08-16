import random
from dino_runner.utils.constants import DOG
from dino_runner.components.obstacles.obstacle import Obstacle


class Dog(Obstacle):
    position = [100, 250]
    def __init__(self):
        super().__init__(DOG, 0)
        self.rect.y = self.position[random.randint(0, 1)]
        

    def draw(self, screen):
        screen.blit(self.image[0], self.rect)
