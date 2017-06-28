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
KTurn4 = Tile('k_turn', [4,5,5])
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
    
    def from_game(self, game_no):
    #self.append(Straight)
        if game_no == 55002:
        #    self.append(Turn4)
        #    self.add_s(2)
        #    self.append(KTurn3)
        #    self.add_s(3)    
        #    self.append(Turn1)    
        #    self.append(Turn1)    
        #    self.add_s(3)
        #    self.append(Turn4)
        #    self.add_s(5)
        #    self.append(Turn1)
        #    self.add_s(3)
        #    self.append(Turn1)
        #    self.add_s(7)    
        #    self.append(Turn1)    
            self.add_s(5)
            self.append(Bump4)
            self.add_s(3)
            self.append(STurn1)
            self.append(STurn1)
            self.add_s(4)
            self.append(STurn2)
            self.append(STurn2)
            self.add_s(2)
            self.append(STurn2)
            self.append(STurn2)
            self.add_s(2)
            self.append(Turn1)
            self.add_s(1)
            self.append(Turn1)
            self.add_s(2)  
            self.append(STurn1)
            self.append(STurn1)
            self.add_s(4)
            self.append(STurn2)
            self.append(STurn2)
            self.add_s(4)
            self.append(STurn2)
            self.append(STurn2)
            self.add_s(2)  
            self.append(Bump4)     
            self.add_s(3)  
        
        
        if game_no == -1:
            self.add_s(4)    
            self.append(STurn3)  
            self.add_s(2)    
        if game_no == 1524:
            self.append(Turn4)
            self.add_s(2)
            self.append(DKTurn1)
            self.add_s(2)    
            self.append(Turn4)    
            self.add_s(1)
            self.append(Turn3)
            self.add_s(6)
            self.append(STurn4)
        
            
        if game_no == 1536:
            #270 s dans ce cas
            # 270s avec l'erreur
            # 280s avec une erreur de gaz qui manque dès le 1er coup
        #    self.add_s(2)
        #    self.append(KTurn2)
        #    self.add_s(3)
        #    self.add_s(1)
        #    self.append(SKATurn3)
        #    self.add_s(2)
        #    self.append(KTurn3)
        #    self.add_s(3)
        #    self.append(Tile('k_turn', [2,3,4]))
            self.add_s(3)
            self.append(KTurn2)
            self.add_s(2)    
            self.append(STurn3)    
            self.append(STurn3)
            self.add_s(2)
            self.append(Turn2)
            self.add_s(2)
            self.append(Turn1)
            self.add_s(3)
            self.append(Turn1)
            self.add_s(9)  
            self.append(Turn1)
            self.add_s(3)
            self.append(Turn1)
            self.add_s(5)
            self.append(Turn4)
            self.add_s(3)  
            self.append(Turn1)  
            self.append(Turn1)     
            self.add_s(3)  
            self.append(KTurn3)
            self.add_s(2)
            self.append(Turn4)
            self.add_s(1)
        if game_no == 152302 :
            self.add_s(2)
            self.append(Turn1)
            self.add_s(3)
            self.append(KTurn4)
            self.add_s(2)
            self.append(Turn4)
            self.add_s(1)
            self.append(Turn3)
            self.add_s(4)
            self.append(Bump3)
            self.add_s(3)
            self.append(STurn4)
            self.add_s(1)
            self.append(Turn4)
            self.add_s(2)
            self.append(Turn3)
            self.add_s(1)  
            self.append(Turn2)
            self.add_s(2)
            self.append(KTurn2)
            self.add_s(3)
            self.append(Turn4)
            self.add_s(4)
            self.append(Turn2)
            self.add_s(1)  
            self.append(Turn4)
            self.add_s(2)
            self.append(DKTurn1)
            self.add_s(2)
            self.append(Turn4)
            self.add_s(2) 
            self.append(KTurn2)
            self.add_s(3)
            self.append(SKATurn3)
            self.add_s(2)
            self.append(KTurn3)
            self.add_s(3)
            
        if game_no == 1525 or game_no == 1537:
            #210 s dans ce cas
            self.append(Turn4)
            self.append(Straight)
            self.append(DKTurn1)    
            self.append(Straight)
            self.append(Turn4)
            self.append(Turn4)
            self.add_s(2)
            self.append(Turn3)
            self.add_s(1)
            self.append(Turn2)
            self.add_s(2)
            self.append(KTurn2)
            self.add_s(3)
            self.append(Turn4)
            self.add_s(4)    
            self.append(Turn2)
            self.add_s(2)
            self.append(KTurn3)
            self.add_s(3)
            self.append(KTurn2)
            self.add_s(2)
            self.append(Turn2)
            self.add_s(2)  
            self.append(Turn1)
            self.add_s(3)
            self.append(Turn1)
            self.add_s(9)
            self.append(STurn4)
            self.add_s(3)     
        
        if game_no == 152301:
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn1)
            self.append(Straight)
            self.append(Turn3)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(KTurn3)
            self.append(Straight)
         #   self.append(Straight) #weird K..
            self.append(SKBTurn3)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(KTurn2)  
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn1)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn1)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn2)
            self.append(Straight)
            self.append(Straight)
        
            
        if game_no == 515:
            self.append(Straight)
            self.append(Turn2)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn1)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn1)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(KTurn2)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(SKATurn3)
            self.append(Straight)
            self.append(Straight)
            self.append(KTurn3)  
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn3)
            self.append(Straight)
            self.append(Turn1)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
        if game_no == 1522:
            self.append(Straight)
            self.append(Straight)
            self.append(Bump4)
            self.append(Straight)
            self.append(Straight)
            self.append(KTurn2)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn2)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn1)
            self.append(Straight)
            self.append(Straight)
            self.append(KTurn1)
            self.append(Straight)
            self.append(KTurn1)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn2)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)   
            self.append(KTurn2)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(SKATurn3)
            self.append(Straight)
            self.append(Straight) #Tile 6-7 : 20s
            self.append(KTurn3)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn4)
            self.append(Straight)
            self.append(Straight)
            self.append(KTurn3)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn1)
            self.append(Turn1)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn4)    
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn1)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn1)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
        
        if game_no == 539:
            self.append(Turn1)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn2)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn3)
            self.append(Straight)
            self.append(STurn3)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Bump4)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn1)
            self.append(Straight)
        elif game_no == 709:
            self.append(Turn2)
            self.append(Straight)
            self.append(Turn2)
            self.append(Straight)
            self.append(Straight)
        elif game_no == 553:
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Turn3)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Turn3)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(STurn4)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Turn4)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(STurn3)
        #    self.append(STurn3)    
        #    self.append(Straight)
        #    self.append(Straight)
            self.append(STurn1)
            self.append(STurn1)    
            self.append(STurn1)
            self.append(STurn1)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(STurn4)
            self.append(STurn4)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)  
            self.append(STurn1)
            self.append(STurn1)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(STurn1)
            self.append(STurn1)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
        elif game_no == 550:
            self.append(Straight)
            self.append(Straight)
            self.append(Turn3)
            self.append(Straight)
            self.append(Turn1)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Turn3)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
            self.append(Bump3)
            self.append(Straight)
            self.append(Straight)
        elif game_no == 551:
        #    self.append(STurn2)
        #    self.append(STurn2)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(LTurn1)
        #    self.append(Straight)
        #    self.append(Turn1)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(STurn1)
        #    self.append(STurn1)    
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(STurn2)
        #    self.append(STurn2)    
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Straight)
            self.append(Straight)
            self.append(STurn2)
            self.append(STurn2)    
            self.append(Straight)
            self.append(Straight)
            self.append(Bump4) 
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
        elif game_no == 1489:
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Bump4)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Turn1)    
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Turn2)
        #    self.append(Straight)    
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Bump4)
        #    self.append(Straight)    
        #    self.append(Straight)
        #    self.append(Bump4)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(Turn2)
        #    self.append(Straight)
        #    self.append(Turn1)
        #    self.append(Straight)
        #    self.append(Turn1)
        #    self.append(Straight)    
        #    self.append(STurn2)
        #    self.append(STurn2)
        #    self.append(Straight)
        #    self.append(Straight)
        #    self.append(STurn2)
        #    self.append(Straight)    
        #    self.append(Straight)
        #    self.append(Straight)
            self.append(Turn1)
            self.append(Straight)
            self.append(Turn1)
            self.append(Straight)    
            
            
            self.append(Turn1)
            self.append(Straight)
            self.append(Straight) # simulation bump
            self.append(Straight)
            self.append(Straight)
            self.append(Straight)
    
    def add_branch(b):
        if b == "J8-J7":
            self.append(Turn4)
            self.add_s(2)
            self.append(DKTurn1)
            self.add_s(2)    
            self.append(Turn4) 
        elif b == "C9-C0":
            self.add_s(1)
            self.append(Turn3)
            self.add_s(2)
        elif b == "V4-V1":
            self.add_s(4)
            self.append(STurn4)
            self.add_s(2)
        
    def from_road_book(s):
        #parse s
        for branch in branch_l:
            self.add_branch(branch)
    
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
                ret.append([2,pot])#parse
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

fr = Road()


#J8-J7/C9-C0/V4-V1/L6-L5/V2-V3/C1-C2/L4-L7/V0-V5/J6-J5/V6-V9/X

p("Test")
fr = Road()
game_no = 152302
fr.from_game(game_no)

         