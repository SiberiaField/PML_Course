import pandas as pd

data_url = "http://lib.stat.cmu.edu/datasets/boston"
# Удалить первые 22 строки предалагет сам sklearn при попытке
# Скачать датасет через него. Видимо, эти первые строки отличаются от строк дальше
# Из-за чего просиходит ошибка чтения
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
df = raw_df.dropna()
df_vars = df.var()
df_sorted = df_vars.sort_values(ascending=False)
print(df_sorted[:3])
