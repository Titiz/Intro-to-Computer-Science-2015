from random import randint
import math
class particle:
    def __init__(self, x, y, v_x, v_y, a, b):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.a = a
        self.b = b
        self.v_c = (v_x**2 + v_y**2)**(1/2) 

class a:
    def __init__(self):
        self.lst = []
    
def setup():
    size(800, 800)

b = a()
for i in range(1):
    b.lst.append(particle(randint(0, 800), randint(0, 800), randint(0,5), randint(0,5), randint(1,10), randint(1,10)))

def draw():
    
    background(0, 0, 0)
    fill(randint(0,255), randint(0, 255), randint(0, 255))
    for item in b.lst:
        if item.x > width or item.x < 0:
            item.v_x *= -1
        if item.y > height or item.y < 0:
            item.v_y *= -1
        ellipse(item.x, item.y, item.a, item.b)
        c = (item.x - mouseX)/sqrt(((item.y - mouseY)**2) + ((item.x -mouseY)**2))
        d = (item.y - mouseY)/sqrt(((item.y - mouseY)**2) + ((item.x -mouseY)**2))
        print(item.x - mouseX)
        item.v_x = item.v_c * -c
        item.v_y = item.v_c * -d
        item.x += item.v_x
        item.y += item.v_y
        
        
    

    
 
 
    