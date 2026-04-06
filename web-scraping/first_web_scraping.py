from bs4 import BeautifulSoup
import requests

response = requests.get("https://gutenberg.org/browse/scores/top")
print("Status code:", response.status_code) # Checking the reponse codes at the beginning is always good practice
print("Headers:", response.headers)
print("Content:", response.text[:500])

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify()[:500])

data = []

headers = soup.find_all('h2')
for header in headers:
    if "Top" in header.get_text():
        data.append({"title": top_header, "items": []})
        list_of_links = header.get_text()
        for link in list_of_links:
            if "ebooks" in link.get("href"):

                if "Top 100 EBooks yesterday" in top_header:
                    complete_url = "https://www.gutenberg.org" + link.get('href')
                    print(complete_url)
                    response2 = requests.get(complete_url)
                    if response2.status_cod != 200:
                        print("Not working, complete_url")