import csv

airport_dict = {}

with open('/home/eytan/Codes/WebScraping/Flights/airports.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        city = row['municipality']
        country = row['iso_country']
        iata_code = row['iata_code']
        state = row['iso_region'] if 'iso_region' in row else None

        
        if city not in airport_dict:
            airport_dict[city] = {
                'country': country,
                'state': state,
                'airports': []
            }
        
        if iata_code:  
            airport_dict[city]['airports'].append(iata_code)

def FindAirport(country, airport_dict):
    airports_in_country = []
    
    for city, info in airport_dict.items():
        if info['country'] == country:
            airports_in_country.extend(info['airports'])
    
    return airports_in_country

