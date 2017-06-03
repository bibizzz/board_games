# -*- coding: utf-8 -*-
def p(s):
    print(s)

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
                return [0,2]
            elif pos_on_tile == 2:
                # 2 deuxième partie du virage dérapé
                return [0,3]
            elif pos_on_tile == 3:
                # 3ème partie du virage dérapé: on sort après
                return [-1]
        elif self.type == 'straight':
            if pos_on_tile == -1:
                return [0]
            elif pos_on_tile == 0:
                return [-1]  
        else:
            return [-5]
    def get_max_gear(self, pos_on_tile):
        if self.type == 'straight':
            return 10
        elif self.type == 'turn':
            if pos_on_tile == 0: #corde
                return self.max_gears[0]
            else:  #dérapage
                return self.max_gears[1]
        else:
            p("Troubles w/h max_gear")
            return -50
    def inspect(self):
        print(self.type + ';' + str(self.max_gears))
                
        
class Road:
    def __init__(self):
        self.tiles = []

    def append(self, tile)   :
        self.tiles.append(tile)
    
    def what_next(self, tile, pos_on_tile):
        nxt = self.tiles[tile].next_pos_on_tile(pos_on_tile)
        if nxt == [-1]: # next tile
            pot_l = self.tiles[tile+1].next_pos_on_tile(-1)
            ret = []
            for pot in pot_l:
                ret.append([1,pot])
            return ret
        else: #same tile
            ret = []
            for pot in nxt:
                ret.append([0,pot])
            return ret
    
    def inspect(self):
        print ('Road length:' + str(len(self.tiles)))
        for tile in self.tiles:
            tile.inspect()
            
            
        
class State:
    def __init__(self,road):
        self.road = road
        self.move = 0
        self.time = 0
        self.tile_position = 0
        self.pos_on_tile = 0
        self.time = 0
        self.dices = [1,2,3,4,5,6]
        self.gaz = 2
        self.actual_speed = 0
        self.father = None 
        self.successors = []
    
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
        p(tile)
        p(pot)
        max_auth = self.road.tiles[self.tile_position+tile].get_max_gear(pot)
        p(max_auth)
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
            ns.dices = self.dices    
            ns.dices.remove(dice)
            ns.actual_speed = dice
        return ns
    
    def must_stop(self):
        return (len(self.dices) == 0 and  self.gaz == 0)
    
    def next_state_stop(self):
        ns = State(self.road)
        ns.tile_position = self.tile_position
        ns.pos_on_tile = self.pos_on_tile
        ns.move = self.move + 1       
        ns.dices = [1,2,3,4,5,6]
        ns.gaz = 2
        ns.actual_speed = self.actual_speed
        if self.actual_speed == 1:
            ns.time = self.time + 50
        elif self.actual_speed == 2:
            ns.time = self.time + 40
        elif self.actual_speed == 3:
            ns.time = self.time + 30        
        elif self.actual_speed == 4:
            ns.time = self.time + 20
        elif self.actual_speed == 5:
            ns.time = self.time + 10 
        return ns
        
    def find_successors(self):
        auth_dices = self.state.auth_dices()
        moves = self.state.road.what_next(self.state.tile_position,
            self.state.pos_on_tile)
        for d in auth_dices:
            for m in moves:
                n = self.state.next_state(d,m)
                n.father = self
                self.successors.append(n)
        # add stop
        if self.state.actual_speed != 0:
            self.successors.append(self.state.next_state_stop())             
        return self.successors
    
    def inspect(self):
        p("Inspect state:")
        p(self.move)
        p(self.time) 
        p(self.tile_position) 
        p(self.pos_on_tile)
        p(self.time) 
        p(self.dices) 
        p(self.gaz) 
        p(self.actual_speed)

class Move_leaf:
    def __init__(self, road):
        self.depth = 0
        self.father = None 
        self.successors = []
        self.state = State(road)
    
    def find_successors(self):
        auth_dices = self.state.auth_dices()
        moves = self.state.road.what_next(self.state.tile_position,
            self.state.pos_on_tile)
        for d in auth_dices:
            for m in moves:
                n = self.state.next_state(d,m)
                m = Move_leaf(self.state.road)
                m.state = n
                self.successors.append(n)
        # add stop
        if self.state.actual_speed != 0:
            self.successors.append(self.state.next_state_stop())
        

        return self.successors

        

            
class Player:
    def __init__(self, road):
        self.state = State(road)
        


fr = Road()
Straight = Tile('straight')
Turn2 = Tile('turn', [2,3])
fr.append(Straight)
fr.append(Straight)
fr.append(Straight)
fr.append(Straight)
fr.append(Turn2)
fr.append(Straight)
fr.append(Straight)
fr.append(Turn2)
fr.append(Straight)
fr.append(Straight)
fr.append(Straight)
fr.inspect()


m = Move_leaf(fr)
suc = m.find_successors()
for s in suc:
    s.inspect()


