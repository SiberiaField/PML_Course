import os

import pandas as pd
from dotenv import load_dotenv


# Загружаем DATA_URL из .env файла
load_dotenv()


def safe_read_csv():
    """
    This function reads dataframe from DATA_URL environment variable and returns None if some troubles appear
    """
    try:
        # Удалить первые 22 строки предалагет сам sklearn при попытке
        # Скачать датасет через него. Видимо, эти первые строки отличаются от строк дальше
        # Из-за чего просиходит ошибка чтения
        df = pd.read_csv(os.getenv("DATA_URL"), sep="\s+", skiprows=22, header=None)
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
    df = raw_df.dropna()
    df_vars = df.var()
    df_sorted = df_vars.sort_values(ascending=False)
    print(df_sorted[:3])


if __name__ == "__main__":
    main()
