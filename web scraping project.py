import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.scrapethissite.com/pages/simple/"
resp = requests.get(url)

soup = BeautifulSoup(resp.text, "lxml")
countries = soup.find_all("div", class_="country")

with open("countries_data.csv", mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Country", "Capital", "Population", "Area_km2"])
    
    for c in countries:
        name = c.find("h3", class_="country-name").get_text(strip=True)
        capital_tag = c.find("span", class_="country-capital")
        population_tag = c.find("span", class_="country-population")
        area_tag = c.find("span", class_="country-area")
        
        capital = capital_tag.get_text(strip=True) if capital_tag else ""
        population = population_tag.get_text(strip=True) if population_tag else ""
        area = area_tag.get_text(strip=True) if area_tag else ""
        
        writer.writerow([name, capital, population, area])

print("Done — data saved in countries_data.csv")
