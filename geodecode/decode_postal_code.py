import pgeocode


def get_lat_lon(country:str, postal_code:str):

    nomi = pgeocode.Nominatim(country)
    query = nomi.query_postal_code(postal_code)

    data = {
        "lat": query["latitude"],
        "lon": query["longitude"]
    }

    return data

print(get_lat_lon('US', '01902'))
