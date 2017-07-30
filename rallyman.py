# -*- coding: utf-8 -*-

from collections import deque
import road

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
                

class State:
    def __init__(self,road, mrc = MRC()):
        self.double_low = False
        
        self.shakedown = True
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
        self.nb_dices_played = 0
        self.nb_seconds_win = 0
        self.info = None
    
    def h_state(self):
        #paramètres différentiateurs
        return str([self.time, self.tile_position, self.pos_on_tile, self.dices,  
                self.gaz, self.actual_speed,self.nb_seconds_win ])
            
    
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
        if dice == 0:
            if self.actual_speed < min_auth:
                return None
        elif dice != 0 and dice < min_auth:
            return None            
           
        # bump ?
        if self.road.tiles[self.tile_position+tile].type == 'bump':
            if self.actual_speed ==  self.road.tiles[self.tile_position].get_max_gear(self.pos_on_tile) - 1:
                tile += 1
            if self.shakedown and self.actual_speed == \
                self.road.tiles[self.tile_position].get_max_gear(self.pos_on_tile):
                tile += 2
       
        ns = State(self.road)
        ns.nb_seconds_win = self.nb_seconds_win
        ns.nb_dices_played = self.nb_dices_played + 1
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
                # bump ?
        if ns.road.tiles[ns.tile_position].type == 'bump':
            if ns.actual_speed ==  ns.road.tiles[ns.tile_position].get_max_gear(ns.pos_on_tile) - 1:
                ns.tile_position += 1
            if ns.shakedown and ns.actual_speed == \
                ns.road.tiles[ns.tile_position].get_max_gear(ns.pos_on_tile):
                ns.tile_position += 2
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
        ns.father = self
        if self.nb_dices_played > 1:
            ns.nb_seconds_win = self.nb_seconds_win + self.nb_dices_played
        else:
            ns.nb_seconds_win = self.nb_seconds_win 
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
    
    def inspect_simple(self):
        ret ="Move " + str(self.move) + ':' + str(self.time) + 's. -' + str(self.nb_seconds_win) + ' ' + str(self.last_dice)
        ret += ' '  + str(self.pos_on_tile) +  ' ' + str(self.tile_position) + ' '\
            + self.road.tiles[self.tile_position].inspect()
        return ret
         
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
    
 
start = State(road.fr)
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

def parcours_dot(root, tile_max = 100000):
    nodes = ""
    if root.last_dice != -1:
        ret = str(root.last_dice) + str(root.tile_position) +str(root.pos_on_tile)
    else:
        ret =  str(root.time)
    if root.tile_position >= tile_max:
        return ""  
    nodes = nodes + 'u' + str(id(root)) + '[label=' + ret + '] \n'     
    nodes = nodes + 'u' + str(id(root)) + '-- {' 
    if root.successors != None:
        for st in root.successors:
           nodes = nodes + 'u' + str(id(st)) + ';' 
        nodes = nodes + "}\n"  
        for st in root.successors:
            nodes = nodes +parcours_dot(st, tile_max)
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
            time = root.time - root.nb_seconds_win
            if (time <= interesting_time):
                interesting.append(root)
            #histo[int(root.time/10)] += 1
            return time, root
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
        if s.time - s.nb_seconds_win < min_ref:
            min_ref = s.time - s.nb_seconds_win
    p("Min: " + str(min_ref))
    min_supress = min_ref + max_time   
    for s in fifo:
        if s.time - s.nb_seconds_win <= min_supress:
            ret.append(s)
        else:
            s.info = "reduced" + str(min_supress)
    return ret
            

min_tile = [10000] * 150

histo_tile = [0] * 10

tile_time = [1000] * 150
tile_number = [0] * 150

hash_state = {}

def play(node, dice):
    for s in node.successors:
        if s.last_dice == dice:
            return s
    p('not a valid move')
    return node



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
              #  histo_tile[int(cur.time/10)] += 1
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
                        cur.info = "hash" + cur.h_state()
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
parcours_tile(start, road.fr)

p(min_tile)
print("start min finding")
print(nb_leaves(start))
min, min_l = find_min(start)
min, min_l = find_min(start, min+9)
p(min_l)
p(min)
#f = min_l
#while f != None:
#    f.inspect()
#    f = f.father
    
p(histo)

#for r in interesting:
#    p("NEW")
#    p(id(r))
#    r.trace_moves()
p(str(len(interesting))+' interesting moves')

#for r in interesting:
#    r.inspect()

#dot = parcours_dot(start)
dot = parcours_dot_sons(interesting)

f = open("test.dot", "w")  
f.write( " graph  {" + dot + "}" )       
f.close()
p(min)

g =open("results.txt", "w")
g.write(str(len(interesting))+ " interesting moves\n")
for r in interesting:         
    g.write("##########NEW##############\n")
    t = r
    while t != None:
        g.write(t.inspect_simple())
        g.write("\n")
        t = t.father
g.close()


