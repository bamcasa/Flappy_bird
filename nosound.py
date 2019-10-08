import pygame
from pygame.locals import *
from math import trunc
import sys
import random

pygame.init()

class Flappybird:
    def __init__(self):
        self.FPS = 30
        self.screen = pygame.display.set_mode((288, 512))
        self.birdScript = 0
        self.jump = 0
        self.jumpspeed = 10
        self.down = 5
        self.pipeX = 288
        self.pipeY = 0
        self.birdY = 256
        self.groundX = 0
        self.score = 0
        self.angle = 0
        self.birdspin = 0
        self.live = False
        self.die = True
        self.start = False
        self.icon = pygame.image.load('assets\Image\icon1.png')
        self.background = pygame.image.load('assets\Image\Background.png')
        self.bird = [pygame.image.load('assets\Image\yellowbird_downflap.png'),
                     pygame.image.load('assets\Image\yellowbird_midflap.png'),
                     pygame.image.load('assets\Image\yellowbird_upflap.png')]
        self.gameover = pygame.image.load('assets\Image\gameover.png')
        self.startpage = pygame.image.load('assets\Image\start.png')
        self.ground = pygame.image.load('assets\Image\Ground.png')
        self.pipe = pygame.image.load('assets\Image\pipe.png')
        self.scoreImage = [pygame.image.load('assets/Image/0.png').convert_alpha(),
                           pygame.image.load('assets/Image/1.png').convert_alpha(),
                           pygame.image.load('assets/Image/2.png').convert_alpha(),
                           pygame.image.load('assets/Image/3.png').convert_alpha(),
                           pygame.image.load('assets/Image/4.png').convert_alpha(),
                           pygame.image.load('assets/Image/5.png').convert_alpha(),
                           pygame.image.load('assets/Image/6.png').convert_alpha(),
                           pygame.image.load('assets/Image/7.png').convert_alpha(),
                           pygame.image.load('assets/Image/8.png').convert_alpha(),
                           pygame.image.load('assets/Image/9.png').convert_alpha()]
        self.pipeup = pygame.transform.flip(self.pipe,False,True)
        pygame.display.set_caption("Flappy Bird")
        pygame.display.set_icon(self.icon)
    def restart(self):
        self.pipeX = 288
        self.birdY = 256
        self.score = 0
        self.live = False
        self.die = True
        self.start = False
    def flap(self):
        if self.jump and self.live:
            self.jumpspeed -= 1
            self.birdY -= self.jumpspeed
            self.jump-=1
            if self.angle < 30:
                self.angle +=3
        elif self.start:
            if not(self.live):
                self.birdY += self.down
                self.down += 0.025
            self.birdY += self.down
            self.down += 0.2
            if self.angle > -98:
                self.angle -= 8

    def pipe_move(self):
        if self.pipeY == 0 and self.live:
            self.pipeY = random.randrange(192,321)
        if self.pipeX > 0 and self.live:
            self.pipeX -= 3
        if self.pipeX <= 0 and self.live:
            self.pipeX = 288
            self.pipeY = 0
        if self.pipeX <= 84 and (self.pipeY-15 < self.birdY  or self.pipeY-120+15 > self.birdY):
            self.live = False
    def showscore(self,score,width):
        if score<10 and self.start:
            if score == 0:
                self.screen.blit(self.scoreImage[0], (144 - self.scoreImage[0].get_width()/2+width, 50))
            elif score == 1:
                self.screen.blit(self.scoreImage[1], (144 - self.scoreImage[1].get_width()/2+width, 50))
            elif score == 2:
                self.screen.blit(self.scoreImage[2], (144 - self.scoreImage[2].get_width()/2+width, 50))
            elif score == 3:
                self.screen.blit(self.scoreImage[3], (144 - self.scoreImage[3].get_width()/2+width, 50))
            elif score == 4:
                self.screen.blit(self.scoreImage[4], (144 - self.scoreImage[4].get_width()/2+width, 50))
            elif score == 5:
                self.screen.blit(self.scoreImage[5], (144 - self.scoreImage[5].get_width()/2+width, 50))
            elif score == 6:
                self.screen.blit(self.scoreImage[6], (144 - self.scoreImage[6].get_width()/2+width, 50))
            elif score == 7:
                self.screen.blit(self.scoreImage[7], (144 - self.scoreImage[7].get_width()/2+width, 50))
            elif score == 8:
                self.screen.blit(self.scoreImage[8], (144 - self.scoreImage[8].get_width()/2+width, 50))
            elif score == 9:
                self.screen.blit(self.scoreImage[9], (144 - self.scoreImage[9].get_width()/2+width, 50))

    def scoreup(self):#999까지
        if self.pipeX == 51 and self.live:
            self.score += 10
        if self.score<10:
            self.showscore(self.score,0)
        elif self.score<100:
            score = str(self.score)
            self.showscore(int(score[0]),-12)
            self.showscore(int(score[1]),12)
        elif self.score<1000:
            score = str(self.score)
            self.showscore(int(score[0]),-25)
            self.showscore(int(score[1]),0)
            self.showscore(int(score[2]),25)
    def show(self):
        self.flap()
        self.pipe_move()
        self.birdScript+=1
        if self.birdScript>2:
            self.birdScript = 0
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.pipe,(self.pipeX,self.pipeY))
        self.screen.blit(self.pipeup,(self.pipeX+self.pipe.get_width() / 2 - self.pipeup.get_width() / 2,
                                      self.pipeY-430+ self.pipe.get_height() / 2 - self.pipeup.get_height() / 2))
        if self.birdY > 400:
            if self.die:
                self.die = False
            self.screen.blit(self.gameover,(48,114))
            self.live = False
        if self.groundX == -48:
            self.groundX = 0
        elif self.live:
            self.groundX -= 4
        if not(self.start):
            self.screen.blit(self.startpage,(50,66.5))
        self.scoreup()
        self.screen.blit(self.ground,(self.groundX,400))
        if self.start:
            self.birdspin = pygame.transform.rotate(self.bird[self.birdScript], self.angle)
            self.screen.blit(self.birdspin, (50, self.birdY))

    def main(self):
        clock = pygame.time.Clock()
        pygame.font.init()
        while True:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if not(self.start):
                        self.start = True
                        self.live = True
                    self.jump = 17
                    self.down = 5
                    self.jumpspeed = 10
                    self.angle = 0
                    if self.start and not(self.live) and not(self.die):

                        Flappybird.restart(self)

            Flappybird.show(self)
            pygame.display.flip()

if __name__ == "__main__":
    Flappybird().main()
