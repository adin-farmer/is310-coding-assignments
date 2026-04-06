from bs4 import BeautifulSoup
import cloudscraper
import csv
import os
import time
URL = "https://slay-the-spire.fandom.com/wiki/Category:Cards"
# CATEGORY_URL = URL + ""
OUTPUT_FILE = "sts_cards.csv"

def fetch_page(url):
    scraper = cloudscraper.create_scraper()
    # soup = BeautifulSoup(response.text, "html.parser")
    try:
        response = scraper.get(url, timeout=15)
        print(f"get {URL} -> {response.status_code}")
        if response.status_code == 200:
            return BeautifulSoup(response.text, "html.parser")
        else:
            print(f" Warning: recieved status {response.status_code}")
            return None
    except Exception as e:
        print(f" error getting url: {URL}")
        return None


def fetch_categories(soup):
    categories = soup.find_all(class_="category-page__trending-page")
    # categories = table.find("category-page__trending-pages")
    for entry in categories:
        print(entry)
    return categories

def parse_cards(soup):
    all_cards = []
    rows = soup.find_all("tr")
    for row in rows:
        cols = row.find_all("td")

        if len(cols) < 7:
            continue

        name = cols[1].get_text(strip=True)
        rarity = cols[3].get_text(strip=True)
        card_type = cols[4].get_text(strip=True)
        energy = cols[5].get_text(strip=True)
        description = cols[6].get_text(strip=True)

        all_cards.append({
            "Name": name,
            "Rarity": rarity,
            "Type": card_type,
            "Energy": energy,
            "Description": description
        })

    return all_cards

def get_cards(set):
    all_cards = []
    for each in cats:
        link = each.find("a").get("href")
        abs_link = f"https://slay-the-spire.fandom.com{link}"
        second_soup = fetch_page(abs_link)
        if second_soup:
            cards = parse_cards(second_soup)
            all_cards.extend(cards)
        time.sleep(1)
    return all_cards
        
if __name__ == "__main__":
    soup = fetch_page(URL)
    cats = fetch_categories(soup)
    cards = get_cards(cats)
    fieldnames = ["Name", "Rarity", "Type", "Energy", "Description"]

    if cards:
        with open(OUTPUT_FILE, "wt", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fieldnames)
            for card in cards:
                writer.writerow([card["Name"], card["Rarity"], card["Type"], card["Energy"], card["Description"]])
        print(f"Saved {len(cards)} to {OUTPUT_FILE}")
