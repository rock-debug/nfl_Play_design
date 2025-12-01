import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

FIELD_LENGTH = 120.0
FIELD_WIDTH = 53.3
HASH_LEFT = 17.0
HASH_RIGHT = FIELD_WIDTH - HASH_LEFT

def draw_field(ax=None, show_hashes=True):
    created = False
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 5))
        created = True
    else:
        fig = ax.figure

    ax.set_xlim(0, FIELD_LENGTH)
    ax.set_ylim(0, FIELD_WIDTH)
    ax.set_xticks([]); ax.set_yticks([])
    ax.add_patch(Rectangle((0,0), FIELD_LENGTH, FIELD_WIDTH, fill=False, linewidth=1.2))
    for x in range(10, 111, 10):
        ax.plot([x, x], [0, FIELD_WIDTH], color='lightgray', linewidth=0.7)
        ax.text(x, FIELD_WIDTH - 2.2, f"{(x-10)%100}", ha='center', va='top', fontsize=8, color='gray')
    if show_hashes:
        for x in range(10, 111):
            ax.plot([x, x], [HASH_LEFT, HASH_LEFT + 0.15], color='black', linewidth=0.8)
            ax.plot([x, x], [HASH_RIGHT - 0.15, HASH_RIGHT], color='black', linewidth=0.8)
    if created: return fig, ax
    return fig, ax

if __name__ == "__main__":
    fig, ax = draw_field()
    ax.set_title("NFL Field (120 x 53.3)")
    plt.show()
