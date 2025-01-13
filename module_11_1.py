import requests
import numpy as np
from random import randint

URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": "55.75222",
    "longitude": "37.61556",
    "daily": "temperature_2m_min,temperature_2m_max,precipitation_sum",
    "timezone": "Europe/Moscow"}

response = requests.get(URL, params=params)
if response.status_code == 200:
    data = response.json()
    tomorrow_temp_min = data['daily']['temperature_2m_min'][1]
    tomorrow_temp_max = data['daily']['temperature_2m_max'][1]
    tomorrow_precipitation = data['daily']['precipitation_sum'][1]

    print(f"Прогноз погоды в Москве на завтра:")
    print(f"Минимальная температура: {tomorrow_temp_min}°C")
    print(f"Максимальная температура: {tomorrow_temp_max}°C")
    print(f"Ожидаемое количество осадков: {tomorrow_precipitation} мм")
else:
    print(f"Ошибка {response.status_code}: {response.text}")

# Сумма элементов массива. Минимальный и максимальный элемент
matrix = np.random.randint(-100, 100, size=(4, 4))

print(matrix)
print()
print(f'{matrix.sum()} - сумма всех элементов массива')
print(f'{matrix.min()} - минимальный элемент массива')
print(f'{matrix.max()} - максимальный элемент массива')
