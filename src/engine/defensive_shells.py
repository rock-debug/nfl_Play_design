from engine.player import Player
FIELD_WIDTH = 53.3

def cover1():
    d=[]
    d.append(Player("CB1",'def','CB',(18,8)))
    d.append(Player("CB2",'def','CB',(18,FIELD_WIDTH-8)))
    d.append(Player("LB1",'def','MLB',(15,FIELD_WIDTH/2 - 6)))
    d.append(Player("LB2",'def','OLB',(15,FIELD_WIDTH/2 + 6)))
    d.append(Player("S1",'def','S',(42,FIELD_WIDTH/2)))
    return d

def cover2():
    d=[]
    d.append(Player("CB1",'def','CB',(18,8)))
    d.append(Player("CB2",'def','CB',(18,FIELD_WIDTH-8)))
    d.append(Player("LB1",'def','MLB',(14,FIELD_WIDTH/2 - 6)))
    d.append(Player("LB2",'def','OLB',(14,FIELD_WIDTH/2 + 6)))
    d.append(Player("S1",'def','FS',(48,12)))
    d.append(Player("S2",'def','SS',(48,FIELD_WIDTH-12)))
    return d

def cover3():
    d=[]
    d.append(Player("CB1",'def','CB',(18,8)))
    d.append(Player("CB2",'def','CB',(18,FIELD_WIDTH-8)))
    d.append(Player("S1",'def','S',(50,FIELD_WIDTH/2)))
    d.append(Player("LB1",'def','MLB',(13,FIELD_WIDTH/2 - 6)))
    d.append(Player("LB2",'def','OLB',(13,FIELD_WIDTH/2 + 6)))
    d.append(Player("DE1",'def','DE',(10,6)))
    d.append(Player("DE2",'def','DE',(10,FIELD_WIDTH-6)))
    return d

def quarters():
    d=[]
    for i,y in enumerate([8, FIELD_WIDTH/2 - 4, FIELD_WIDTH/2 + 4, FIELD_WIDTH-8]):
        d.append(Player(f"S{i+1}",'def','S',(48,y)))
    d.append(Player("LB1",'def','MLB',(12,FIELD_WIDTH/2)))
    d.append(Player("DE1",'def','DE',(10,10)))
    d.append(Player("DE2",'def','DE',(10,FIELD_WIDTH-10)))
    return d
