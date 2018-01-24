import matplotlib

matplotlib.use('Agg')

import pandas as pd

import numpy as np

def bootstrap(statistic_func, iterations, data):
    vals = []
    samples = np.random.choice(data, replace=True, size=[iterations, len(data)])
    for sample in samples:
        sta = statistic_func(sample)
        vals.append(sta)
    b = np.array(vals)
    # print b
    lower, upper = np.percentile(b, [2.5, 97.5])
    return np.mean(b), lower, upper

if __name__ == "__main__":


    boots = []
    samples = 100000
    df = pd.read_csv('./vehicles.csv')
    fleet_current = df.values.T[0]
    fleet_proposed = df.dropna().values.T[1]

    # Find the upper and lower bound of the standard deviation in the current fleet.
    # Current fleet.
    boot = bootstrap(np.std, samples, fleet_current)
    print("::::: Standard Deviation: Current Fleet")
    print("STD : %f" % np.std(fleet_current))
    print("STD Mean: %f" % boot[0])
    print("STD Lower Bound : %f" % boot[1])
    print("STD Upper Bound: %f" % boot[2])

    # Proposed fleet.
    boot = bootstrap(np.std, samples, fleet_proposed)
    print("::::: Standard Deviation: Proposed Fleet")
    print("STD : %f" % np.std(fleet_proposed))
    print("STD Mean: %f" % boot[0])
    print("STD Lower Bound : %f" % boot[1])
    print("STD Upper Bound: %f" % boot[2])