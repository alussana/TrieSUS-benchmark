#!/usr/bin/env python3

# Alessandro Lussana <alussana@ebi.ac.uk>

import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

from matplotlib import rcParams

rcParams["axes.facecolor"] = "FFFFFF"
rcParams["savefig.facecolor"] = "FFFFFF"
rcParams["xtick.direction"] = "in"
rcParams["ytick.direction"] = "in"

rcParams.update({"figure.autolayout": True})

plt.rcParams["figure.figsize"] = (5,4)

if __name__ == '__main__':
    df = pd.read_csv('records.tsv', header=None, sep='\t')
    df.columns = [
        'Method',
        'Sets',
        'Items',
        'Universe',
        'Function calls',
        'Seconds'
    ]
    df['Input size parameter'] = df['Sets'].astype(str)
    df = df.sort_values(by='Sets') 
    
    plt.clf()
    g = sns.lineplot(
        data=df,
        x='Input size parameter',
        y='Seconds',
        hue='Method',
    )
    g.set(yscale='log')
    plt.legend(frameon=False)
    sns.despine()
    plt.savefig('plots/seconds_log.svg')
    
    plt.clf()
    g = sns.lineplot(
        data=df,
        x='Input size parameter',
        y='Seconds',
        hue='Method',
    )
    plt.legend(frameon=False)
    sns.despine()
    plt.savefig('plots/seconds.svg')
    
    plt.clf()
    g = sns.lineplot(
        data=df,
        x='Input size parameter',
        y='Function calls',
        hue='Method',
    )
    g.set(yscale='log')
    plt.legend(frameon=False)
    sns.despine()
    plt.savefig('plots/function_calls_log.svg')
    
    plt.clf()
    g = sns.lineplot(
        data=df,
        x='Input size parameter',
        y='Function calls',
        hue='Method',
    )
    plt.legend(frameon=False)
    sns.despine()
    plt.savefig('plots/function_calls.svg')