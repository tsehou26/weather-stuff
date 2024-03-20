import requests
api_key = '5d55880eb3bc0934b23efec146bb96e3'
base_url = 'http://api.openweathermap.org/data/2.5/weather'
city_names = ['Kaohsiung', 'Berkeley']

html_content = f"""
<html>
<head>
    <title>Weather Information</title>
</head>
<body>
"""

for city_name in city_names:
    url = f"{base_url}?q={city_name}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        html_content += f"""
        <h1>Weather data for {city_name}:</h1>
        <p>Temperature: {round(data['main']['temp'] - 273.15, 2)} C</p>
        <p>Weather: {data['weather'][0]['description']}</p>
        <p>Humidity: {data['main']['humidity']}</p>
        <p>Wind Speed: {data['wind']['speed']} m/s</p>
        """
    else:
        html_content += f"Error retrieving weather data for {city_name}"
    if city_name != city_names[-1]:
        html_content += "<p>&nbsp</p>"
html_content += """
</body>
</html>
"""

with open('today_weather.html', 'w') as file:
    file.write(html_content)