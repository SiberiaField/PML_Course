import os

from dotenv import load_dotenv
import pandas as pd


# Читаем DATA_URL из .env файла
load_dotenv()


# Так как Boston датасет не содрежит имён колонок,
# вот один из варинатов наименования.
COL_NAMES = [
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


def safe_read_csv() -> pd.DataFrame | None:
    """
    This function reads dataframe from DATA_URL environment variable.\n
    It returns pd.DataFrame if there are no troubles and it returns None if there are.
    """
    url = os.getenv("DATA_URL")
    if url is None or url == "":
        print("Переменная окружения DATA_URL не определена или содержит пустую строку")
        return None

    try:
        # Параметры этого метода, в частности, skiprows=22,
        # были взяты из рекомендации от sklearn по установке датасета Boston.
        # То есть, эти параметры подобраны исключительно под Boston датасет.
        df = pd.read_csv(url, sep="\s+", skiprows=22, header=None, names=COL_NAMES)
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


def main():
    raw_df = safe_read_csv()
    if raw_df is not None:
        df = raw_df.dropna()
        df_vars = df.var(numeric_only=True)
        df_sorted = df_vars.sort_values(ascending=False)
        print(df_sorted[:3])


if __name__ == "__main__":
    main()
