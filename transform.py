from datetime import datetime, timezone

def transform_weather(data):
    print("DEBUG - Raw data to transform:", data)
    city = data.get("name")
    main = data.get("main", {})
    weather = data.get("weather")[0] if data.get("weather") else {}
    row = {
        "city_name": city,
        "temp_celsius": main.get("temp"),
        "humidity": main.get("humidity"),
        "weather_description": weather.get("description"),
        "obs_timestamp": datetime.fromtimestamp(data.get("dt", 0), tz=timezone.utc)
    }
    print("DEBUG - Transformed row:", row)
    return row