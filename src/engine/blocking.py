import numpy as np
from engine.player import Player

def ol_pass_protect(ol_players, pocket_depth=6.0, T=30):
    routes = {}
    for p in ol_players:
        start = np.array(p.start_pos)
        side = -1 if p.role in ("LT","LG") else (1 if p.role in ("RG","RT") else 0)
        route = np.zeros((T,2))
        for t in range(T):
            back = min(p.speed * t * 0.4, pocket_depth)
            lateral = side * min(t*0.08, 1.0) * 1.5
            route[t] = start + np.array([-back, lateral])
        routes[p.id] = route
    return routes

def dl_basic_rush(dl_players, rush_angle_deg=0.0, T=30):
    routes = {}
    rad = np.deg2rad(rush_angle_deg)
    dir_vec = np.array([1.0, np.tan(rad)])
    dir_vec = dir_vec / (np.linalg.norm(dir_vec) + 1e-6)
    for p in dl_players:
        start = np.array(p.start_pos)
        route = np.zeros((T,2))
        for t in range(T):
            step = p.speed * (t+1) * 0.9
            route[t] = start + dir_vec * step
        routes[p.id] = route
    return routes
