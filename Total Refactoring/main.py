# Bren007pie July 5, 2020 NEVADA Main game loop

import pygame
from pygame.locals import *
import cevent
#Tutorial: http://pygametutorials.wikidot.com/tutorials

class CApp(cevent.CEvent):
    def __init__(self):
        self.running = True
        self.display_surf = None
        self.size = self.width, self.height = 640, 400
        self._image_surf = None
        self.image_position = self.image_x, self.image_y = 0, 0
        self.image_velocity = self.image_Vx,self.image_Vy = 0,0
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        self.running = True
        self._image_surf = pygame.image.load("hacker.jpg").convert()

        self.myfont = pygame.font.SysFont('arial',69,True,True)

    def on_loop(self):

        pass
    def on_render(self):
        self.image_x += self.image_Vx
        self.image_y += self.image_Vy
        pygame.draw.rect(self.display_surf,(255,0,0),pygame.Rect(0,0,640,400))  # Background
        #print(self.image_y, self.image_Vy)
        self.display_surf.blit(self._image_surf,(self.image_x,self.image_y))
        self.display_surf.blit(self.myfont.render("Chikens are good", False, (0,0,255)),(0,0))  # Blit order does matter
        pygame.display.flip()

        self.clock.tick(60)
        #self.clock.tick()
        #print("FPS:",self.clock.get_fps())

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self.running):  # Game Loop
            for event in pygame.event.get():  # Events
                self.on_event(event)
            self.on_loop()  # Update game world
            self.on_render()  # Render

        self.on_cleanup()  # Cleanup quitting
        print("I'M DONE")



if __name__ == "__main__" :  # Main call that runs the app
    theApp = CApp()
    theApp.on_execute()