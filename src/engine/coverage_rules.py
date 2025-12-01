import numpy as np

def nearest_neighbor_assign(def_pos, off_positions):
    dists = np.linalg.norm(off_positions - def_pos.reshape(1,2), axis=1)
    return int(np.argmin(dists)), float(np.min(dists))

def simple_man_zone_decision(def_pos, off_positions, threshold_man=5.5):
    idx, dist = nearest_neighbor_assign(np.array(def_pos), np.array(off_positions))
    if dist <= threshold_man:
        return "MAN", idx, dist
    return "ZONE", None, dist

def tessellate_grid(def_positions, grid_res=(240,120)):
    xs = np.linspace(0, 120, grid_res[0])
    ys = np.linspace(0, 53.3, grid_res[1])
    XX, YY = np.meshgrid(xs, ys)
    pts = np.stack([XX.ravel(), YY.ravel()], axis=1)
    D = np.linalg.norm(pts[:,None,:] - np.array(def_positions)[None,:,:], axis=2)
    nearest = D.argmin(axis=1).reshape(XX.shape)
    return xs, ys, nearest
