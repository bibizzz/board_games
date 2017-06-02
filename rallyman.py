# -*- coding: utf-8 -*-
class Tile:
    def __init__(self, type = 'straight', max_gears = []):
        self.max_gears = max_gears
        self.type = type
    
    def next_pos_on_tile(self, pos_on_tile):
        if self.type == 'turn':
            # -1: on arrive de l'extérieur
            if pos_on_tile == -1:
                return [0,1]
            elif pos_on_tile == 0:
                # 0 corde la prochaine case sort
                return [-1]
            elif pos_on_tile == 1:
                # 1 première partie du virage dérapé
                return[0,2]
            elif pos_on_tile == 2:
                # 2 deuxième partie du virage dérapé
                return[0,3]
            elif pos_on_tile == 3:
                # 3ème partie du virage dérapé: on sort après
                return[-1]
        elif self.type == 'straight':
            if pos_on_tile == -1:
                return [0]
            elif pos_on_tile == 0:
                return[-1]  
    def get_max_gear(self, pos_on_tile):
        if type == 'straight':
            return 10
        elif type == 'turn':
            if pos_on_tile == 0: #corde
                return self.max_gears[0]
            else:  #dérapage
                return self.max_gears[1]
                
        
class Road:
    def __init__(self):
        self.tiles = []

    def append(self, tile)   :
        self.tiles.append(tile)
    
    def what_next(self, tile, pos_on_tile):
        next_pos = self.tiles[tile].next_pos_on_tile(pos_on_tile)
        if next_pos == [-1]: # next tile
            pot_l = self.tiles[tile+1].next_pos_on_tile(-1)
            ret = []
            for pot in pot_l:
                ret.append([1,pot])
            return ret
        else: #same tile
            pot_l = self.tiles[tile].next_pos_on_tile(pos_on_tile)
            ret = []
            for pot in pot_l:
                ret.append([0,pot])
            return ret
            
            
        
class State:
    def __init__(self,road):
        self.road = Road()
        self.move = 0
        self.time = 0
        self.tile_position = 0
        self.pos_on_tile = 0
        self.time = 0
        self.dices = [1,2,3,4,5,6]
        self.gaz = 2
        self.actual_speed = 0
    
    def auth_dices(self):
        gears = [f for f in self.dices if 
            f >= self.actual_speed-1 and 
            f <= self.actual_speed +1]
        if self.actual_speed != 0:
            for d in range(self.acc):
                gears.append(0)
        return gears
            
    def next_state(self, dice, move):
        # check if dice is valid
        tile, pot = move
        max_auth = self.road.tiles[tile_position+tile].get_max_gear(pot)
        if dice > max_auth:
            return None
        
        ns = State(self.road)
        ns.tile_position = self.tile_position + tile
        ns.time = self.time
        ns.move = self.move + 1
        ns.pos_on_tile = pot
        if dice == 0: #gaz           
            ns.gaz = self.gaz - 1
            ns.dices = self.dices
            ns.actual_speed= self.actual_speed
        else:
            ns.gaz = self.gaz
            ns.dices = self.dices.remove(dice)            
            ns.actual_speed = dice
        return ns
            

class Move_tree:
    def __init__(self, road):
        self.depth = 0
        self.father = None 
        self.successors = []
        self.state = State(road)
    
    def find_successors(self):
        auth_dices = self.state.auth_dices()
        print(auth_dices)
        move = self.state.road.what_next(self.state.tile_position,
            self.state.pos_on_tile)
        print(move)

            
            


class Player:
    def __init__(self, road):
        self.state = State(road)
        


first_road = Road()

m = Move_tree(first_road)
m.find_successors()


