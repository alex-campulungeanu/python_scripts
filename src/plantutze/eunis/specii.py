# TODO: sda
# - sa mormalizez stringul din baza de date (inlocuiesc spatiul cu plus: "Abies alba" => "Abies+alba")

# Trisetum flavescens ssp. flavescens var. corsicum
# Achillea nana
# Abies alba subsp. nebrodensis 
# Acinos alpinus subsp. meridionalis
# Hyparrhenia hirta ssp. hirta
# Romulea rosea var. australis

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
from helpers import log_error, logger, extract_data_text, get_current_time
from xlwt import Workbook
import argparse
from datetime import datetime
import traceback

ENABLE_LOGGER=False
SPECIES_LINK = 'https://eunis.eea.europa.eu/'

# with open(INPUT_FILE) as file:
#     species= file.read().splitlines()

def get_input_species(file):
    with open(INPUT_FILE) as file:
        species= file.read().splitlines()
    # species = [
    #     "Centaurea plumosa var. carpatica", 
    #     "Romulea rosea var. australis",
    #     "Hyparrhenia hirta ssp. hirta",
    #     'Abies alba', 
    #     'Achillea nana', 
    #     'Abies alba subsp. nebrodensis',
    #     'Acinos alpinus subsp. meridionalis',
    #     'Trisetum flavescens ssp. flavescens var. corsicum'
    # ]
    return species

## create excel file
wb = Workbook()
species_sheet = wb.add_sheet('species')
species_sheet.write(0, 0, 'numele')
species_sheet.write(0, 1, 'genul')
species_sheet.write(0, 2, 'specia')
species_sheet.write(0, 3, 'subspecia')
species_sheet.write(0, 4, 'varietatea')
species_sheet.write(0, 5, 'autorul')

def get_result_list(specie: str, result_file: str, idx: int):
    encoded_specie = urllib.parse.quote_plus(specie)
    species_sheet.write(idx + 1, 0, specie.strip())
    to_search = f'https://eunis.eea.europa.eu/species-names-result.jsp?comeFromQuickSearch=true&showGroup=true&showOrder=true&showFamily=true&showScientificName=true&showValidName=true&showOtherInfo=true&relationOp=3&searchVernacular=true&searchSynonyms=true&sort=3&ascendency=1&scientificName={encoded_specie}&Submit=Search'
    soup = BeautifulSoup(urlopen(to_search), 'html.parser')
    first_link = soup.select('table[summary="Search results"] tbody:nth-of-type(1) tr:nth-of-type(1) td:nth-of-type(4) a')
    # logger(f'first_link: {first_link}')
    first_link_href = first_link[0]['href']
    # logger(f'first_link_href: {first_link_href}')
    validation = soup.select('table[summary="Search results"] tbody:nth-of-type(1) tr:nth-of-type(1) td:nth-of-type(6) img')
    validation_alt = validation[0]['alt']
    # logger(f'validation_alt: {validation_alt}')
    species_search = f'{SPECIES_LINK}{first_link_href}'
    # logger(f'species_search: {species_search}')
    soup_species = BeautifulSoup(urlopen(species_search), 'html.parser')
    gen = ''
    author = ''
    specia = ''
    sub_specia = ''
    varietatea = ''
    # TODO: don't duplicate the ret values :(
    if (validation_alt == 'Valid species name'): # TODO: aici pot sa folosesc si culoarea green
        ret = extract_data_text(soup_species)
        gen = ret['gen']
        specia = ret['specia']
        sub_specia = ret['sub_specia']
        varietatea = ret['varietatea']
        author = ret['author']
    elif (validation_alt == 'Invalid species name'):
        redirect = soup_species.select('span[class="redirection-msg"] a')
        # logger(f'redirect: {redirect}')
        redirect_href = redirect[0]['href']
        # logger(f'redirect_href: {redirect_href}')
        redirect_search = f'{SPECIES_LINK}{redirect_href}'
        soup_redirect = BeautifulSoup(urlopen(redirect_search), 'html.parser')
        ret = extract_data_text(soup_redirect)
        gen = ret['gen']
        specia = ret['specia']
        sub_specia = ret['sub_specia']
        varietatea = ret['varietatea']
        author = ret['author']
    logger(f'gen: {gen}')
    logger(f'specia: {specia}')
    logger(f'sub_specia: {sub_specia}')
    logger(f'varietatea: {varietatea}')
    logger(f'author: {author}')
    species_sheet.write(idx + 1, 1, gen.strip())
    species_sheet.write(idx + 1, 2, specia.strip())
    species_sheet.write(idx + 1, 3, sub_specia.strip())
    species_sheet.write(idx + 1, 4, varietatea.strip())
    species_sheet.write(idx + 1, 5, author.strip())
    wb.save(result_file)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetch species from unies site')
    parser.add_argument('--user', help='The user for whom we extract data')
    parser.add_argument('--file', help='The file for analizing')
    args = parser.parse_args()
    if args.user == None:
        print('USER MUST BE FILLED !')
    if args.file == None:
        print('FILE MUST BE PROVIDED !')
    else:
        print(f'START: {get_current_time()}')
        user_analyzed = args.user
        file_analyzed = args.file
        USER = user_analyzed
        BASE_FILE = file_analyzed.rpartition('.')[0]
        print(f'Fisier analizat {file_analyzed}')
        INPUT_FILE = f'./{USER}/input/{file_analyzed}'
        RESULT_FILE = f'./{USER}/output/{BASE_FILE}_filled.xls'
        ERROR_FILE = f'./{USER}/output/{BASE_FILE}_errors.txt'
        species = get_input_species(INPUT_FILE)
        for idx, specie in enumerate(species):
            logger('\n')
            try:
                get_result_list(specie, RESULT_FILE, idx)
                print(f'{idx} {USER} {get_current_time()} -> SPECIE analizata: {specie}')
                # if idx % 5 == 0:
                #     log_error(f'health check: {idx}', ERROR_FILE)    
            except Exception as e:
                print(f'{USER} {get_current_time()} -> EROARE: {specie}')
                log_error(f'{idx} # {get_current_time()} {specie} # {traceback.format_exc()}', ERROR_FILE)
                continue
        print(f'END: {get_current_time()}')
                