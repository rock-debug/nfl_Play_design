import numpy as np

def compute_basic_features(off, defn):
    # Example placeholder: measure how deep defenders are
    depths = defn[:, 0]
    num_deep = int(np.sum(depths > 18))
    avg_depth = float(np.mean(depths))
    return {"num_deep": num_deep, "avg_depth": avg_depth}
