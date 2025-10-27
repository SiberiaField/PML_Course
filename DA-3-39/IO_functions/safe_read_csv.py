import pandas as pd


def safe_read_csv(data_path: str, read_csv_kwargs: dict) -> pd.DataFrame | None:
    """
    This function reads dataframe using given kwargs which are passed directly into pandas.read_csv function.\n
    It returns pd.DataFrame if there are no troubles and it returns None if there are.
    """
    try:
        df = pd.read_csv(data_path, **read_csv_kwargs)
        if df.empty:
            print("Dataset is empty or doesn't contain any data")
        return df
    except FileNotFoundError:
        print("Unable to download a dataset")
        return None
    except pd.errors.ParserError as e:
        print(f"Parsing error during reading dataset: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error during reading dataset: {e}")
        return None
