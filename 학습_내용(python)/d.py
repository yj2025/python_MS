import requests
import json

city = "Suwon"
apikey = "4da9533d78f44fe23b6fe73a2395beca"
lang = "kr"
# units = metric
# api = "http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}"
api = f"""http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"""
# api2 = https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
print(api)

result = requests.get(api)
data = result.text
data2 = json.loads(data)
print(data)
print(type(data))
print(data2)
print(type(data2))

print(data2["name"], "의 날씨입니다.")
print(f'날씨는 {data2['weather'][0]['description']} 입니다.')
print("현재 온도는 ",data2["main"]["temp"],"입니다.")
print("하지만 체감 온도는 ",data2["main"]["feels_like"],"입니다.")
# 최저 기온 : main - temp_min
print("최저 기온은 ",data2["main"]["temp_min"],"입니다.")
# 최고 기온 : main - temp_max
print("최고 기온은 ",data2["main"]["temp_max"],"입니다.")
# 습도 : main - humidity
print("습도는 ",data2["main"]["humidity"],"입니다.")
# 기압 : main - pressure
print("기압은 ",data2["main"]["pressure"],"입니다.")
# 풍향 : wind - deg
print("풍향은 ",data2["wind"]["deg"],"입니다.")
# 풍속 : wind - speed
print("풍속은 ",data2["wind"]["speed"],"입니다.")