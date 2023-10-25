from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

URLS = [
    # 'https://www.imobiliare.ro/vanzare-case-vile/brasov/sacele/casa-de-vanzare-4-camere-X8IH1107V'
    'https://www.imobiliare.ro/vanzare-case-vile/brasov/sacele/casa-de-vanzare-3-camere-XBOD0100U'
]

def prepare_soup(url: str):
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req)
    soup = BeautifulSoup(page, features="html.parser")
    return soup

def get_price(soup: BeautifulSoup):
    # print(soup)
    with open('out.txt', 'w') as file:
        file.write(str(soup))
    price = soup.select("div.pret.first.dl_infotip_pret_fix.tooltipstered")
    # price = soup.select(".pret_desc.tooltipstered")
    print(f'price: {price}')
    return price



if __name__ == '__main__':
    print('Start')
    site = URLS[0]
    soup = prepare_soup(site)
    price = get_price(soup)
    # print(price)