from fastapi import FastAPI
from energy_usage_optimizer_api.weather import get_weather_forecast_from_openweathermap, VirtualWeatherStation, WeatherForecast

app = FastAPI()

@app.get("/")
def index():
    return {"details": "Hi, there."}

@app.post("/weather_forecast")
async def get_weather_forecast(virtual_weather_station: VirtualWeatherStation) -> WeatherForecast:
    result = await get_weather_forecast_from_openweathermap(virtual_weather_station)
    return result
