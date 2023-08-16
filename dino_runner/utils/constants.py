import pygame
import os

# Global Constants
TITLE = "NYAN RUNNER"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "NYANNNN.png"))

cat_sheet = pygame.image.load(os.path.join(IMG_DIR, "Cat/NyanCatSpriteSheet.png"))  # cat anim
RUNNING = []  # cat anim
for i in range(6):  # cat anim
    img = cat_sheet.subsurface((i * 136, 0), (136, 84))  # cat anim
    RUNNING.append(img)  # cat anim

cat_sheet = pygame.image.load(os.path.join(IMG_DIR, "Cat/NyanCatSpriteSheet_SHIELD.png"))  # cat anim
RUNNING_SHIELD = []  # cat anim
for i in range(6):  # cat anim
    img = cat_sheet.subsurface((i * 136, 0), (136, 84))  # cat anim
    RUNNING_SHIELD.append(img)  # cat anim
#####################################################################################################################

cat_sheet_ducking = pygame.image.load(os.path.join(IMG_DIR, "Cat/NyanCatSpriteSheet_DUCK.png"))  # cat anim
DUCKING = []  # cat anim
for i in range(6):  # cat anim
    img = cat_sheet_ducking.subsurface((i * 136, 0), (136, 34))  # cat anim
    DUCKING.append(img)  # cat anim

cat_sheet_ducking_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Cat/NyanCatSpriteSheet_DUCKSHIELD.png"))  # cat anim

DUCKING_SHIELD = []  # cat anim
for i in range(6):  # cat anim
    img = cat_sheet_ducking_SHIELD.subsurface((i * 136, 0), (136, 34))  # cat anim
    DUCKING_SHIELD.append(img)  # cat anim
######################################################################################################################

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Scene/BG.png'))
#BG = pygame.transform.scale2x(BG)
GROUND = pygame.image.load(os.path.join(IMG_DIR, 'Scene/Ground.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
