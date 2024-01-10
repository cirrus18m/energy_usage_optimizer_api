
from pydantic import BaseModel
from typing import List
import httpx


class VirtualWeatherStation(BaseModel):
    lat: float = 47.869975370191305
    lon: float = 12.648035414408115
    openweathermap_api_key: str | None = None


class WeatherForecast(BaseModel):
    dt_UTC: List[int] | None
    dt_txt_UTC: List[str] | None
    clouds: List[int] | None
    temperature_K: List[float] | None
    pressure: List[int] | None
    humidity: List[int] | None
    sunrise_UTC: int | None
    sunset_UTC: int | None


async def get_weather_forecast_from_openweathermap(virtual_weather_station: VirtualWeatherStation):

    if virtual_weather_station.openweathermap_api_key is None or virtual_weather_station.openweathermap_api_key=="string":
        virtual_weather_station.openweathermap_api_key = "ENTER_YOUR_OWN_KEY_HERE"
        
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={virtual_weather_station.lat}&lon={virtual_weather_station.lon}&appid={virtual_weather_station.openweathermap_api_key}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        forecast = response.json()
    
        forecast_light = WeatherForecast(
        dt_UTC = [item['dt'] for item in forecast['list']], 
        dt_txt_UTC = [item['dt_txt'] for item in forecast['list']],            
        clouds = [item['clouds']['all'] for item in forecast['list']],
        temperature_K =  [item['main']['temp'] for item in forecast['list']],
        pressure = [item['main']['pressure'] for item in forecast['list']],
        humidity = [item['main']['humidity'] for item in forecast['list']],
        sunrise_UTC = forecast['city']['sunrise'],
        sunset_UTC = forecast['city']['sunset'], 
        )
    
    return forecast_light
   

# if __name__ == "__main__":

#     vws = VirtualWeatherStation(lat=47.869975370191305, lon=12.6, openweathermap_api_key="307789277bd8f58cb4528a316bdcd1b7")
#     forecast_light = _get_weather_forecast(vws)
#     print(forecast_light)
