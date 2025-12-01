import numpy as np

def extract_player_features(route, snap_x=20.0):
    """
    route: np.array(T,2)
    Returns a 1D vector of engineered features for classification.
    """
    if len(route) < 2:
        # fallback
        route = np.vstack([route, route])

    x0, y0 = route[0]   # pre-snap
    x1, y1 = route[1]   # first post-snap movement

    # Early movement vector
    dx = x1 - x0
    dy = y1 - y0
    direction = np.arctan2(dy, dx + 1e-6)

    # Speeds
    diffs = np.diff(route, axis=0)
    speeds = np.linalg.norm(diffs, axis=1)

    speed_mean = np.mean(speeds)
    speed_std  = np.std(speeds)

    # Depth (distance from LOS)
    depth = x0 - snap_x

    # width alignment (slot vs wide)
    width_from_center = abs(y0 - 26.65)

    return np.array([
        x0, y0,
        dx, dy,
        direction,
        speed_mean, speed_std,
        depth,
        width_from_center
    ], dtype=float)
