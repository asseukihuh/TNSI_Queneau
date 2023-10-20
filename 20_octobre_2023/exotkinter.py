#!/usr/bin/env Python
# -*- coding: utf-8 -*-

import tkinter
import time

class Environnement:
    def __init__(self, Canvas):
        self.x = 100
        self.y = 150
        self.Canvas = Canvas
        self.mur = True
        
    def drawe(self):
        self.Canvas.create_rectangle(0, 700, 1500, 1000, fill = '#5e3619', outline = '#5e3619')
        self.Canvas.create_polygon(500,700, 500,500,1500,700, fill="#5e3619", outline="#5e3619")
        self.Canvas.create_rectangle(0, 500, 500, 700, fill = '#5e3619', outline = '#5e3619')
        self.Canvas.create_rectangle(1920, 700, 1500, 1000, fill = '#422008', outline = '#422008')
        self.Canvas.create_polygon(1500,700,700,1000,1500,1000, fill="#422008", outline="#422008")
        self.Canvas.create_rectangle(0, 950, 1500, 1000, fill = '#422008', outline = '#422008')
        self.Canvas.create_oval(self.x,self.y,350+self.x,350+self.y, fill='#2b2927', outline = '#2b2927')
        
    def move(self):
        if self.x < 340 and self.mur:
            self.x += 10
        
        elif self.x >= 340 and self.x < 1340 and self.mur:
            self.x += 10
            self.y += 2
            
        elif self.x >= 1340 and self.x < 1561 and self.mur:
            self.x += 10
            
        if self.x >= 1340 and self.mur == False:
            self.x -= 10
        
        elif self.x <= 1340 and self.x >= 630 and self.mur == False:
            self.x -= 10
            self.y += 3.5
            
        elif self.mur == False and self.x > -100:
            self.x -= 10
            
        if self.x > 1561:
            self.mur = False
            
            
    def reset(self):
        self.x = 100
        self.y = 150
        
            
            
def animation(zone_graphique, Environnement):
    running = True
    while running:
        zone_graphique.delete('all')
        Environnement.drawe()
        Environnement.move()
        
        zone_graphique.update()
        time.sleep(0.0001)
    
        
        
fenetre = tkinter.Tk()
fenetre.title('Animation')
zone_graphique = tkinter.Canvas(fenetre, width = 1920, height = 1000, bg = '#8fbaff')
zone_graphique.pack()


draw = Environnement(zone_graphique)
draw.drawe()

while True:
    animation(zone_graphique, draw)
    draw.reset()
    

fenetre.mainloop()