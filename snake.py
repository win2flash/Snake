#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# импортируем библиотеку pygame
import pygame
from pygame import *
 
 
class Window(object):
    def __init__(self, width, heigth, bgcolor, caption):
        self.display = (width, heigth)
        self.bgcolor = bgcolor
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode(self.display)  
 
    def drawing(self):
        self.background = Surface(self.display)
        self.background.fill(Color(self.bgcolor))
   
    def update(self):
        self.screen.blit(self.background, (0,0))
 
       
       
class Snake (object):
 
    def __init__(self, fragment_head):
        self.squares = []
        self.last_coords = []
        self.head = fragment_head
       
    def add_fragment(self, square):
        self.squares.append(square)
 
    def create_last_coords(self):
        self.last_coords = [self.head.coords()]
        for square in self.squares:
            self.last_coords.append(square.coords())
     
    def move_snake(self):
        for i in xrange(len(self.squares)):
            self.squares[i].x = self.last_coords[i][0]
            self.squares[i].y = self.last_coords[i][1]
       
    def drawing_head(self):
        self.head_surface = Surface(self.head.size)
        self.head_surface.fill(Color(self.head.color))
        self.head.curent_surface.blit(self.head_surface, (self.head.x, self.head.y))
        self.last_coords.append((self.head.x, self.head.y))
         
    def drawing_fragments(self):
        for fragment in self.squares:
            fragment.square = Surface(fragment.size)
            fragment.square.fill(Color(fragment.color))
            fragment.curent_surface.blit(fragment.square, fragment.coords())
 
       
class Square(object):
    def __init__ (self, x, y, side, color, curent_surface):
        self.side = side
        self.size = (side, side)
        self.x = x
        self.y = y
        self.color = color
        self.curent_surface = curent_surface
       
    def drawing (self):
        self.square = Surface(self.size)
        self.square.fill(Color(self.color))
        self.curent_surface.blit(self.square, (self.x, self.y))
    def coords(self):
        return (self.x, self.y)
 
     
class Head(Square):
 
    def __init__(self, x, y, side, color, curent_surface):
        Square.__init__(self, x, y, side, color, curent_surface)
        self.direction = "left"
 
    #def change_direction(self, direction):
       # self.direction = direction
        
    def move(self, direction):
        self.direction = direction
        if self.direction == "left":
            self.x -= self.side          
        elif self.direction == "right":
            self.x += self.side
        elif self.direction == "up":
            self.y -= self.side
        else:
            self.y += self.side
 
       
def main():
    pygame.init()
    window = Window(800, 640, "red", "SnakeIt")
    window.drawing()
    square = Square(332,300, 32, "white", window.screen)
    fragment = Head(300,300,32, "black", window.screen)
    snake = Snake(fragment)
    snake.add_fragment(square)
    for i in xrange(5):
        snake.add_fragment(Square(364,300, 32, "white", window.screen))
   
    while 1:
        snake.create_last_coords()
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_LEFT:
                fragment.move("left")
                snake.move_snake()
            if e.type == KEYDOWN and e.key == K_RIGHT:
                fragment.move("right")
                snake.move_snake()
            if e.type == KEYDOWN and e.key == K_UP:
                fragment.move("up")
                snake.move_snake()
            if e.type == KEYDOWN and e.key == K_DOWN:
                fragment.move("down")
                snake.move_snake()
        window.update()          
        #square.drawing()
        #fragment.drawing()
        snake.drawing_head()
        snake.drawing_fragments()
        pygame.display.update()     # обновление и вывод всех изменений на экран
       
 
if __name__ == "__main__":
    main()