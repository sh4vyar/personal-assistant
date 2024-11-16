import geocoder

def get_city():
    location = geocoder.ip('me')
    city = location.city
    return city

