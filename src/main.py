import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"❌ Gagal ambil data, status: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, "lxml")
    titles = [h2.get_text(strip=True) for h2 in soup.find_all("h2")]
    return titles

def save_to_csv(data, filename="data/output.csv"):
    df = pd.DataFrame(data, columns=["Judul"])
    df.to_csv(filename, index=False)
    print(f"✅ Data disimpan di {filename}")

if __name__ == "__main__":
    url = "https://example.com"
    data = scrape_data(url)
    if data:
        save_to_csv(data)
