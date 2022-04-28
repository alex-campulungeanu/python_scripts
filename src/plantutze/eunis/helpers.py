from datetime import datetime
from bs4 import BeautifulSoup

def get_current_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
# TODO: ENABLE_LOGGER i can pass it as a cli parameter
def logger(str, ENABLE_LOGGER=False):
    if ENABLE_LOGGER:
        print(str)

def log_error(message, error_file):
    with open(error_file, 'a') as file:
        file.write(f'{get_current_time()} : {message}\n')

def extract_data_text(souped_page: BeautifulSoup):
    ret = dict({
        'gen': '',
        'autorul': '',
        'specia': '',
        'subspecia': '',
        'varietatea': '',
        'phylum': '', #increngatura #2 (sau division)
        'clasa': '', #clasa #3
        'order': '', #ordin #4
        'family': '', #familia #5
    })
    gen = ''
    autorul = ''
    specia = ''
    subspecia = ''
    varietatea = ''
    phylum = ''
    clasa = ''
    order = ''
    family = ''
    # italic data
    title_italics = souped_page.select('div[id="content"] h1 span.italics')
    logger(f'title_italics: {title_italics}')
    title_italics_content = title_italics[0].text.strip()
    # title_italics_content = 'Trisetum specia subsp. subspecia var. varietatea'
    # title_italics_content = 'Romulea rosea var. australis'
    logger(f'title_italics_content: {title_italics_content}')
    gen = title_italics_content.split()[0]
    title_italics_content_second = " ".join(title_italics_content.split()[1:])
    logger(f'title_italics_content_second: {title_italics_content_second}')
    if 'subsp.' in title_italics_content_second and 'var.' in title_italics_content_second:
        specia = title_italics_content_second.split('subsp.')[0]
        subspecia = "".join(title_italics_content_second.split('subsp.')[1]).split('var.')[0]
        varietatea = "".join(title_italics_content_second.split('subsp.')[1]).split('var.')[1]
    elif 'subsp.' in title_italics_content_second:
        specia = title_italics_content_second.split('subsp.')[0]
        subspecia = title_italics_content_second.split('subsp.')[1]
    elif 'var.' in title_italics_content_second:
        specia = title_italics_content_second.split('var.')[0]
        varietatea = title_italics_content_second.split('var.')[1]
    else:
        specia = title_italics_content_second
    # TODO: fix next error "text" is not a known member of "None"
    autorul = title_italics[0].next_sibling.text.strip()
    # breadcrumbs data
    phylum = souped_page.select('span[id="breadcrumbs-2"] a')[0].text.strip()
    clasa = souped_page.select('span[id="breadcrumbs-3"] a')[0].text.strip()
    order = souped_page.select('span[id="breadcrumbs-4"] a')[0].text.strip()
    family = souped_page.select('span[id="breadcrumbs-5"] a')[0].text.strip()
    logger(f'phylum: {phylum}')
    logger(f'clasa: {clasa}')
    logger(f'order: {order}')
    logger(f'family: {family}')
    ret['gen'] = gen
    ret['specia'] = specia
    ret['subspecia'] = subspecia
    ret['varietatea'] = varietatea
    ret['autorul'] = autorul
    ret['phylum'] = phylum
    ret['clasa'] = clasa
    ret['order'] = order
    ret['family'] = family
    return ret
