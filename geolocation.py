# geolocation.py

from math import tan, radians
from geopy.distance import distance

def locate_transmitter(
    station_lat,
    station_lon,
    azimuth,
    elevation,
    virtual_height
):

    # Calculate ground distance
    ground_distance = virtual_height / tan(radians(elevation))

    station = (station_lat, station_lon)

    destination = distance(
        kilometers=ground_distance
    ).destination(
        station,
        azimuth
    )

    return {
        "distance": round(ground_distance, 2),
        "latitude": round(destination.latitude, 6),
        "longitude": round(destination.longitude, 6)
    }