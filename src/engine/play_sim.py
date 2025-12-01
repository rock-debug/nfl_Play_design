import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from engine.field import draw_field
from engine.player import Player
from engine.formations import singleback_11
from engine.defensive_shells import cover2
from engine.blocking import ol_pass_protect, dl_basic_rush
from engine.coverage_rules import simple_man_zone_decision, tessellate_grid

def gen_route(start_x, start_y, route_type="go", T=30):
    t = np.linspace(0, 1, T)
    if route_type == "go":
        x = start_x + t * 30; y = np.full_like(t, start_y)
    elif route_type == "slant":
        x = start_x + t * 20; y = start_y + t * 10
    elif route_type == "out":
        x = start_x + t * 15; y = start_y + (t>0.5)*(t-0.5)*20
    else:
        x = np.full_like(t, start_x); y = np.full_like(t, start_y)
    return np.stack([x, y], axis=1)

def simulate_demo(T=40, visualize=True):
    # offense formation
    off_players = singleback_11()
    # assign simple WR routes
    for p in off_players:
        if p.role == "WR":
            p.route = gen_route(*p.start_pos, route_type="go", T=T)
        elif p.role == "TE":
            p.route = gen_route(*p.start_pos, route_type="out", T=T)
        else:
            p.route = np.tile(p.start_pos, (T,2))

    # OL pass pro
    ol = [p for p in off_players if p.role in ("LT","LG","C","RG","RT")]
    ol_routes = ol_pass_protect(ol, pocket_depth=6.0, T=T)
    for p in ol:
        p.route = ol_routes[p.id]

    # defense shell
    def_players = cover2()
    # designate DL (if present) to rush
    dl = [p for p in def_players if p.role in ("DE","DT","NT")]
    if dl:
        dl_routes = dl_basic_rush(dl, rush_angle_deg=2.0, T=T)
        for p in dl:
            p.route = dl_routes[p.id]
    # others will be moved by simple man/zone each frame
    others = [p for p in def_players if p not in dl]
    for p in others:
        p.route = np.tile(p.start_pos, (T,2))

    # build arrays for fast stepping
    off_routes = np.stack([p.route for p in off_players], axis=0)  # (N_off,T,2)
    def_routes = np.stack([p.route for p in def_players], axis=0)  # (N_def,T,2)

    # per-frame update for DB/LB (others)
    for t in range(T):
        offs_t = off_routes[:, t, :]
        for i,p in enumerate(def_players):
            if p in dl:  # DL already has route
                continue
            cur = def_routes[i, t-1] if t>0 else p.start_pos
            mode, tgt, _ = simple_man_zone_decision(cur, offs_t, threshold_man=6.0)
            if mode == "MAN" and tgt is not None:
                target = offs_t[tgt]
                direction = target - cur
                norm = np.linalg.norm(direction) + 1e-6
                step = min(p.speed*0.8, norm)
                new_pos = cur + (direction / norm) * step
            else:
                center = np.array([60.0, 26.65])
                direction = center - cur
                norm = np.linalg.norm(direction) + 1e-6
                new_pos = cur + (direction / norm) * (p.speed*0.4)
            def_routes[i, t, :] = new_pos
            if t < T-1:
                def_routes[i, t+1:, :] = new_pos

    if visualize:
        fig, ax = draw_field()
        scat_off = ax.scatter([], [], c='blue', s=80, label='Offense')
        scat_def = ax.scatter([], [], c='red',  s=80, label='Defense')
        ax.legend(loc='upper right')

        def update(frame):
            offs = off_routes[:, frame, :]
            defs = def_routes[:, frame, :]
            scat_off.set_offsets(offs)
            scat_def.set_offsets(defs)
            xs, ys, nearest = tessellate_grid(defs, grid_res=(240,120))
            ax.images = []
            ax.imshow(nearest, origin='lower', extent=(0,120,0,53.3), alpha=0.25, interpolation='nearest')
            ax.set_title(f"Timestep {frame}")
            return scat_off, scat_def

        FuncAnimation(fig, update, frames=range(T), interval=150, blit=False)
        plt.show()

    return off_players, def_players, off_routes, def_routes

if __name__ == "__main__":
    simulate_demo(T=40, visualize=True)
