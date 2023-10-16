#!/usr/bin/env Python
# -*- coding: utf-8 -*-

import tkinter

class Voiture:
    def __init__(self, Canvas):
        Canvas.create_rectangle(100, 500, 700, 580, fill = '#9354ba', outline = '#9354ba')
        Canvas.create_rectangle(100, 400, 600, 580, fill = '#9354ba', outline = '#9354ba')
        Canvas.create_oval(200,600,300,500, fill = '#000000')
        Canvas.create_oval(210,590,290,510, fill='#292727')
        Canvas.create_oval(500,600,600,500, fill='#000000')
        Canvas.create_oval(510,590,590,510, fill='#292727')
        
fenetre = tkinter.Tk()
fenetre.title('Animation')
zone_graphique = tkinter.Canvas(fenetre, width = 1920, height = 1080, bg = 'white')
zone_graphique.pack()

draw = Voiture(zone_graphique)

fenetre.mainloop()