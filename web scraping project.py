from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.scrapethissite.com/pages/simple/"

page = requests.get(url)

def main(page):
    soup = BeautifulSoup(page.content, "lxml")
    container = soup.find_all("div" , class_="row")[3:]
    countriesDetails = []
    
    def getRowInfo(row):
        countriesRow = row.find_all("div" , class_="country")
        
        for country in countriesRow:
            countryName = country.find("h3").text.strip()
            capital = country.find("div" , class_="country-info").find("span" , class_="country-capital").text.strip()
            population = country.find("div" , class_="country-info").find("span" , class_="country-population").text.strip()
            area = country.find("div" , class_="country-info").find("span" , class_="country-area").text.strip()
            
            countriesDetails.append({
                "Country Name" : countryName,
                "Capital" : capital,
                "Population" : population,
                "Area" : area
            })

    for countryRow in container:
        getRowInfo(countryRow)
    
    if countriesDetails:
        keys = countriesDetails[0].keys()
        with open("countries-details.csv", "w", newline="", encoding="utf-8") as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(countriesDetails)
        print("file created successfully")
    else:
        print("No matches found for that date")
    


main(page)