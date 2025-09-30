from json import loads
from argparse import ArgumentParser

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
import seaborn as sns

import IO_functions


# Default col names for Boston dataset
BOSTON_COL_NAMES = [
    "Potato",
    "Tomato",
    "Cabbage",
    "Apple",
    "Grape",
    "Orange",
    "Banana",
    "Watermelon",
    "Carrot",
    "Onion",
    "Strawberry"
]


def parse_args():
    parser = ArgumentParser(
        description="This script compute covariation over the given dataset and compare it with correlation to show the difference"
    )
    parser.add_argument("--read_csv_kwargs", type=loads,
                        help="Parameters for read_csv function. Refer to pandas.read_csv documentation for more information. Default is parameters for Boston dataset",
                        default={"filepath_or_buffer": "http://lib.stat.cmu.edu/datasets/boston",
                                 "sep": "\\s+",
                                 "skiprows": 22,
                                 "header": None,
                                 "names": BOSTON_COL_NAMES})
    parser.add_argument("--figsize", type=float, nargs=2, default=[14.4, 7.2],
                        help="Size of the figure with heatmaps in inches. Default: height = 14.4, width = 7.2")
    parser.add_argument("--output", type=str, default=None,
                        help="Absolute path to a file where to save the figure with heatmaps. Don't save if it's not set. File format: <fname>.[png, jpg, jpeg]")
    parser.add_argument("--show", action="store_true",
                        help="If it's set then show heatmaps on the display")
    return parser.parse_args()


def custom_corr(cov_matrix: pd.DataFrame, df: pd.DataFrame) -> pd.DataFrame:
    """
    Custom function for computing correlation to show how it's connected with covariation.

    Args:
        cov_matrix (pd.Dataframe): Covariation matrix of df
        df (pd.DataFrame): Dataframe itself

    Returns:
        pd.DataFrame: Correaltion matrix = cov(x, y) / sqrt(Var(x) * Var(y))
    """
    corr_matrix = cov_matrix.copy()
    df_vars = df.var(numeric_only=True)
    for row in corr_matrix.index:
        corr_matrix[row] = corr_matrix[row] / np.sqrt(df_vars[row] * df_vars)
    return corr_matrix


def draw_heatmaps(cov_matrix: pd.DataFrame, corr_matrix: pd.DataFrame, figsize: list[float]) -> Figure:
    """Just create a figure and draw two heatmaps on it using seaborn library"""
    fig, axs = plt.subplots(nrows=1, ncols=2, layout="constrained", figsize=figsize)
    axs[0].set_title("Covariation")
    sns.heatmap(cov_matrix, annot=True, ax=axs[0])
    axs[1].set_title("Correlation = cov(x, y) / sqrt(Var(x) * Var(y)) = [-1, 1]")
    sns.heatmap(corr_matrix, annot=True, vmin=-1, vmax=1, ax=axs[1], fmt=".3f")
    return fig


def main():
    args = parse_args()
    if (args.output is not None) and (IO_functions.check_output_path(args.output) is False):
        return 1

    raw_df = IO_functions.safe_read_csv(args.read_csv_kwargs)
    if raw_df is None:
        return 2

    df = raw_df.dropna()
    cov_matrix = df.cov(numeric_only=True)
    corr_matrix = custom_corr(cov_matrix, df)
    fig = draw_heatmaps(cov_matrix, corr_matrix, args.figsize)
    if args.output is not None:
        fig.savefig(args.output)
    if args.show:
        plt.show()

    return 0


if __name__ == "__main__":
    exit(main())
