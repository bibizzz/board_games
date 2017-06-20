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
        if tile >= len(self.tiles): # this is the last tile
            return [-10,-10]
        
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
        self.last_dice = -1
        self.road = road
        self.move = 0
        self.time = 0
        self.tile_position = -1
        self.pos_on_tile = 0
        self.time = 0
        self.dices = [1,2,3,4,5]
        self.gaz = 2
        self.actual_speed = 0
        self.father = None 
        self.successors = []
        self.finish = False
    
    def auth_dices(self):
        gears = [f for f in self.dices if 
            f >= self.actual_speed-1 and 
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
        
        ns = State(self.road)
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
            ns.last_dice = dice    
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
        ns.dices = [1,2,3,4,5]
        ns.gaz = 2
        ns.last_dice = -1
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
            p("Move " + str(r.move) + ':' + str(r.time) + 's. ' + str(r.last_dice))  
            r = r.father
         
    def inspect(self):
        p("Move " + str(self.move) + ':' + str(self.time) + 's. ' + str(self.last_dice))   
        p('position ' + str(self.tile_position) + ' on_tile ' + str(self.pos_on_tile))         
        p(str(self.dices) + ' gaz:' + str(self.gaz) + ' speed:' 
            + str(self.actual_speed) + ' Finish ' + str(self.finish))

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
        

p("T'est")
fr = Road()
Straight = Tile('straight')
Turn2 = Tile('turn', [2,3])
#fr.append(Straight)
fr.append(Turn2)
fr.append(Straight)
#fr.append(Straight)
#fr.append(Straight)
fr.append(Turn2)
fr.append(Straight)
#fr.append(Straight)
#fr.append(Straight)
fr.inspect()

start = State(fr)
start.actual_speed = 4
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

histo = [0] *50
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

def find_min(root):
    if root.successors == []:
        if root.finish == True:
            if (root.time < 50):
                interesting.append(root)
            histo[int(root.time/10)] += 1
            return root.time, root
        else:
            return 1000000, None
    else:
        min = 100000000
        for st in root.successors:
            min_s, st_l = find_min(st) 
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
    ret= []    
    min_ref = 100000
    for s in fifo:
        if s.time < min_ref:
            min_ref = s.time
    p(min_ref)
    min_supress = min_ref + max_time
    
    for s in fifo:
        if s.time <= min_supress:
            ret.append(s)
    return ret
            

min_tile = [10000] * 20


tile_time = [1000] * 20
tile_number = [0] * 20 

def parcours_tile(node, road):
    nb_tiles = len(road.tiles)
    node.find_successors()
    fifo = []
    for s in node.successors:
        fifo.append(s)
    for pos in range(nb_tiles):
        next_fifo = []
        while len(fifo) > 0:
            cur = fifo.pop(0) 
            if cur.tile_position > pos:
                next_fifo.append(cur)
            else:
                cur.find_successors()
                for lower in cur.successors:
                    fifo.append(lower)
        print('Tile ' + str(pos) + ' finished. Next: ' + str(len(next_fifo)) )
        fifo  = next_fifo
        if len(fifo) > 1000 and road.tiles[pos].type == 'straight' :
            p("reduce!")
            fifo = reduce_fifo(fifo, 100)
            p(len(fifo))

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
p(min_l)
p(min)
f = min_l
while f != None:
    f.inspect()
    f = f.father
    
#p(histo)
#for r in interesting:
#    p("NEW")
#    r.trace_moves()

#dot = parcours_dot(start)

#f = open("test.dot", "w")  
#f.write( " graph  {" + dot + "}" )       
#f.close()
