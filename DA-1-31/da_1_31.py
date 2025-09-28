from json import loads
from argparse import ArgumentParser

import pandas as pd


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


def safe_read_csv(read_kwargs: dict) -> pd.DataFrame | None:
    """
    This function reads dataframe using given kwargs which are passed directly into pandas.read_csv function.\n
    It returns pd.DataFrame if there are no troubles and it returns None if there are.
    """
    try:
        df = pd.read_csv(**read_kwargs)
        if df.empty:
            print("Файл пустой или не содержит данных")
        return df
    except FileNotFoundError:
        print("Невозможно скачать датасет")
        return None
    except pd.errors.ParserError as e:
        print(f"Ошибка парсинга: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None


def parse_args():
    parser = ArgumentParser(
        description="This program reads dataset via pandas.read_csv function, computes variances over each column and prints the three highest results")
    parser.add_argument("--read_csv_kwargs", type=loads,
                        help="Parameters for read_csv function. Refer to pandas.read_csv documentation for more information. Default is parameters for Boston dataset",
                        default={"filepath_or_buffer": "http://lib.stat.cmu.edu/datasets/boston",
                                 "sep": "\\s+",
                                 "skiprows": 22,
                                 "header": None,
                                 "names": BOSTON_COL_NAMES})
    return parser.parse_args()


def main():
    raw_df = safe_read_csv(parse_args().read_csv_kwargs)
    if raw_df is not None:
        df = raw_df.dropna()
        df_vars = df.var(numeric_only=True)
        df_sorted = df_vars.sort_values(ascending=False)
        print(df_sorted[:3])


if __name__ == "__main__":
    main()
