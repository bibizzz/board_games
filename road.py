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
        elif self.type == 'dirt_straight': #avec stright après
            # -1: on arrive de l'extérieur
            if pos_on_tile == -1:
                return [0,1]
            elif pos_on_tile == 0:
                # on sort direct
                return [-1]
            elif pos_on_tile == 1:
                # 1 première partie du dérapé
                return [2]
            elif pos_on_tile == 2:
                # 2 deuxième partie du dérapé
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
        elif self.type == 'short_k_turn':
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
        elif self.type == 'cross':
            if pos_on_tile == -1:
                return [0]
            elif pos_on_tile == 0:
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
        elif self.type == 'cross':
            return self.max_gears[0]
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
            return self.max_gears[0]+1
        else:
            p("Troubles w/h max_gear")
            return -50
    def get_min_gear(self, pos_on_tile):
        if 'turn' in self.type:
            if pos_on_tile in [1,2,3,4]:
                return self.max_gears[1]
        return 0
    def inspect(self):
        return (self.type + ';' + str(self.max_gears))


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
ShortKTurn4 = Tile('short_k_turn', [4,5,5])
ShortKTurn3 = Tile('short_k_turn', [3,4,4])
ShortKTurn2 = Tile('short_k_turn', [2,3,3])
DKTurn1 = Tile('dk_turn', [1,2,2])
Turn4 = Tile('turn', [4,5])
Turn3 = Tile('turn', [3,4])
Turn2 = Tile('turn', [2,3])
Turn1 = Tile('turn', [1,2])
LTurn1 = Tile('long_turn', [1,2])  
Cross2 = Tile('cross', [2])        
        
class Road:
    def __init__(self):
        self.tiles = []
        
    def append(self, tile)   :
        self.tiles.append(tile)
    
    def append_road(self, road):
        for t in road.tiles:
            self.append(t)
        return self
    
    def invert(self):
        self.tiles = list(reversed(self.tiles))
        return self.tiles
    
    def add_s(self, num):
        for i in range(num):
            self.tiles.append(Straight)
    
    def from_game(self, game_no):
    #self.append(Straight)
        if game_no == 55002:
            #
#            self.append(Turn4)
#            self.add_s(2)
#            self.append(KTurn3)
#            self.add_s(3)    
#            self.append(Turn1)    
#            self.append(Turn1)    
#            self.add_s(3)
#            self.append(Turn4)
#            self.add_s(5)
#            self.append(Turn1)
#            self.add_s(3)
#            self.append(Turn1)
#            self.add_s(4)    
#            self.add_s(3)  
#            self.append(KTurn1)    
#            self.add_s(3)    
#            self.add_s(1)
#           self.add_s(1)
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
#            self.add_s(3)
#            self.append(KTurn2)
#            self.add_s(2)    
#            self.append(STurn3)    
#            self.append(STurn3)
#            self.add_s(2)
#            self.append(Turn2)
#            self.add_s(2)
#            self.append(Turn1)
#            self.add_s(3)
#            self.append(Turn1)
#            self.add_s(9)  
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
        # J8-J7/C1-C2/J6-J5/L8-L9/V4-V1/X
            self.append(Turn4)
            self.append(Straight)
            self.append(DKTurn1)    
            self.append(Straight)
            self.append(Turn4)
            self.append(Turn4)
            self.add_s(1)
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
#            self.append(Straight)
#            self.append(Straight)
#            self.append(Bump4)
#            self.append(Straight)
#            self.append(Straight)
#            self.append(KTurn2)
#            self.append(Straight)
#            self.append(Straight)
#            self.append(Straight)
#            self.append(Straight)
#            self.append(Turn2)
#            self.append(Straight)
#            self.append(Straight)
#            self.append(Straight)
#            self.append(Straight)
#            self.append(Turn1)
#            self.append(Straight)
#            self.append(Straight)
#            self.append(KTurn1)
#            self.append(Straight)
#            self.append(KTurn1)
#            self.append(Straight)
#            self.append(Straight)
#            self.append(Turn2)
#            self.append(Straight)
#            self.append(Straight)
#            self.append(Straight)   
#            self.append(KTurn2)
#            self.append(Straight)
#            self.append(Straight)
#            self.append(Straight)
#            self.append(SKATurn3)
#            self.append(Straight)
#            self.append(Straight) #Tile 6-7 : 20s
#            self.append(KTurn3)
#            self.append(Straight)
#            self.append(Straight)
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
#            self.append(Turn1)
#            self.append(Straight)
#            self.append(Straight)
#            self.append(Straight)
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
    
    def add_branch(self, b, invert = False):
        new_road = Road()
        if b == "J8-J7":
            new_road.append(Turn4)
            new_road.add_s(1)
            new_road.append(DKTurn1)
            new_road.add_s(1)    
            new_road.append(Turn4) 
        elif b == "J3-J2":
            new_road.add_s(1)    
            new_road.append(STurn3)       
            new_road.add_s(1)
        elif b == "L3-L2":            
            new_road.add_s(2)
            new_road.append(Bump4)
            new_road.add_s(4)    
            new_road.append(Turn1)       
            new_road.add_s(4)
            new_road.append(KTurn2)
            new_road.add_s(1)
        elif b == "J1-J4":            
            new_road.append(Turn4)
            new_road.add_s(2)
            new_road.append(KTurn3)
            new_road.add_s(3)    
            new_road.append(Turn1)    
            new_road.append(Turn1)    
            new_road.add_s(3)
            new_road.append(Turn4)
            new_road.add_s(5)
            new_road.append(Turn1)
            new_road.add_s(3)
            new_road.append(Turn1)
            new_road.add_s(4) 
        elif b == "C6-C7":            
            new_road.append(Turn2)
            new_road.add_s(4)
            new_road.append(Turn3)   
        elif b == "C9-C0":
            new_road.add_s(1)
            new_road.append(Turn3)
            new_road.add_s(2)
        elif b == "V4-V1":
            new_road.add_s(4)
            new_road.append(STurn4)
            new_road.add_s(2)
        elif b == "L6-L5":
            new_road.add_s(2)
            new_road.append(Turn1)
            new_road.add_s(3)
            new_road.append(KTurn4)
            new_road.add_s(2)
            new_road.append(Turn4)
        elif b == "V2-V3":
            new_road.add_s(3)
            new_road.append(Turn1)
            new_road.add_s(3)
        elif b == "C1-C2":
            new_road.append(Turn4)
            new_road.add_s(2)
            new_road.append(Turn3)
            new_road.add_s(1)
            new_road.append(Turn2)  
            new_road.add_s(2)
            new_road.append(KTurn2)
            new_road.add_s(3)
            new_road.append(Turn4)
            new_road.add_s(4)
            new_road.append(Turn2)                  
            new_road.add_s(1)
        elif b == "L4-L7":
            new_road.add_s(2)
            new_road.append(KTurn4)
            new_road.add_s(2)
            new_road.append(ShortKTurn3)  
            new_road.add_s(2)
            new_road.append(Bump4)
            new_road.add_s(5)
        elif b == "V0-V5":
            new_road.add_s(1)
            new_road.append(ShortKTurn4)
            new_road.add_s(3)
            new_road.append(Bump3)  
            new_road.add_s(4)
            new_road.append(KTurn3)
            new_road.add_s(1)
        elif b == "J6-J5":
            new_road.add_s(1)
            new_road.append(KTurn3)
            new_road.add_s(3)
            new_road.append(KTurn2)  
            new_road.add_s(1)
        elif b == "V6-V9":
            new_road.add_s(2)
            new_road.append(KTurn3)
            new_road.add_s(1)
            new_road.append(SKBTurn3)  
            new_road.add_s(3)
            new_road.append(KTurn2)
            new_road.add_s(2)  
        elif b == "A24-A33-A21":
            new_road.add_s(2)
            new_road.append(Cross2)
            new_road.append(Turn2)  
            new_road.add_s(1)
            new_road.append(Turn1)
            new_road.add_s(4)
            new_road.append(Turn3)
            new_road.add_s(1)               
        elif b == "C3-C8":
            new_road.add_s(1)
            new_road.append(Turn2)
            new_road.add_s(2)
            new_road.append(KTurn1)
            new_road.add_s(1)
            new_road.append(KTurn1)  
            new_road.add_s(2)
            new_road.append(Turn1)
            new_road.add_s(4)
            new_road.append(Turn2)
            new_road.add_s(4)
            new_road.append(KTurn2)                  
            new_road.add_s(2)
            new_road.append(Bump4)
            new_road.add_s(2)
        elif b == "P16-P13":
            new_road.append(Turn3)
            new_road.add_s(2)
            new_road.append(ShortKTurn4)
            new_road.add_s(4)
            new_road.append(Turn3)  
        elif b == "J19-J10":
            new_road.add_s(1)
            new_road.append(Turn1)
            new_road.add_s(2)
            new_road.append(STurn1)
            new_road.append(STurn1)
            new_road.add_s(4)
        elif b == "C5-C4":
            new_road.add_s(1)
            new_road.append(Turn3)
            new_road.add_s(1)
            new_road.append(Turn1)
            new_road.add_s(5)
        elif b == "L16-L15":
            new_road.add_s(2)
            new_road.append(STurn1)
            new_road.append(STurn1)
            new_road.add_s(3)
            new_road.append(Turn3)
            new_road.add_s(2)     
            new_road.append(Turn3)   
        elif b == "C1-C2":
            new_road.append(Turn4)
            new_road.add_s(2)
            new_road.append(Turn3)
            new_road.add_s(1)
            new_road.append(Turn2)
            new_road.add_s(2)
            new_road.append(KTurn2)
            new_road.add_s(3)
            new_road.append(Turn4)
            new_road.add_s(4)
            new_road.append(Turn2)
            new_road.add_s(1)
        elif b == "C10-C19":
            new_road.add_s(2)
            new_road.append(STurn3)
            new_road.append(STurn3)
            new_road.add_s(1)
           
        elif b == "C12-C11":
            new_road.add_s(1)
            new_road.append(STurn2)
            new_road.append(STurn2)
            new_road.add_s(4)
            new_road.append(STurn4)
            new_road.append(STurn4)
            new_road.add_s(3)
            new_road.append(Turn1)
            new_road.add_s(2)
            new_road.append(Turn1)
            new_road.add_s(1)
            new_road.append(STurn3)
            new_road.append(STurn3)
            new_road.add_s(2)
            new_road.append(STurn4)
            new_road.append(STurn4)            
        elif b == "J11-J14":
            new_road.append(Turn4)
            new_road.add_s(2)
            new_road.append(STurn3)
            new_road.append(STurn3)
            new_road.add_s(3)
            new_road.append(STurn1)
            new_road.append(STurn1)
            new_road.append(STurn1)
            new_road.append(STurn1)
            new_road.add_s(3)
            new_road.append(STurn4)
            new_road.append(STurn4)
            new_road.add_s(5)
            new_road.append(STurn1)
            new_road.append(STurn1)
            new_road.add_s(3)
            new_road.append(STurn1)
            new_road.append(STurn1)
            new_road.add_s(4)
        elif b == "V3-V2":
            new_road.add_s(3)
            new_road.append(KTurn1)
            new_road.add_s(3)        
        elif b == "J0-J9":
            new_road.add_s(4)
            new_road.append(Turn1)
            new_road.add_s(2)      
            new_road.append(KTurn2)
            new_road.add_s(1) 
        elif b =="C9-C0":
            new_road.add_s(1)             
            new_road.append(Turn3)
            new_road.add_s(2)  
        elif b == "L0-L1":
            new_road.add_s(1)  
            new_road.append(Turn2)
            new_road.add_s(3)  
            new_road.append(KTurn3)
            new_road.add_s(1)
        elif b == "L8-L9":
            new_road.add_s(1)  
            new_road.append(Turn2)
            new_road.add_s(2)  
            new_road.append(Turn1)
            new_road.add_s(3)
            new_road.append(Turn1)
            new_road.add_s(5)
        elif b == "V7-V8":
            new_road.add_s(1)  
            new_road.append(STurn3)
            new_road.append(STurn3)
            new_road.add_s(1)
        elif b == "X":
            new_road.add_s(1)     
            #V2-V3/C1-C2/L4-L7/V0-V5/J6-J5/V6-V9/X 
        else:
            return False
        if invert:
            new_road.invert()
        self.append_road(new_road)
        return True
        
    
    def from_road_book(self, s):
        #parse s
        branch_l = s.split("/")
        for branch in branch_l:
            if self.add_branch(branch) == False:
                b_l = branch.split('-')
                b_i = b_l[1] + '-' + b_l[0]
                if self.add_branch(b_i, True) == False:
                     print("Error, unknown branch:" + branch)
                    
    
    def what_next(self, tile, pos_on_tile):
        #return [add_to_tile, pos_on_tile]
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
        ret = 'Road length:' + str(len(self.tiles)) + "\n"
        for tile in self.tiles:
            ret += tile.inspect() + "\n"
        return ret
        
fr = Road()

#1522:  C8-C3/V9-V6/J1-J4/X
#J8-J7/C9-C0/V4-V1/L6-L5/V2-V3/C1-C2/L4-L7/V0-V5/J6-J5/V6-V9/X
#1523_03 :C3-C8/V3-V2/J0-J9/C9-C0/X
#1537_01:  J8-J7/C1-C2/J6-J5/L8-L9/V4-V1/X
#551_03: J19-J10/C5-C4/V5-V0/L16-L15/V1-V4/J11-J14/X/
#1525_02: V0-V5/C3-C8/L4-L7/X
#1524_03: V1-V4/J6-J5/L5-L6/C2-C1/L7-L4/V5-V0/X
#539_01_ending: J3-J2/L3-L2//X
p("Test")
fr = Road()
game_no = 55002
#fr.from_game(1536)
#fr.from_road_book("V5-V0/J6-J5/V1-V4/C4-C5/L7-L4/X")
#fr.from_road_book("J4-J1/V5-V0/L4-L7/C5-C4/X")
#fr.append(Bump4)
#fr.add_s(4)    
#fr.append(Turn1)       
#fr.add_s(4)
#fr.append(KTurn2)
#fr.add_s(1)
#ANALYSER 1537_02
#fr.add_s(1)
#fr.append(KTurn3)
#fr.add_s(1)
#fr.add_s(1)
#fr.append(Turn2)
#fr.add_s(2)
#fr.append(KTurn1)
#fr.add_s(1)
#fr.append(KTurn1)  
#fr.add_s(2)
#fr.append(Turn1)
#fr.add_s(4)
#fr.append(Turn2)
#fr.add_s(4)
#fr.append(KTurn2)                  
#fr.add_s(2)
#fr.append(Bump4)
#fr.add_s(2)
#fr.from_road_book("C3-C8/X")#/L4-L7/X")
#fr.from_road_book("J4-J1/L0-L1/J0-J9/X")
#fr.append(KTurn4)
#fr.add_s(2)
#fr.append(ShortKTurn3)  
#fr.add_s(2)
#fr.append(Bump4)
#fr.append(KTurn3)
#fr.add_s(1)
fr.from_road_book("B8-B9/L17-L14/C2-C1/X")

print(fr.inspect())

         