import requests
from bs4 import BeautifulSoup

def scrape_bbc_technology_and_science():
    url_technology = "https://www.bbc.co.uk/news/technology"
    url_science = "https://www.bbc.co.uk/news/science_and_environment"

    scrape_section(url_technology, "Technology")
    scrape_section(url_science, "Science")

def scrape_section(url, section_name):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        article_titles = soup.find_all("h3", class_="gs-c-promo-heading__title")

        if not article_titles:
            print(f"No articles found on the BBC News {section_name} section.")
        else:
            print(f"Latest articles in the BBC News {section_name} section:")
            for index, title in enumerate(article_titles, start=1):
                print(f"{index}. {title.text.strip()}")
    else:
        print("Failed to retrieve the webpage. Please check your internet connection.")

if __name__ == "__main__":
    scrape_bbc_technology_and_science()
