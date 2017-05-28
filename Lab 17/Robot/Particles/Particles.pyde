from random import randint
class particle:
    def __init__(self, x, y, v_x, v_y, a, b):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.a = a
        self.b = b

class a:
    def __init__(self):
        self.lst = []
    
def setup():
    size(800, 800)

b = a()
for i in range(50):
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
        item.x += item.v_x
        item.y += item.v_y
    

    
 
 
    