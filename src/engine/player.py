import numpy as np
from engine.player_defaults import POSITION_SPEED, POSITION_RADIUS

OFFENSIVE_POSITIONS = ["QB","RB","FB","WR","TE","LT","LG","C","RG","RT"]
DEFENSIVE_POSITIONS = ["DE","DT","NT","OLB","ILB","MLB","LB","CB","S","FS","SS","NB"]
ALL_ROLES = OFFENSIVE_POSITIONS + DEFENSIVE_POSITIONS + ["K","P","LS"]

class Player:
    def __init__(self, player_id, team='off', role='WR', start_pos=(0.0,0.0), route=None, speed=None):
        role = role.upper()
        assert role in ALL_ROLES, f"Invalid role {role}"
        self.id = player_id
        self.team = team
        self.role = role
        self.start_pos = np.array(start_pos, dtype=float)
        self.speed = float(POSITION_SPEED.get(role, 1.4)) if speed is None else float(speed)
        self.radius = float(POSITION_RADIUS.get(role, 1.6))
        self.route = np.array(route, dtype=float) if route is not None else None
    def set_route(self,route):
        self.route=route    

    def position_at(self, t_idx):
        if self.route is None: return self.start_pos.copy()
        if t_idx < 0: return self.route[0].copy()
        if t_idx >= len(self.route): return self.route[-1].copy()
        return self.route[t_idx].copy()

    def __repr__(self):
        return f"<Player id={self.id} role={self.role} team={self.team} speed={self.speed}>"
