
def setup():
    size(800,800)

class Particle:
    def __init__(self):
        self.y = 775
        self.v_y = -1
        self.d = 20
        
    def display(self):
        return ellipse(400, self.y, 50, 50)
        
    def move(self):
        self.y += self.v_y
        if self.v_y > -1:
            self.v_y -= 1
        
    def deflate(self):
        self.v_y += self.d
        self.d *= 0.97
    
def keyTyped():
    p.deflate()
    
p = Particle()

def draw():
    background(100,100,100)
    
    p.display()
    p.move()
    if p.y < -25:
        fill(255,255,255)
        textSize(64)
        text('You LOSE', 400, 400)
    
        
        