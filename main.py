import pygame as pg
from log import log

class WIN:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        self.clock = pg.time.Clock()
        self.running = True
        self.fps = 60
    
    def run(self):
        while self.running:
            self.clock.tick(self.fps)
            self.screen.fill((0, 0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            pg.display.flip()
        pg.quit()
        log("Quit")

if __name__ == "__main__":
    win = WIN()
    win.run()