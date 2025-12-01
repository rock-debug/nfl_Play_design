from engine.player import Player
FIELD_WIDTH = 53.3
SNAP_X = 20.0

def singleback_11():
    players = []
    players.append(Player("QB", 'off', 'QB', (SNAP_X, FIELD_WIDTH/2)))
    players.append(Player("RB", 'off', 'RB', (SNAP_X-3, FIELD_WIDTH/2)))
    players.append(Player("WR1",'off','WR',(SNAP_X+2, 8)))
    players.append(Player("WR2",'off','WR',(SNAP_X+2, FIELD_WIDTH-8)))
    players.append(Player("WR3",'off','WR',(SNAP_X+2, FIELD_WIDTH/2 + 10)))
    players.append(Player("TE", 'off','TE',(SNAP_X+1, FIELD_WIDTH/2 + 2)))
    ol_x = SNAP_X - 1
    for off,yoff in zip(["LT","LG","C","RG","RT"], [-3,-1,0,1,3]):
        players.append(Player(off,'off',off,(ol_x, FIELD_WIDTH/2 + yoff)))
    return players

def shotgun_trips():
    p = []
    p.append(Player("QB",'off','QB',(SNAP_X+4, FIELD_WIDTH/2)))
    p.append(Player("RB",'off','RB',(SNAP_X+2, FIELD_WIDTH/2 - 6)))
    p.append(Player("WR1",'off','WR',(SNAP_X+6, FIELD_WIDTH/2 + 12)))
    p.append(Player("WR2",'off','WR',(SNAP_X+6, FIELD_WIDTH/2 + 6)))
    p.append(Player("WR3",'off','WR',(SNAP_X+6, FIELD_WIDTH/2 + 2)))
    p.append(Player("WR4",'off','WR',(SNAP_X+6, 6)))
    p.append(Player("TE",'off','TE',(SNAP_X+1, FIELD_WIDTH/2 + 2)))
    ol_x = SNAP_X + 3
    for off,yoff in zip(["LT","LG","C","RG","RT"], [-3,-1,0,1,3]):
        p.append(Player(off,'off',off,(ol_x-2, FIELD_WIDTH/2 + yoff)))
    return p
