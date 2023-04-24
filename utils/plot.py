import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

GREY = '#f4f4f4'
COLOR = '#355778'


def generate_mosaic(names: list[str]) -> list:
    col_per_row = 4
    n_rows = int(np.ceil(len(names) / col_per_row))
    mosaic = names.copy()
    mosaic += [''] * int((n_rows * col_per_row) - len(mosaic))
    return np.reshape(mosaic, (n_rows, col_per_row)).tolist()


def plot_split_pie(df, ax_names='name', save=None):
    """Plot that pie chart

    Args:
        df (_type_):
        ax_names (str, optional): a column in the dataframe that represent an id for each subplot axis. Defaults to 'name'.
        save (_type_, optional): _description_. Defaults to None.
    """

    cummulative = 0
    mosaic = generate_mosaic(df[ax_names].tolist())
    row_height = 2.5
    fig, axs = plt.subplot_mosaic(mosaic, figsize=(8, len(mosaic) * row_height), dpi=250)
    for i, row in df.iterrows():
        focus = row['value']
        other = df['value'].sum() - focus
        angle = (cummulative / df['value'].sum()) * 360

        axs[row[ax_names]].set_title(row[ax_names])
        axs[row[ax_names]].pie([focus, other],
                               wedgeprops={
                                   'edgecolor': 'white',
                                   'linewidth': 0.5,
                                   'width': 0.6,
                               },
                               colors=[COLOR, GREY] * len(df),
                               startangle=angle,
                               counterclock=True)
        cummulative += row['value']

    if '' in axs:
        axs[''].set_axis_off()
    if save:
        plt.savefig(save, dpi=200)
    plt.show()