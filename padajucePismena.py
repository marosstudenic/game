#import
import tkinter
import string
import random
import time

#definitions
class Pismeno:
    run = True
    count = 0
    
    def __init__(self,canvas, root):
        self.can = canvas
        self.root = root
        self.width = root.winfo_screenwidth()-80
        self.height = root.winfo_screenheight()-150
        self.text = random.choice(string.ascii_lowercase)
        self.x = random.randint(10,self.width)
        self.id = self.can.create_text(self.x, 0,text = self.text.upper(),font=("sans serif", 32))
        
        self.move()

    def move(self):
        if Pismeno.run:
            
            if self.can.coords(self.id)[1]<self.height and Pismeno.run:
                self.can.move(self.id, 0,10+Pismeno.count//5)
                self.can.after(50, self.move)
            else:
                Pismeno.run = False
        else:
            self.can.delete('all')
            self.can.create_text(self.width//2, self.height//2, text = "Game Over", font=("Purisa", 50))
            self.can.create_text(self.width//2,self.height//2+50, text = str(Score.score), font = "Purisa 20")

    def check(self, st):
        if self.text == st:
            self.can.delete(self.id)
            return True
        return False

class Score:
    score =0
    def __init__(self,canvas):
        
        self.canvas = canvas
        self.scoreText = canvas.create_text(20,20,text = Score.score, font='Georgia 30')
    def redraw(self, plus):
        Score.score+=plus
        self.canvas.delete(self.scoreText)
        self.scoreText = canvas.create_text(20,20,text = Score.score, font='Georgia 30')

def start():
    Pismeno.run = False
    
    pismena = []
    canvas.delete('all')
    Score.score = 0    
    Pismeno.run = True
    print(pismena)
    
    generator()
    


def generator():
    Pismeno.count += 1
    
    
    if Pismeno.run:
        pismena.append(Pismeno(canvas,root))
        canvas.after(1000, generator)
    else:
        return
    

def keyPressed(event):
    
    popp = []
    key = event.keysym
    print(key, "key")
    if key == 'space':
        start()
    
    for i in range(len(pismena)):
        if pismena[i].check(key):
            popp.append(i) 
    if len(popp)==0 and key!='space':
        Pismeno.run = False

    popp.reverse()
    sc.redraw(len(popp))
   

    for i in popp:
        pismena.pop(i)


    


#code

#inicialization
root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()-150
pismena = []
# canvas = tkinter.Canvas(root, height = height, width = width)
canvas = tkinter.Canvas(height = height, width = width)
canvas.pack()
# button = tkinter.Button(root,text='Start', command=generator) 


sc = Score(canvas)
button = tkinter.Button(text='Start', command=start)
button.pack(side='left') 

root.bind_all('<KeyPress>', keyPressed)

#variables








canvas.mainloop()
# root.mainloop()



