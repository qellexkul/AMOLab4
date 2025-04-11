from catboost.datasets import titanic
import pandas as pd

# Загрузка данных
train_df, _ = titanic()

# Чтение данных
df = pd.read_csv("date/titanic.csv")

# Выбор нужных признаков
selected_features = df[['Pclass', 'Sex', 'Age']]

# Сохранение нового датасета
selected_features.to_csv("date/selected_features.csv", index=False)