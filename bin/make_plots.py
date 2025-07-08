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

plt.rcParams["figure.figsize"] = (2.5, 2.5)


# ====
plt.rcParams["axes.titlesize"] = 7
plt.rcParams["axes.labelsize"] = 6
plt.rcParams["xtick.labelsize"] = 6
plt.rcParams["ytick.labelsize"] = 6
plt.rcParams["legend.fontsize"] = 6
plt.rcParams["figure.titlesize"] = 8
plt.rcParams["font.size"] = 6

red_shade = "#d62728"
grey_shade = "#7f7f7f"

custom_palette = sns.color_palette(["grey", "red"])

blended_palette = sns.blend_palette([custom_palette[0], custom_palette[1]], n_colors=4)

sns.set_palette(custom_palette)
# ====


if __name__ == "__main__":
    color_map = {
        "TrieSUS (single solution)": "red",
        "TrieSUS (all solutions)": "darkred",
        "Brute force (single solution)": "darkgrey",
        "Brute force (all solutions)": "grey",
    }

    df = pd.read_csv("records.tsv", header=None, sep="\t")
    df.columns = ["Method", "Sets", "Items", "Universe", "Function calls", "Seconds"]
    df["Method"] = pd.Categorical(
        df["Method"],
        categories=[
            "TrieSUS (single solution)",
            "TrieSUS (all solutions)",
            "Brute force (single solution)",
            "Brute force (all solutions)",
        ],
        ordered=True,
    )

    df["Input size parameter"] = df["Sets"].astype(str)
    df = df.sort_values(by="Sets")

    plt.clf()
    g = sns.lineplot(
        data=df,
        x="Input size parameter",
        y="Seconds",
        hue="Method",
        palette=color_map,
        hue_order=[
            "Brute force (all solutions)",
            "Brute force (single solution)",
            "TrieSUS (all solutions)",
            "TrieSUS (single solution)",
        ],
    )
    g.set(yscale="log")
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(handles[::-1], labels[::-1], frameon=False)
    sns.despine()
    plt.tight_layout()
    plt.savefig("plots/seconds_log.pdf")

    plt.clf()
    g = sns.lineplot(
        data=df,
        x="Input size parameter",
        y="Seconds",
        hue="Method",
        palette=color_map,
        hue_order=[
            "Brute force (all solutions)",
            "Brute force (single solution)",
            "TrieSUS (all solutions)",
            "TrieSUS (single solution)",
        ],
    )
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(handles[::-1], labels[::-1], frameon=False)
    sns.despine()
    plt.tight_layout()
    plt.savefig("plots/seconds.pdf")

    plt.clf()
    g = sns.lineplot(
        data=df,
        x="Input size parameter",
        y="Function calls",
        hue="Method",
        palette=color_map,
        hue_order=[
            "Brute force (all solutions)",
            "Brute force (single solution)",
            "TrieSUS (all solutions)",
            "TrieSUS (single solution)",
        ],
    )
    g.set(yscale="log")
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(handles[::-1], labels[::-1], frameon=False)
    sns.despine()
    plt.tight_layout()
    plt.savefig("plots/function_calls_log.pdf")

    plt.clf()
    g = sns.lineplot(
        data=df,
        x="Input size parameter",
        y="Function calls",
        hue="Method",
        palette=color_map,
        hue_order=[
            "Brute force (all solutions)",
            "Brute force (single solution)",
            "TrieSUS (all solutions)",
            "TrieSUS (single solution)",
        ],
    )
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(handles[::-1], labels[::-1], frameon=False)
    sns.despine()
    plt.tight_layout()
    plt.savefig("plots/function_calls.pdf")
