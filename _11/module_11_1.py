import pandas as pd
import numpy as np

#генерация дат
dates = pd.date_range(end=pd.Timestamp.today(), periods=30).strftime('%Y-%m-%d')
#cлучайные данные для столбцов
temperatures = np.random.randint(-20, 2, size=30)
precipitation = np.random.uniform(0, 5, size=30).round(1)
wind_speed = np.random.uniform(0, 10, size=30).round(1)
cloudiness = np.random.randint(0, 101, size=30)

#создание DataFrame
weather_data = pd.DataFrame({
    "Дата": dates,
    "Температура (°C)": temperatures,
    "Осадки (мм)": precipitation,
    "Скорость ветра (м/с)": wind_speed,
    "Облачность (%)": cloudiness
})

#изменение и проверка типа данных
weather_data["Дата"] = pd.to_datetime(weather_data["Дата"])
print(weather_data.dtypes)

#для отображения всех столбцов
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#вывод первых трёх строк таблицы
print(weather_data.head(n=3))

#быстрый анализ данных
print(weather_data.describe())

#нахождение среднего значения по одному из столбцов
print('Средняя температура: ', weather_data["Температура (°C)"].mean())

#фильтрация по значениям выше(больше) среднего
print(weather_data[weather_data['Температура (°C)'] > weather_data["Температура (°C)"].mean()])

#сортировка от большего к меньшему
print(weather_data.sort_values('Осадки (мм)', ascending=False).head())

#сохранение в CSV
weather_data.to_csv("weather_moscow.csv", index=False)