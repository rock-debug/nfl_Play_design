import numpy as np

def arr_from_routes(routes):
    """
    routes: List[PlayerRoute]
    return np.array (N_players, T, 2) assuming equal length; pads by last value if unequal
    """
    max_T = max(len(p.route) for p in routes) if routes else 0
    mats = []
    for r in routes:
        pts = np.array([[p.x, p.y] for p in r.route], dtype=float)
        if len(pts) < max_T and len(pts) > 0:
            pad = np.tile(pts[-1], (max_T - len(pts), 1))
            pts = np.vstack([pts, pad])
        mats.append(pts if len(pts) else np.zeros((max_T, 2)))
    return np.stack(mats, axis=0) if mats else np.zeros((0, 0, 2))

def num_deep_defenders(def_routes, eval_idx=10, depth_thresh=18.0):
    """Count defenders deeper than threshold at eval frame."""
    if def_routes.size == 0: return 0
    depths = def_routes[:, eval_idx, 0]
    return int(np.sum(depths > depth_thresh))
def dist(a, b):
    return float(np.linalg.norm(a - b))

def unit(v):
    n = np.linalg.norm(v)
    return v if n < 1e-6 else v / n
