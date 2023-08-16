import pygame
import os

# Global Constants
TITLE = "NYAN RUNNER"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

####### GAME LOGIC ######
FPS = 60
ANIM_FPS = FPS // 14
GRAVITY_FORCE = 9.5
#---------------------------
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "NYANNNN.png"))



################# ANIMAÇÕES #################################################################
################################### CAT RUN ######################################################
cat_sheet = pygame.image.load(os.path.join(IMG_DIR, "Cat/NyanCatSpriteSheet.png"))   
RUNNING = []   
for i in range(6):   
    img = cat_sheet.subsurface((i * 136, 0), (136, 84))   
    RUNNING.append(img)   

cat_sheet = pygame.image.load(os.path.join(IMG_DIR, "Cat/NyanCatSpriteSheet_SHIELD.png"))   
RUNNING_SHIELD = []   
for i in range(6):   
    img = cat_sheet.subsurface((i * 136, 0), (136, 84)) 
    RUNNING_SHIELD.append(img)  

#####################################################################################################################
################################### CAT DUCKING ######################################################
cat_sheet_ducking = pygame.image.load(os.path.join(IMG_DIR, "Cat/NyanCatSpriteSheet_DUCK.png"))   
DUCKING = []   
for i in range(6):   
    img = cat_sheet_ducking.subsurface((i * 136, 0), (136, 34))   
    DUCKING.append(img)   

cat_sheet_ducking_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Cat/NyanCatSpriteSheet_DUCKSHIELD.png"))   

DUCKING_SHIELD = []   
for i in range(6):   
    img = cat_sheet_ducking_SHIELD.subsurface((i * 136, 0), (136, 34))   
    DUCKING_SHIELD.append(img)

########################## SPRITES OF GAME ##################################################################
######################################################################################################################

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Bone/Osso1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bone/Osso1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bone/Osso2.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Bone/Osso2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bone/Osso3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bone/Osso3.png")),
]

DOG = [pygame.image.load(os.path.join(IMG_DIR, 'Scene/EvilCuteDog.png'))]



CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Scene/BG.png'))
GROUND = pygame.image.load(os.path.join(IMG_DIR, 'Scene/Ground.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))


####################### TYPE DEFINITION ############################
DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
