# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 23:18:26 2019

@author: lenovo
"""
import random

class Agent:
    
    def __init__(self,environment,neighbourhood, x, y):
        self.x = random.randint(0, 100)
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
        self.y = random.randint(0, 100)
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y
#        self.agents = agents
        self.environment = environment
        self.store = 0
        
    
    def __str__(self):
        return "store=" +str(self.store)+ ", x=" + str(self.x) + ", y=" + str(self.y)
    
    def move(self):
        # dsfdfdfdsfdsfdsfdsfds
        if random.random() < 0.5:
            self.x = (self.x + 1)%300
        else:
            self.x = (self.x - 1)%300
        if random.random() < 0.5:
            self.y = (self.y + 1)%300
        else:
            self.y = (self.y - 1)%300
            
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 50:
            self.environment[self.y][self.x] -= 50
            self.store += 50
            
    def distance_between(self, agents_row_b):
        return (((self.x - agents_row_b.x)**2) +
                ((self.y - agents_row_b.y)**2))**0.5
        
    def share_with_neighbours(self, neighbor):  
        if self.distance_between(neighbor)< neighbourhood:
            avg = (neighbor.store+self.store)/2
            neighbor.store = avg
            self.store = avg
            