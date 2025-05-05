import requests
import json
import pandas as pd
import os # Assuming AIRVISUAL_KEY is an environment variable
import matplotlib.pyplot as plt
import seaborn as sns

# Load city data
# Note: Might need adjustments based on the exact JSON structure
# Reading line-delimited JSON might require lines=True
AIRVISUAL_KEY = os.getenv("AIRVISUAL_KEY")

try:
    df_cidade = pd.read_json('dados_cidade.json')
    with open('dados_cidade.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    df_cidade2 = pd.json_normalize(data['listaCidades'])
    # You might need further processing if it loads as nested dicts
    # e.g., pd.json_normalize() might be useful after initial load
    print("City data loaded.")
except ValueError as e:
    print(f"Error loading dados_cidade.json: {e}")
    print("This might be due to multiple JSON objects in the file. Try loading differently or preprocessing the file.")


# Load forecast data
df_forecast_raw = pd.read_json('dados_forecast.json')

# Normalize the nested forecast data
# Extract forecastday details
df_forecast_day = pd.json_normalize(df_forecast_raw['forecast']['forecastday'][0], record_path=['hour'],
                                   meta=['date', ['day', 'maxtemp_c'], ['day', 'mintemp_c'], ['day', 'avgtemp_c'], ['day', 'totalprecip_mm'], ['astro', 'sunrise'], ['astro', 'sunset']])
print("Forecast data loaded and normalized.")

print("\nSample City Data:")
print(df_cidade.head()) # Display head if loading succeeds
print(df_cidade2.head()) # Display head if loading succeeds

print(df_cidade.columns)
print(df_cidade2.columns) # Display columns to understand structure
print("\nSample Forecast Data:")
print(df_forecast_day.head())
print(df_forecast_day.columns) # Display columns to understand structure
print(df_forecast_day.dtypes) # Display dtypes to understand structure


# Example coordinates for Belo Horizonte
# latitude = -19.9167
# longitude = -43.9333
latitude = -15.7938
longitude = -47.8827
try:
    # Construct the API URL for nearest station

    url = f"http://api.airvisual.com/v2/nearest_city?lat={latitude}&lon={longitude}&key={AIRVISUAL_KEY}"
    response = requests.get(url)
    response.raise_for_status() # Raise an exception for bad status codes
    data = response.json()

    print("Successfully fetched nearest station data:")
    print(json.dumps(data, indent=4))

    # --- Pandas Integration Example ---
    if data.get('status') == 'success' and 'data' in data:
        station_data = data['data']
        # Normalize pollution and weather data if needed
        pollution_info = pd.json_normalize(station_data['current']['pollution'])
        weather_info = pd.json_normalize(station_data['current']['weather'])

        print("\nPollution Info (DataFrame):")
        print(pollution_info)

        print("\nWeather Info (DataFrame):")
        print(weather_info)

        # Further analysis/visualization would go here

except requests.exceptions.RequestException as e:
    print(f"Error fetching data from IQAir API: {e}")
except KeyError as e:
    print(f"Error processing API response - unexpected structure: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")



# Ensure forecast data is loaded and preprocessed as df_forecast_day

# Convert time to datetime objects for better plotting
df_forecast_day['time'] = pd.to_datetime(df_forecast_day['time'])
print(df_forecast_day)
# Example Plot 1: Hourly Temperature Trend
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_forecast_day, x='time', y='temp_c', marker='o')
plt.title('Hourly Temperature Forecast for Capanema (2025-05-20)')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Example Plot 2: Chance of Rain
plt.figure(figsize=(12, 6))
sns.barplot(data=df_forecast_day, x='time', y='chance_of_rain', color='skyblue')
plt.title('Hourly Chance of Rain Forecast for Capanema (2025-05-20)')
plt.xlabel('Time')
plt.ylabel('Chance of Rain (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()