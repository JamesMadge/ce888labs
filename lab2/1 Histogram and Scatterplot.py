import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 

# def permutation(statistic, error):

def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))

if __name__ == "__main__":
    # READ DATA
    df = pd.read_csv('./vehicles.csv')

    # TRANSPOSE DATA
    data_current_fleet = df.values.T[0]
    data_proposed_fleet = df.dropna().values.T[1]

    # PRINT SUMMARY STATISTICS
    print("::::: Summary Statistics: Current Fleet")
    print((("Mean: %f")%(np.mean(data_current_fleet))))
    print((("Median: %f")%(np.median(data_current_fleet))))
    print((("Var: %f")%(np.var(data_current_fleet))))
    print((("std: %f")%(np.std(data_current_fleet))))
    print((("MAD: %f")%(mad(data_current_fleet))))

    print("::::: Summary Statistics: Proposed Fleet")
    print((("Mean: %f")%(np.mean(data_proposed_fleet))))
    print((("Median: %f")%(np.median(data_proposed_fleet))))
    print((("Var: %f")%(np.var(data_proposed_fleet))))
    print((("std: %f")%(np.std(data_proposed_fleet))))
    print((("MAD: %f")%(mad(data_proposed_fleet))))

    # SCATTER PLOT
    sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)
    sns_plot.axes[0,0].set_ylim(0,)
    sns_plot.axes[0,0].set_xlim(0,)
    sns_plot.savefig("scaterplot_vehicles.png",bbox_inches='tight')
    sns_plot.savefig("scaterplot_vehicles.pdf",bbox_inches='tight')

    # HISTOGRAMS
    # CURRENT FLEET
    plt.clf()
    sns_plot2 = sns.distplot(data_current_fleet, bins=20, kde=False, rug=True).get_figure()
    axes = plt.gca()
    axes.set_xlabel('Fuel Consumption (MPG)')
    axes.set_ylabel('Vehicle Count')
    sns_plot2.savefig("histogram_vehicles_current_fleet.png",bbox_inches='tight')
    sns_plot2.savefig("histogram_vehicles_current_fleet.pdf",bbox_inches='tight')

    # PROPOSED FLEET
    plt.clf()
    sns_plot2 = sns.distplot(data_proposed_fleet, bins=20, kde=False, rug=True).get_figure()
    axes = plt.gca()
    axes.set_xlabel('Fuel Consumption (MPG)')
    axes.set_ylabel('Vehicle Count')
    sns_plot2.savefig("histogram_vehicles_proposed_fleet.png",bbox_inches='tight')
    sns_plot2.savefig("histogram_vehicles_proposed_fleet.pdf",bbox_inches='tight')