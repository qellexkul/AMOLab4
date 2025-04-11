from catboost.datasets import titanic
import pandas as pd

# Загрузка данных
train_df, _ = titanic()

# Чтение данных
df = pd.read_csv("date/processed_features.csv")

# One-hot encoding для признака Sex
df = pd.get_dummies(df, columns=['Sex'], drop_first=True)

# Сохранение нового датасета
df.to_csv("date/final_dataset.csv", index=False)