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
        'author': '',
        'specia': '',
        'sub_specia': '',
        'varietatea': '',
    })
    varietatea = ''
    title_italics = souped_page.select('div[id="content"] h1 span.italics')
    # logger(f'title_italics: {title_italics}')
    title_italics_content = title_italics[0].text.strip()
    # title_italics_content = 'Romulea rosea var. australis'
    logger(f'title_italics_content: {title_italics_content}')
    gen = title_italics_content.split()[0]
    title_italics_content_second = " ".join(title_italics_content.split()[1:])
    logger(f'title_italics_content_second: {title_italics_content_second}')
    specia = title_italics_content_second.split('subsp.')[0]
    if specia == '':
        specia = title_italics_content_second.split('var. ')[0]
    logger(f'specia: {specia}')
    try:
        sub_specia = title_italics_content_second.split('subsp.')[1]
        logger(f'sub_specia: {sub_specia}')
    except IndexError as e:
        try:
            varietatea = title_italics_content_second.split('var.')[1]
        except IndexError as e2:
            varietatea = ''
        sub_specia = ''
    # TODO: fix next error "text" is not a known member of "None"
    author = title_italics[0].next_sibling.text.strip()
    ret['gen'] = gen
    ret['specia'] = specia
    ret['sub_specia'] = sub_specia
    ret['varietatea'] = varietatea
    ret['author'] = author
    return ret
