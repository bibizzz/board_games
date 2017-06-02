# -*- coding: utf-8 -*-
class Tile:
    def __init__(self, max_speed):
        self.max = max_speed
        self.type = 'straight'
    
    def next_pos_on_tile(self, pos_on_tile):
        if self.type == 'turn':
            if pos_on_tile == -1:
                return [0,1]
            elif pos_on_tile == 0:
                return [-1]
            elif pos_on_tile == 1:
                return[0,2]
            elif pos_on_tile == 2:
                return[0,3]
            elif pos_on_tile == 3:
                return[-1]
        elif self.type == 'straigth':
            if pos_on_tile == -1:
                return [0]
            elif pos_on_tile == 0:
                return[-1]       

class Road:
    def __init__(self):
        self.tiles = []

    def append(self, tile)   :
        self.tiles.append(tile)
    
    def what_next(self, tile, pos_on_tile):
        next_pos = self.tiles[tile](pos_on_tile)
        if next_pos == -1:
            
        else:
            
            
            
            
        
class State:
    def __init__(self,road):
        self.road = Road()
        self.nb_moves = 0
        self.time = 0
        self.tile_position = 0
        self.pos_on_tile = 0
        self.time = 0
        self.dices = [1,2,3,4,5,6]
        self.acc = 2
        self.actual_speed = 0
    
    def auth_dices(self):
        return [f for f in self.dices if 
            f >= self.actual_speed-1 and 
            f <= self.actual_speed +1]
            
    def next_state(self, dice, pos_on_tile):
        # check if dice is valid
        # TO DO
        if dice == 0: #gaz
            self.acc -= 1
            self.tile_position += 1
            

class Move_tree:
    def __init__(self, road):
        self.depth = 0
        self.father = None 
        self.successors = []
        self.state = State(road)
    
    def find_successors(self):
        auth_dices = self.state.auth_dices()
        print(auth_dices)
        for d in auth_dices:
            s = State()            
            s.nb_moves += 1
            
            self.sucessors.append = State()
            
            


class Player:
    def __init__(self, road):
        self.state = State(road)
        


first_road = Road()

m = Move_tree(first_road)
m.find_successors()


print(first_road.pos.max)