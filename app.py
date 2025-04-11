from catboost.datasets import titanic
import pandas as pd

# Загрузка данных
train_df, _ = titanic()

# Сохранение в CSV
# train_df.to_csv("titanic.csv", index=False)
df = train_df[["Pclass", 'Sex', 'Age']]
df.to_csv("titanic.csv", index=False)