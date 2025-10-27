from json import loads
from argparse import ArgumentParser

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

from IO_functions import check_output_path, safe_read_csv


def parse_args():
    parser = ArgumentParser(description="Create and analyse interaction feature")
    parser.add_argument("--data", type=str, default=None
                        help="Path to .csv file with data. Default is None and use synthetic data")
    parser.add_argument("--read_csv_kwargs", type=loads, default=None
                        help="Parameters for read_csv function. Refer to pandas.read_csv documentation for more information")
    parser.add_argument("--samples", type=int, default=1000,
                        help="Number if samples in synthetic data. Default is 1000")
    parser.add_argument("--num_col", type=str, default="numerical_feature",
                        help="Name of numerical feature. Default is 'numerical_feature'")
    parser.add_argument("--cat_col", type=str, default="categorical_feature",
                        help="Name of categorical feature. Default is 'categorical_feature'")
    parser.add_argument("--output_data", type=str, default=None,
                        help="Absolute path to file where to save the data")
    parser.add_argument("--output_plot", type=str, default=None,
                        help="Absolute path to file where to save the plot")
    parser.add_argument("--show_plot", action="store_true",
                        help="Show boxplot if flag is set")
    return parser.parse_args()


def generate_synthetic_data(num_samples: int = 1000) -> pd.DataFrame:
    np.random.seed(42)
    numerical = np.random.normal(0, 1, num_samples)
    categories = ["A", "B", "C", "D"]
    categorical = np.random.choice(categories, num_samples, p=[0.4, 0.3, 0.2, 0.1])
    return pd.DataFrame({
        "numerical_feature": numerical,
        "categorical_feature": categorical
    })


def create_interaction_feature(df: pd.DataFrame, numerical_col: str, categorical_col: str) -> pd.DataFrame:
    le = LabelEncoder()
    encoded_categorical = le.fit_transform(df[categorical_col])
    df["interaction_feature"] = df[numerical_col] * encoded_categorical
    return df


def plot_boxplot(df: pd.DataFrame, numerical_col: str, categorical_col: str, ax: plt.Axes):
    sns.boxplot(data=df, x=categorical_col, y=numerical_col, ax=ax)
    ax.set_title(f"Boxplot of {numerical_col} by {categorical_col}")


def main():
    args = parse_args()

    if (args.output_data is not None) and (check_output_path(args.output_data, "^\\w+\\.csv$") is False):
        return 1
    if (args.output_plot is not None) and (check_output_path(args.output_plot, "^\\w+\\.(?:png|jpg|jpeg)$") is False):
        return 1

    df = None
    if args.data is None:
        df = generate_synthetic_data(args.samples)
        print("Generated df:")
    else:
        df = safe_read_csv(args.data, args.read_csv_kwargs)
    print(df.head())

    df = create_interaction_feature(df, args.num_col, args.cat_col)
    print("\ndf with interaction feature:")
    print(df.head())

    if args.output_data is not None:
        df.to_csv(args.output_data, index=False)
        print(f"\nData was saved to: {args.output_data}")

    fig, axs = plt.subplots(1, 2, layout="constrained", figsize=[10, 4])
    plot_boxplot(df, "interaction_feature", args.cat_col, axs[0])
    plot_boxplot(df, args.num_col, args.cat_col, axs[1])
    if args.output_plot is not None:
        fig.savefig(args.output_plot)
    if args.show_plot:
        plt.show()

    return 0


if __name__ == "__main__":
    exit(main())
