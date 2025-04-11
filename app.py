from catboost.datasets import titanic
import pandas as pd

# Загрузка данных
train_df, _ = titanic()


df = pd.read_csv("date/selected_features.csv")

# Заполнение пропущенных значений
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Сохранение обработанного датасета
df.to_csv("date/processed_features.csv", index=False)