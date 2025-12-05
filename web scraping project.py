from bs4 import BeautifulSoup
import requests
import csv

date = input("Please enter a Date in the following formate MM/DD/YYYY: ")

page = requests.get(f"https://www.yallakora.com/match-center?date={date}")

def main(page):
    soup = BeautifulSoup(page.content, "lxml")
    matches_details = []

    arabCups = soup.find_all("div", class_="matchCard")

    def get_match_info(card):
        title = card.find("div", class_="title").find("h2").text.strip()

        all_matches = card.find_all("div", class_="item")

        for match in all_matches:
            try:
                team_A = match.find("div", class_="teamA").find("p").text.strip()
                team_B = match.find("div", class_="teamB").find("p").text.strip()

                result_section = match.find("div", class_="MResult")
                score_spans = result_section.find_all("span", class_="score")

                score = f"{score_spans[0].text.strip()} - {score_spans[1].text.strip()}"
                time = result_section.find("span", class_="time").text.strip()

                matches_details.append({
                    "نوع البطولة": title,
                    "الفريق الاول": team_A,
                    "الفريق الثاني": team_B,
                    "معاد المباراه": time,
                    "النتيجة": score
                })

            except:
                continue

    for card in arabCups:
        get_match_info(card)

    if matches_details:
        keys = matches_details[0].keys()
        with open("matches-details.csv", "w", newline="", encoding="utf-8") as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(matches_details)
        print("file created successfully")
    else:
        print("No matches found for that date")

main(page)
