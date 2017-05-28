class Marker:
    def __init__(self, x, y, name):
        self.name = name
        self.x = x
        self.y = y

class Lst(list):
    pass
    
lst = Lst()

class Counter:
    count = 0
    
counter = Counter()

def setup():
    size(900, 900)

    
def draw():
    background(255,255,255)
    line(300, 0, 300, 900)
    line(600, 0, 600, 900)
    line(0, 300, 900, 300)
    line(0, 600, 900, 600)
    for item in lst:
        image(item.name, item.x-100, item.y-100, 200, 200)
    
def mouseClicked():
    if counter.count < 9:
        if counter.count % 2 == 0:
            lst.append(Marker(mouseX, mouseY, loadImage('x.png')))
        else:
            lst.append(Marker(mouseX, mouseY, loadImage('o.png')))
        counter.count += 1
    
               
    