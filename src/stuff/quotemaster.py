import requests
import string
from bs4 import BeautifulSoup
from urllib.request import urlopen

URL = 'https://www.quotemaster.org/'

letters = string.ascii_uppercase

all_hrefs = []
with open('cat_hrefs.txt', 'a') as f:
    for l in letters:
        u = URL + f'?alpha={l}'
        print(u)
        header = {'User-Agent': 'Mozilla/5.0'}
        page  = urlopen(u)
        soup = BeautifulSoup(page, 'html.parser')
        # cat = soup.find_all('div', attrs={'class': ['col-sm-4']})
        cat_list = soup.find('div', {'class': ['categories-list']})
        cat_list_child = cat_list.find('div', {'class': 'row'})
        cat_list_child_4 = cat_list_child.find_all('div', {'class': 'col-sm-4'})
        for c in cat_list_child_4: 
            for cl in c.find_all('a', href=True):
                all_hrefs.append(cl['href'])
                f.write(cl['href'] + '\n')

print(all_hrefs)