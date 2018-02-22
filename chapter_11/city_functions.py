def format_city(city, country, population=''):
    """Generate a formatted city with country name"""
    if population:
        formatted_city = city + ', ' + country + ' - population ' + population
    else:
        formatted_city = city + ', ' + country
    return formatted_city.title()