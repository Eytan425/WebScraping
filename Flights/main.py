from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
import airportCodes


driver = webdriver.Chrome()
driver.get("https://www.elal.com/eng/israel")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("El Al flights", Keys.RETURN)

origin_input = driver.find_element(By.ID, "outbound-origin-location-input")
origin_input.send_keys("TLV")

destination_input = driver.find_element(By.ID, "outbound-destination-location-input")
destination = input("Where would you like to go?")
airports = airportCodes.FindAirport(destination, airportCodes.airport_dict)
print(airportCodes)
iata = input("Choose which one from above: ")
if(iata in airports):
    destination_input.send_keys(iata.upper())


time.sleep(30)


data = pd.DataFrame({"Test": ["Success"]})
print(data)

driver.quit()


#input origin, input destination, input date, input amountOfPeople