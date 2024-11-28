import pandas as pd
import matplotlib.pyplot as plt

# 데이터 읽기
data = pd.read_csv("city_temperature.csv")

# 데이터 정리
city = input("Enter city name: ")
city_data = data[data["City"] == city]

# 시각화
plt.figure(figsize=(10, 5))
plt.plot(city_data["Month"], city_data["AvgTemperature"], label="Avg Temperature", marker="o")
plt.title(f"Average Monthly Temperature in {city}")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.legend()
plt.show()
