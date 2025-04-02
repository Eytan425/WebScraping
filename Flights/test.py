import airportCodes

destination = input("Where would you like to go? ")
airports = airportCodes.FindAirport(destination, airportCodes.airport_dict)
if airports:
    for codes in airports:
        print(codes)

    
    iata = input("Choose which one from above: ")
    if(iata in airports):
        print(iata)
    else:
        print("None were found")
else:
    print("None found")

