from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH







class Debugar:
    def __init__(self):
        self.screen_2d = [[] for y in range(SCREEN_WIDTH)]
        for x in range(SCREEN_HEIGHT):
            self.screen_2d.append(x+1)
            for y in range(SCREEN_HEIGHT):
                self.screen_2d[x].append(y+1)
    
    def show_screen_2d_matriz(self):
        print(self.screen_2d)

    def update(self):
        pass

    def draw(self):
        pass
        


