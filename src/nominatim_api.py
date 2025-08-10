import requests

def get_lat_long(address):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': address,
        'format': 'json',
        'limit': 1  # get only the top result
    }
    headers = {
        'User-Agent': 'Hard_to_Heat_Homes_2.0'  # required by Nominatim usage policy
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    if data:
        lat = data[0]['lat']
        lon = data[0]['lon']
        return lat, lon
    else:
        return None, None

# Example usage
address = "10 Downing Street, London"
lat, lon = get_lat_long(address)
print(f"Latitude: {lat}, Longitude: {lon}")
