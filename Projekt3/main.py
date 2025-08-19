"""
main.py: třetí projekt do Engeto Online Python Akademie

author: Jana Barotová
email: jana.barotova@seznam.cz
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

def get_towns(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    towns = []

    rows = soup.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        if len(cells) > 0:
            code = cells[0].text.strip()
            name = cells[1].text.strip()
            link_tag = cells[0].find("a")
            if link_tag:
                town_url = "https://www.volby.cz/pls/ps2017nss/" + link_tag["href"]
                towns.append([code, name, town_url])
    return towns

def scrape_town(code, name, url):
    r = requests.get(url)
    s = BeautifulSoup(r.text, "html.parser")

    voters = s.find("td", {"headers": "sa2"}).text.strip().replace("\xa0", "")
    envelopes = s.find("td", {"headers": "sa3"}).text.strip().replace("\xa0", "")
    valid = s.find("td", {"headers": "sa6"}).text.strip().replace("\xa0", "")

    data = {
        "code": code,
        "name": name,
        "registered": voters,
        "envelopes": envelopes,
        "valid": valid
    }

    party_rows = s.find_all("tr")
    for row in party_rows:
        cells = row.find_all("td")
        if len(cells) == 5:
            party = cells[1].text.strip()
            votes = cells[2].text.strip().replace("\xa0", "")
            data[party] = votes

    return data

def main():
    if len(sys.argv) != 3:
        print("Chyba, výstup musí být v tomto formátu: python main.py <url_okresu> <vystupni_soubor.csv>")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]

    if not url.startswith("https://www.volby.cz/pls/ps2017nss/"):
        print("Chyba: první argument musí být platný odkaz na volby.cz.")
        sys.exit(1)

    response = requests.get(url)
    if response.status_code != 200:
        print("Chyba: stránku se nepodařilo načíst. Zkontrolujte URL.")
        sys.exit(1)
    towns = get_towns(url)
    print("Nalezeno obcí:", len(towns))

    results = []
    all_parties = set()

    first_data = scrape_town(*towns[0])
    all_parties.update([k for k in first_data.keys() if k not in ("code","name","registered","envelopes","valid")])
    results.append(first_data)

    for town in towns[1:]:
        code, name, town_url = town
        print("Stahuji:", name)
        data = scrape_town(code, name, town_url)
        all_parties.update([k for k in data.keys() if k not in ("code","name","registered","envelopes","valid")])
        results.append(data)

    columns = ["code", "name", "registered", "envelopes", "valid"] + sorted(all_parties)
    df = pd.DataFrame(results)
    df = df.reindex(columns=columns)

    df.to_csv(output_file, index=False, encoding="utf-8-sig", sep=";")
    print("Úloha dokončena. Data uložená v souboru:", output_file)

if __name__ == "__main__":
    main()