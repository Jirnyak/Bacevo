import pygame, random, sys, time, numpy, math
from pygame.locals import *

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
gray = (128,128,128)
navy = (0,0,128)
rose = (255,0,255)
green = (0,128,0)

clock = pygame.time.Clock()

class people():

    def __init__(self):

        screen = pygame.display.get_surface()
        
        self.okras = [random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)]

        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)


  
        self.wantfood = None

        self.lopal = 0

        self.health = round(numpy.random.normal(0.5, 0.1, None), 3)
        self.hp = round(self.health*1000)

    def wantfood(self, foods):

        razn = 0

        raznabs = 1000

        
        for obj in foods:

            razn = math.sqrt((self.x - obj.x)**2+(self.y - obj.y)**2)

            if razn < raznabs:

                raznabs = razn

                self.wantfood = obj
            

    def move(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)
        if self.x < 0:
            self.x = 0
        if self.x > 800:
            self.x = 800
        if self.y < 0:
            self.y = 0
        if self.y > 600:
            self.y = 600
   
    def goto(self, a, b, foodobj, foods):
        if self.x - a < 0 and self.y - b < 0:
            self.x += 1
            self.y += 1
        if self.x - a > 0 and self.y - b < 0:
            self.x -= 1
            self.y += 1
        if self.x - a > 0 and self.y - b > 0:
            self.x -= 1
            self.y -= 1
        if self.x - a < 0 and self.y - b > 0:
            self.x += 1
            self.y -= 1
        if self.x - a == 0 and self.y - b > 0:
            self.y -= 1
        if self.x - a == 0 and self.y - b < 0:
            self.y += 1
        if self.x - a < 0 and self.y - b == 0:
            self.x += 1
        if self.x - a > 0 and self.y - b == 0:
            self.x -= 1
        elif self.x == a and self.y == b:
            if foodobj in foods:
                foods.remove(foodobj)
                self.lopal = 1

        else:
            self.x += random.randint(-1, 1)
            self.y += random.randint(-1, 1)


    def place(okras, x, y,):

  

        screen = pygame.display.get_surface()

       
        pygame.draw.rect(screen, okras, [x, y, 5, 5])
        
  
          



class food():

    def __init__(self):

        screen = pygame.display.get_surface()
 
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)

        self.slopano = 0

    def place(x, y):

        screen = pygame.display.get_surface()
        
        pygame.draw.rect(screen, green, [x, y, 3, 3])

    def slopano(self, slopanolist):

        self.slopano = 1
             
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Test')

    peoples = []

    foods = []

    slopanolist = []

    foodcount = 0

    dead = []

    countdecay = 0

    naselenje = 2

   



    for i in range(naselenje):
         peoples.append(people())

    while True:

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                None 

        pygame.display.set_caption(str(len(peoples)))
        
        screen.fill(white)


        Nutrition = int(len(peoples)/10)

        for obj in peoples:
        
            people.place(obj.okras, obj.x, obj.y)

            people.move(obj)




            people.wantfood(obj, foods)
           
            if obj.wantfood != None and obj.wantfood.slopano == 1 :

                obj.wantfood = None

            if obj.wantfood != None:
                
                people.goto(obj, obj.wantfood.x,  obj.wantfood.y,  obj.wantfood, foods )

            if obj.lopal == 1:
                                    
                obj.hp = round(obj.health*1000)
                food.slopano(obj.wantfood, slopanolist)
                obj.wantfood = None

            if obj.lopal == 0:

                obj.hp -= 1

            if obj.hp == 0:

                peoples.remove(obj)
                dead.append(obj)

            if obj.lopal > 0:

                peoples.append(people())

                peoples[len(peoples)-1].x = obj.x
                peoples[len(peoples)-1].y = obj.y
                peoples[len(peoples)-1].okras = [obj.okras[0] + random.randint(-10, 10), obj.okras[1] + random.randint(-10, 10), obj.okras[2] + random.randint(-10, 10)]
                if peoples[len(peoples)-1].okras[0] > 255 or peoples[len(peoples)-1].okras[0] < 0:
                    peoples[len(peoples)-1].okras[0] = 127
                if peoples[len(peoples)-1].okras[1] > 255 or peoples[len(peoples)-1].okras[1] < 0:
                    peoples[len(peoples)-1].okras[1] = 127
                if peoples[len(peoples)-1].okras[2] > 255 or peoples[len(peoples)-1].okras[2] < 0:
                    peoples[len(peoples)-1].okras[2] = 127
                peoples[len(peoples)-1].health = round(random.uniform(obj.health-0.1, obj.health+0.1), 3)
                peoples[len(peoples)-1].hp = round(peoples[len(peoples)-1].health*1000)

                obj.lopal = 0

        foodcount += 1

        if foodcount > Nutrition:

            foods.append(food())

            foodcount = 0

        for obj in foods:

                food.place(obj.x, obj.y)
                
        for obj in slopanolist:

            del obj

        for obj in dead:
            
            
            del obj

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()

pygame.quit()
quit()

