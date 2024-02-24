import requests
from bs4 import BeautifulSoup


class RozetkaParser:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

    def parse_category(self):
        with open("discounted_products.txt", "w", encoding="UTF-8") as file:
            for page_num in range(1, 20):
                print(f"Parsing page {page_num}...")
                url = f"{self.url}p-{page_num}/"
                response = self.session.get(url, headers=self.header)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")
                    products = soup.find_all('div', class_="product-card")

                    for product in products:
                        try:
                            title = product.find("a", class_="product-card__title").text.strip()
                            price = product.find("div", class_="v-pb__cur discount").text.strip()
                            file.write(f"{title}: {price}\n")
                            print(f"Found discounted product: {title} - {price}")
                        except AttributeError:
                            pass

if __name__ == "__main__":
    url = 'https://rozetka.com.ua/logitech_910_005880/p269114036/'
    parser = RozetkaParser(url)
    parser.parse_category()