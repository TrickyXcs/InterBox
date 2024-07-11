
import requests
from bs4 import BeautifulSoup

'''
 Потрібно створити клас який буде збирати дані за посиланням на Ebay сторінку товару,
формат даних в якому повинні повертатись дані json в тестовому завданні можна просто виводити в консоль,
або зберігати в файл. 
Обов’язкові дані це 
    назва, 
    посилання на фото, 
    саме посилання на товар,
    ціна, 
    продавець, 
    ціна доставки. 
Авжеж чим більше даних, тим краще, але в контексті тестового це не важливо.'''


class EbayParser:
    def get_soup(self, url: str) -> BeautifulSoup:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

    def parse_data(self, data):
        name = data.find("h1", class_="x-item-title__mainTitle").find("span").text
        photo_url = data.find("div", class_="image-treatment").find("img").get("src")
        item_url = data.find('meta', property='og:url').get("content")
        price_in_eur = data.find("div", class_="x-price-primary").text
        price_in_usd = data.find("div", class_="x-price-approx").find_all("span")[-1].text
        _raw_seller = data.find("div", class_="x-sellercard-atf__info__about-seller").find('a')
        seller_url = _raw_seller.get("href")
        seller_name = _raw_seller.text
        shipping_price = data.find("div", class_="d-shipping-minview").find("span", class_="ux-textspans--NEGATIVE").text

        result = {
            "title": name,
            "photo_url": photo_url,
            "item_url": item_url,
            "price": {
                "eur": price_in_eur,
                "usd": price_in_usd
            },
            "seller": {
                "title": seller_name,
                "url": seller_url
            },
            "shipping_price": shipping_price
        }

        return result
    
    def print_data(self, url):
        soup = self.get_soup(url)
        data = self.parse_data(data = soup)
        print(data)



ebay_api = EbayParser()
ebay_api.print_data(url = input("Введіть url: "))