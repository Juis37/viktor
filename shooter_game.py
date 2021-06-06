#Создай собственный Шутер!

from pygame import *
from random import*
window=display.set_mode((700,500))
back = transform.scale(image.load('galaxy.jpg'),(700,500))


class Gam(sprite.Sprite):
    def __init__(self, player_image, player_x, plaer_y,s_x,s_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(s_x,s_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = plaer_y

    def recet(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


puls=sprite.Group()
class Player(Gam):
    def con(self):
        kp  = key.get_pressed()
        if kp[K_UP] and self.rect.y>=0:
            self.rect.y = self.rect.y - self.speed
            
        if kp[K_DOWN] and self.rect.y<=435:
            self.rect.y = self.rect.y + self.speed
        if kp[K_RIGHT]and self.rect.x<=635:
            self.rect.x = self.rect.x + self.speed
        if kp[K_LEFT] and self.rect.x>=0:
            self.rect.x = self.rect.x - self.speed
    def fire(self):
        
        
        pulya=pul('bullet.png',self.rect.centerx,self.rect.top,20,20,4)
        puls.add(pulya)
        
i=0       
class Mon(Gam):
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y >= 435:
            #lose
            self.rect.y=0
            self.rect.x=randint(0,635)

class pul(Gam):
    def update(self):
        self.rect.y = self.rect.y - self.speed
        if self.rect.y <= 0:
            self.kill()
    



font.init()
font = font.Font(None, 70)
w = font.render(
    'YOU W!',True,(255,215,0)
)
            


monsters=sprite.Group()
for i in range(100):
    monster=Mon('ufo.png',randint(1,635),randint(-200,0),65,65,randint(1,3))
    monsters.add(monster)







kor = Player('rocket.png',100,100,65,65,10)


cl=time.Clock()
FPS = 60

fin=False


g= True
while g:
    for e in event.get():
        if e.type == QUIT:
            g = False
    if fin != True:
        kp2= key.get_pressed()
        window.blit(back,(0,0))            
        if kp2[K_SPACE]:
            kor.fire()
        if sprite.groupcollide(monsters,puls,True,True):
            i = i+1
            monster1=Mon('ufo.png',randint(1,635),randint(-200,0),65,65,randint(1,3))
            monsters.add(monster1)


        kor.con()
        kor.recet()
        puls.draw(window)
        puls.update()
        monsters.draw(window)
        monsters.update()
        
       
        cl.tick(FPS)



    
        display.update()
