# -*- coding: utf-8 -*-

from collections import deque
def p(s):
    print(s)
    
class MRC:
    def __init__(self, tire = 'asphalte'):
        self.tire_type = tire
        self.dices_max = 5
        self.degat = 0
        self.gaz_max = 2
        self.crevaison = 0
        self.retrogade = False
                  
    def degats(self, nb):
        self.degat += nb

    
    def crevaison(self):
        self.crevaison += 1
    
    def nb_dices(self, road_type):
        if self.tire_type == 'asphalte':
            if road_type == 'asphalte':
                return 5-self.degat, 2-self.crevaison
                

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
        elif self.type == 'dirt_turn': #avec stright après
            # -1: on arrive de l'extérieur
            if pos_on_tile == -1:
                return [0,1]
            elif pos_on_tile == 0:
                # 0 corde la prochaine case sort
                return [5,2]
            elif pos_on_tile == 1:
                # 1 première partie du virage dérapé
                return [0,2]
            elif pos_on_tile == 2:
                # 2 deuxième partie du virage dérapé
                return [5,3]
            elif pos_on_tile == 3:
                # 3ème partie du virage dérapé: on sort après
                return [-1]
            elif pos_on_tile == 5:
                return [-1]
        elif self.type == 'k_turn':
            # -1: on arrive de l'extérieur
            if pos_on_tile == -1:
                return [0,1,9]
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
            elif pos_on_tile == 9:
             #corde
                return [-1]
        elif self.type == 'sk_turn_after': #avec stright après
            # -1: on arrive de l'extérieur
            if pos_on_tile == -1:
                return [0,1,9]
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
            elif pos_on_tile == 9:
                 #corde spéciale
                return [-2]
        elif self.type == 'sk_turn_bfr': #avec stright avant
            # -1: on arrive de l'extérieur
            if pos_on_tile == -1:
                return [5,9]
            elif pos_on_tile == 5:
                # 0 corde la prochaine case sort
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
            elif pos_on_tile == 9:
                return [-1]
        elif self.type == 'dk_turn': #avec stright avant après
            # -1: on arrive de l'extérieur
            if pos_on_tile == -1:
                return [5,9]
            elif pos_on_tile == 5:
                # 0 corde la prochaine case sort
                return [0,1]
            elif pos_on_tile == 0:
                # 0 corde la prochaine case sort
                return [6]
            elif pos_on_tile == 1:
                # 1 première partie du virage dérapé
                return [0,2]
            elif pos_on_tile == 2:
                # 2 deuxième partie du virage dérapé
                return [0,3]
            elif pos_on_tile == 3:
                # 3ème partie du virage dérapé: on sort après
                return [6]
            elif pos_on_tile == 6:
                # straight après
                return [-1]
            elif pos_on_tile == 9:
                return [-1]
        
        elif self.type == 'straight':
            if pos_on_tile == -1:
                return [0]
            elif pos_on_tile == 0:
                return [-1]
        elif self.type == 'long_turn':
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
                return [0,4]
            elif pos_on_tile == 4:
                # 3ème partie du virage dérapé: on sort après
                return [-1]
        elif self.type == 'straight':
            if pos_on_tile == -1:
                return [0]
            elif pos_on_tile == 0:
                return [-1]
        elif self.type == 'short_turn':
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
                # 2 deuxième partie du virage dérapé on sort tout de suite
                return [-1] 
        elif self.type == 'bump':
            if pos_on_tile == -1:
                return [0]
            elif pos_on_tile == 0:
                return [-1]                
        else:
            return [-5]
    def get_max_gear(self, pos_on_tile):
        if self.type == 'straight':
            return 10
        elif 'k_turn' in self.type:
            if pos_on_tile == 0: #corde
                return self.max_gears[0]
            elif pos_on_tile == 9:
                return self.max_gears[2]
            elif pos_on_tile == 5:
                return 10
            else:  #dérapage
                return self.max_gears[1]
            
        elif 'turn' in self.type:
            if pos_on_tile == 0: #corde
                return self.max_gears[0]
            else:  #dérapage
                return self.max_gears[1]
        elif self.type == 'bump':
            return self.max_gears[0]
        else:
            p("Troubles w/h max_gear")
            return -50
    def get_min_gear(self, pos_on_tile):
        if 'turn' in self.type:
            if pos_on_tile in [1,2,3,4]:
                return self.max_gears[1]
        return 0
    def inspect(self):
        print(self.type + ';' + str(self.max_gears))


Straight = Tile('straight')
Bump4 = Tile('bump', [4])
Bump3 = Tile('bump', [3])
STurn4 = Tile('short_turn', [4,5])
STurn3 = Tile('short_turn', [3,4])
DirtTurn3 = Tile('dirt_turn', [3,4])
STurn2 = Tile('short_turn', [2,3])
STurn1 = Tile('short_turn', [1,2])
KTurn3 = Tile('k_turn', [3,4,4])
KTurn2 = Tile('k_turn', [2,3,3])
KTurn1 = Tile('k_turn', [1,2,2])
SKBTurn3 = Tile('sk_turn_bfr', [3,4,4])
SKATurn3 = Tile('sk_turn_after', [3,4,4])
DKTurn1 = Tile('dk_turn', [1,2,2])
Turn4 = Tile('turn', [4,5])
Turn3 = Tile('turn', [3,4])
Turn2 = Tile('turn', [2,3])
Turn1 = Tile('turn', [1,2])
LTurn1 = Tile('long_turn', [1,2])          
        
class Road:
    def __init__(self):
        self.tiles = []
        
    def append(self, tile)   :
        self.tiles.append(tile)
    
    def add_s(self, num):
        for i in range(num):
            self.tiles.append(Straight)
    
    def what_next(self, tile, pos_on_tile):
        if tile >= len(self.tiles): # this is the last tile
            return [-10,-10]
        
        nxt = self.tiles[tile].next_pos_on_tile(pos_on_tile)
        if nxt == [-1]: # next tile
            pot_l = self.tiles[tile+1].next_pos_on_tile(-1)
            ret = []
            for pot in pot_l:
                ret.append([1,pot])
            return ret
        elif nxt == [-2]: #jump over a tile
            pot_l = self.tiles[tile+2].next_pos_on_tile(-1)
            ret = []
            for pot in pot_l:
                ret.append([2,pot])
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
    def __init__(self,road, mrc = MRC()):
        self.double_low = False
        self.last_dice = -1
        self.road = road
        self.mrc = mrc
        self.move = 0
        self.time = 0
        self.tile_position = -1
        self.pos_on_tile = 0
        self.dices = [1,2,3,4,5]
        d, g = 5 , 2
        self.nb_dices = d
        self.gaz = g
        self.actual_speed = 0
        self.father = None 
        self.successors = []
        self.finish = False
        self.passed = False
        self.nb_seconds_win = 0
    
    def h_state(self):
        #paramètres différentiateurs
        return str([self.time, self.tile_position, self.pos_on_tile, self.dices,  
                self.gaz, self.actual_speed])
            
    
    def auth_dices(self):
        gears = []        
        if self.double_low:
            minus = 2
        else:
            minus = 1
            
        if self.nb_dices > 0:
            gears = [f for f in self.dices if 
                f >= self.actual_speed-minus and 
                f <= self.actual_speed +1]
        

        if self.actual_speed != 0:
            if self.gaz > 0:            
                gears.append(0)
        return gears
            
    def next_state(self, dice, move):
        # check if dice is valid
        tile, pot = move
#        p("next_state")
#        p(tile)
#        p(pot)
        
        max_auth = self.road.tiles[self.tile_position+tile].get_max_gear(pot)
        if dice > max_auth:
            return None
        if dice == 0 and self.actual_speed > max_auth:
            return None

        min_auth = self.road.tiles[self.tile_position+tile].get_min_gear(pot)
        if dice < min_auth:
            return None
        if dice == 0 and self.actual_speed < min_auth:
            return None
             
        # bump ?
        if self.road.tiles[self.tile_position].type == 'bump' and self.actual_speed == self.road.tiles[self.tile_position].get_max_gear(self.pos_on_tile):
            tile += 1
        
        ns = State(self.road)
        if self.last_dice != -1:
            ns.nb_seconds_win = self.nb_seconds_win + 1
        else:
            ns.nb_seconds_win = self.nb_seconds_win
        ns.tile_position = self.tile_position + tile
        ns.time = self.time
        ns.move = self.move + 1
        ns.pos_on_tile = pot        
        ns.dices = list(self.dices)
        if dice == 0: #gaz           
            ns.gaz = self.gaz - 1
            ns.last_dice = 0
            ns.actual_speed= self.actual_speed
        else:
            ns.gaz = self.gaz
            ns.nb_dices = self.nb_dices - 1
            ns.last_dice = dice    
            ns.dices.remove(dice)
            ns.actual_speed = dice
        return ns
    
    def must_stop(self):
        return ((len(self.dices) == 0 or self.nb_dices == 0) and self.gaz == 0)
    
    def next_state_stop(self):
        ns = State(self.road)
        ns.tile_position = self.tile_position
        ns.pos_on_tile = self.pos_on_tile
        ns.move = self.move + 1       
#          ns.dices = [1,2,3,4,5]
#        ns.gaz = 1
        ns.last_dice = -1
        ns.nb_seconds_win = self.nb_seconds_win
        ns.father = self
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
        self.passed = True
        if self.tile_position >= len(self.road.tiles)-1:
            if self.last_dice != -1:            
                ns = self.next_state_stop()
                ns.last_dice = -1   
                ns.finish = True
                ns.father = self
                
                self.successors.append(ns)
                return self.successors
            else:
                return None
        auth_dices = self.auth_dices()
        moves = self.road.what_next(self.tile_position,
            self.pos_on_tile)
        for d in auth_dices:
            for m in moves:
                n = self.next_state(d,m)
                if n != None:                
                    n.father = self
                    self.successors.append(n)
        # add stop
        if self.actual_speed != 0 and self.last_dice != -1:
            self.successors.append(self.next_state_stop())             
        return self.successors
    
    def trace_moves(self):
        r = self        
        while r != None:
            p("Move " + str(r.move) + ':' + str(r.time) + 's. ' + str(r.last_dice) + ' ' + str(id(r)))  
            r = r.father
         
    def inspect(self):
        p("Move " + str(self.move) + ':' + str(self.time) + 's. -' + str(self.nb_seconds_win) + ' ' + str(self.last_dice))   
        p('position ' + str(self.tile_position) + ' on_tile ' + str(self.pos_on_tile))         
        p(str(self.dices) + ' gaz:' + str(self.gaz) + ' speed:' 
            + str(self.actual_speed) +  'nb_d:' + str(self.nb_dices)  + ' Finish ' + str(self.finish))

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
        

p("Test")
fr = Road()

#fr.append(Straight)
game_no = 1524
if game_no == -1:
    fr.add_s(4)    
    fr.append(STurn3)  
    fr.add_s(2)    
if game_no == 1524:
    fr.append(Turn4)
    fr.add_s(2)
    fr.append(DKTurn1)
    fr.add_s(2)    
    fr.append(Turn4)    
    fr.add_s(1)
    fr.append(Turn3)
    fr.add_s(6)
    fr.append(STurn4)

    
if game_no == 1536:
    #270 s dans ce cas
    # 270s avec l'erreur
    # 280s avec une erreur de gaz qui manque dès le 1er coup
#    fr.add_s(2)
#    fr.append(KTurn2)
#    fr.add_s(3)
#    fr.add_s(1)
#    fr.append(SKATurn3)
#    fr.add_s(2)
#    fr.append(KTurn3)
#    fr.add_s(3)
#    fr.append(Tile('k_turn', [2,3,4]))
    fr.add_s(3)
    fr.append(KTurn2)
    fr.add_s(2)    
    fr.append(STurn3)    
    fr.append(STurn3)
    fr.add_s(2)
    fr.append(Turn2)
    fr.add_s(2)
    fr.append(Turn1)
    fr.add_s(3)
    fr.append(Turn1)
    fr.add_s(9)  
    fr.append(Turn1)
    fr.add_s(3)
    fr.append(Turn1)
    fr.add_s(5)
    fr.append(Turn4)
    fr.add_s(3)  
    fr.append(Turn1)  
    fr.append(Turn1)     
    fr.add_s(3)  
    fr.append(KTurn3)
    fr.add_s(2)
    fr.append(Turn4)
    fr.add_s(1)
if game_no == 1525 or game_no == 1537:
    #210 s dans ce cas
    fr.append(Turn4)
    fr.append(Straight)
    fr.append(DKTurn1)    
    fr.append(Straight)
    fr.append(Turn4)
    fr.append(Turn4)
    fr.add_s(2)
    fr.append(Turn3)
    fr.add_s(1)
    fr.append(Turn2)
    fr.add_s(2)
    fr.append(KTurn2)
    fr.add_s(3)
    fr.append(Turn4)
    fr.add_s(4)    
    fr.append(Turn2)
    fr.add_s(2)
    fr.append(KTurn3)
    fr.add_s(3)
    fr.append(KTurn2)
    fr.add_s(2)
    fr.append(Turn2)
    fr.add_s(2)  
    fr.append(Turn1)
    fr.add_s(3)
    fr.append(Turn1)
    fr.add_s(9)
    fr.append(STurn4)
    fr.add_s(3)     

if game_no == 1523:
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn1)
    fr.append(Straight)
    fr.append(Turn3)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(KTurn3)
    fr.append(Straight)
 #   fr.append(Straight) #weird K..
    fr.append(SKBTurn3)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(KTurn2)  
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn1)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn1)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn2)
    fr.append(Straight)
    fr.append(Straight)
if game_no == 515:
    fr.append(Straight)
    fr.append(Turn2)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn1)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn1)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(KTurn2)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(SKATurn3)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(KTurn3)  
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn3)
    fr.append(Straight)
    fr.append(Turn1)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
if game_no == 1522:
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Bump4)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(KTurn2)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Turn2)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Turn1)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(KTurn1)
#    fr.append(Straight)
#    fr.append(KTurn1)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Turn2)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Straight)   
    fr.append(KTurn2)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(SKATurn3)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(KTurn3)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn4)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(KTurn3)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn1)
    fr.append(Turn1)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn4)    
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn1)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn1)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)

if game_no == 539:
    fr.append(Turn1)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn2)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn3)
    fr.append(Straight)
    fr.append(STurn3)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Bump4)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn1)
    fr.append(Straight)
elif game_no == 709:
    fr.append(Turn2)
    fr.append(Straight)
    fr.append(Turn2)
    fr.append(Straight)
    fr.append(Straight)
elif game_no == 553:
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Turn3)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Turn3)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(STurn4)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Turn4)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(STurn3)
#    fr.append(STurn3)    
#    fr.append(Straight)
#    fr.append(Straight)
    fr.append(STurn1)
    fr.append(STurn1)    
    fr.append(STurn1)
    fr.append(STurn1)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(STurn4)
    fr.append(STurn4)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)  
    fr.append(STurn1)
    fr.append(STurn1)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(STurn1)
    fr.append(STurn1)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
elif game_no == 550:
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn3)
    fr.append(Straight)
    fr.append(Turn1)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Turn3)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Bump3)
    fr.append(Straight)
    fr.append(Straight)
elif game_no == 551:
#    fr.append(STurn2)
#    fr.append(STurn2)
#    fr.append(Straight)
    fr.append(Straight)
    fr.append(LTurn1)
    fr.append(Straight)
    fr.append(Turn1)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(STurn1)
    fr.append(STurn1)    
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(STurn2)
    fr.append(STurn2)    
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)
    fr.append(STurn2)
    fr.append(STurn2)    
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Bump4) # simulation bump
    fr.append(Straight)
    fr.append(Straight)
elif game_no == 1489:
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Bump4)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Turn1)    
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Turn2)
#    fr.append(Straight)    
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Bump4)
#    fr.append(Straight)    
#    fr.append(Straight)
#    fr.append(Bump4)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(Turn2)
#    fr.append(Straight)
#    fr.append(Turn1)
#    fr.append(Straight)
#    fr.append(Turn1)
#    fr.append(Straight)    
#    fr.append(STurn2)
#    fr.append(STurn2)
#    fr.append(Straight)
#    fr.append(Straight)
#    fr.append(STurn2)
#    fr.append(Straight)    
#    fr.append(Straight)
#    fr.append(Straight)
    fr.append(Turn1)
    fr.append(Straight)
    fr.append(Turn1)
    fr.append(Straight)    
    fr.append(Turn1)
    fr.append(Straight)
    fr.append(Straight) # simulation bump
    fr.append(Straight)
    fr.append(Straight)
    fr.append(Straight)


fr.inspect()
start = State(fr)
start.actual_speed = 0
p("start")
start.inspect()
#suc = start.find_successors()
#p("1st")
#for s in suc:
#    s.inspect()
#    s2 = s.find_successors()
#    for p2 in s2:
#        p("2nd")        
#        p2.inspect()
#        s3 = p2.find_successors()        
#        for p3 in s3:   
#            p("3rd")
#            p3.inspect()

histo = [0] * 50
interesting = []

def parcours_brace(root):
    ret = {}
    sl = root.find_successors()
    if root.last_dice != -1:
        ret = '(' + str(root.last_dice) + ' '
    else:
        ret = '(' + str(root.time)
    if root.move > 20:
        return "overdose"
    if sl != None:
        for st in sl:
            ret = ret + ',' + parcours_brace(st)   

    ret = ret + ')'
    return ret

def parcours_dot(root):
    nodes = ""
    if root.last_dice != -1:
        ret = str(root.last_dice) + str(root.tile_position) +str(root.pos_on_tile)
    else:
        ret =  str(root.time)
    if root.move > 20:
        return ""  
    nodes = nodes + 'u' + str(id(root)) + '[label=' + ret + '] \n'     
    nodes = nodes + 'u' + str(id(root)) + '-- {' 
    if root.successors != None:
        for st in root.successors:
           nodes = nodes + 'u' + str(id(st)) + ';' 
        nodes = nodes + "}\n"  
        for st in root.successors:
            nodes = nodes +parcours_dot(st)
    return nodes

def up_dot(leaf):
    if leaf.father == None:
        labels = ""
        if leaf.passed == True:
            if leaf.last_dice != -1:
                ret = str(leaf.last_dice) + str(leaf.tile_position) +str(leaf.pos_on_tile)
            else:
                ret =  str(leaf.time)
            labels = 'u' + str(id(leaf)) + '[label=' + ret + '] \n'  
            leaf.passed = False
        return labels, 'u' + str(id(leaf)) +';\n'   
    else:
        labels = ""
        if leaf.passed == True:
            if leaf.last_dice != -1:
                ret = str(leaf.last_dice) + str(leaf.tile_position) +str(leaf.pos_on_tile)
            else:
                ret =  str(leaf.time)
            labels = 'u' + str(id(leaf)) + '[label=' + ret + '] \n'  
            leaf.passed = False
        ups = up_dot(leaf.father)
        return labels + ups[0] ,   'u' + str(id(leaf)) + "--" + ups[1]
        
    
def parcours_dot_sons(sons):    
    label = ""
    ret = ""    
    for son in sons:
        r = up_dot(son)
        label += r[0]
        ret += r[1]
    return label + ret
            

def find_min(root, interesting_time = -1):
    if root.successors == []:
        if root.finish == True:
            if (root.time == interesting_time):
                interesting.append(root)
            histo[int(root.time/10)] += 1
            return root.time, root
        else:
            return 1000000, None
    else:
        min = 100000000
        for st in root.successors:
            min_s, st_l = find_min(st, interesting_time) 
            if min_s <= min:
                min = min_s
                ret = st_l
        return min, ret
    
def nb_leaves(root):
    if root.successors == []:
        return 1
    else:
        ret = 0
        for st in root.successors:
            ret = ret + nb_leaves(st)
        return ret

def reduce_fifo(fifo, max_time):
    ret = deque() 
    min_ref = 100000
    fifo = list(fifo)
    for s in fifo:
        if s.time < min_ref:
            min_ref = s.time
    p(min_ref)
    min_supress = min_ref + max_time   
    for s in fifo:
        if s.time <= min_supress:
            ret.append(s)
    return ret
            

min_tile = [10000] * 100

histo_tile = [0] * 10

tile_time = [1000] * 100
tile_number = [0] * 100 

hash_state = {}

def parcours_tile(node, road):
    nb_tiles = len(road.tiles)
    hash_state[node.h_state()] = True
    node.find_successors()
    fifo = deque()
    next_fifo = deque()
    for s in node.successors:
        fifo.append(s)
    for pos in range(nb_tiles):
        histo_tile = [0] * 40
        count = 0
        next_fifo = deque()
        if  road.tiles[pos].type == 'straight' and pos >= 2:
            p("reduce!")
            fifo = reduce_fifo(fifo, 110)
            p(len(fifo))
        while len(fifo) > 0:
            cur = fifo.popleft() 
            count += 1
            if cur.tile_position > pos:
                #p(int(cur.time/10))
                #histo_tile[int(cur.time/10)] += 1
                next_fifo.append(cur)
            else:
                if min_tile[pos] > cur.time:
                    min_tile[pos] = cur.time   
                if cur.passed == False:
                    if cur.h_state() not in hash_state:
                        hash_state[cur.h_state()] =  cur
                        cur.find_successors()
                        cur.passed = True
                        for lower in cur.successors:
                            fifo.append(lower)  
                    else:
#                        p('########already hashed###########')
#                        cur.inspect()
#                        p id(cur)
#                        hash_state[cur.h_state()].inspect()
#                        p id( hash_state[cur.h_state()])
#                        input()
                        cur.successors = []
                        cur.passed = True
                else:
                    p('passed')
        print('Tile ' + str(pos) + ' finished. Next: ' + str(len(next_fifo)) )
        print('hash_len ' + str(len(hash_state)) )
        print(str(count))
        p(histo_tile)
        fifo  = next_fifo


def parcours_largeur(node, max = 1000):
    fifo = []
    fifo.append(node)
    cur_move = node.move
    while len(fifo) > 0:
        cur = fifo.pop(0)
        if cur.time < min_tile[cur.tile_position]:
            min_tile[cur.tile_position] = cur.time
        if cur.move > cur_move:
            cur_move = cur.move
            p("##########Cur move: " + str(cur_move) + ' ' + str(1+len(fifo)))
            if (len(fifo) > 100000): #reduce !!!
                p("reduce!")
                fifo = reduce_fifo(fifo, 100)
                p(len(fifo))
        if cur.move < max:
            cur.find_successors()
            for lower in cur.successors:
                fifo.append(lower)




#print(parcours_brace(start))

#parcours_largeur(start)
parcours_tile(start, fr)

p(min_tile)
print("start min finding")
print(nb_leaves(start))
min, min_l = find_min(start)
min, min_l = find_min(start, min)
p(min_l)
p(min)
f = min_l
while f != None:
    f.inspect()
    f = f.father
    
p(histo)

for r in interesting:
    p("NEW")
    p(id(r))
    r.trace_moves()
p(str(len(interesting))+' interesting moves')

for r in interesting:
    r.inspect()

#dot = parcours_dot(start)
dot = parcours_dot_sons(interesting)

f = open("test.dot", "w")  
f.write( " graph  {" + dot + "}" )       
f.close()
