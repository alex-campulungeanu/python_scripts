import requests
import time
import xlwt
from xlwt import Workbook
import sys

ORIGIN_FILE = 'genuri.txt'
RESULT_FILE = 'completate.xls'

with open(ORIGIN_FILE) as file:
    plants= file.read().splitlines()
# plants = ['Taraxacum', 'Carnatia']
# sys.exit()


## create excel file
wb = Workbook()
plant_sheet = wb.add_sheet('plants')
plant_sheet.write(0, 1, 'phylum')
plant_sheet.write(0, 2, 'clasa')
plant_sheet.write(0, 3, 'order')
plant_sheet.write(0, 4, 'family')


for idx, plant in enumerate(plants):
    print(f'Datele pentru: {plant} cu idx: {idx}')
    plant_sheet.write(idx + 1,0, plant)
    suggestion_req = requests.get(f'https://api.catalogueoflife.org/dataset/2344/nameusage/suggest?fuzzy=false&limit=25&q={plant}')
    suggestion_dict = suggestion_req.json()
    if not suggestion_dict:
        continue
    suggestions_arr = suggestion_dict['suggestions']

    genus = {}

    for suggestion in suggestions_arr:
        if suggestion['rank'] == 'genus':
            genus = suggestion
            break

    # print(genus)
    try:
        usage_id = genus['usageId']
        classification_req = requests.get(f'https://api.catalogueoflife.org/dataset/2344/taxon/{usage_id}/classification')
        classification_arr = classification_req.json()

        family = ''
        clasa = ''
        order = ''
        phylum = ''

        for classification in classification_arr:
            if classification['rank'] == 'family':
                family = classification['name']
            if classification['rank'] == 'class':
                clasa = classification['name']
            if classification['rank'] == 'order':
                order = classification['name']
            if classification['rank'] == 'phylum':
                phylum = classification['name']
        print(family)
        print(clasa)
        print(order)
        print(phylum)
        print('################')
        plant_sheet.write(idx + 1, 1, phylum)
        plant_sheet.write(idx + 1, 2, clasa)
        plant_sheet.write(idx + 1, 3, order)
        plant_sheet.write(idx + 1, 4, family)
        # time.sleep(1)
        # if idx == 10:
        #     break
    except Exception as e:
        continue

    wb.save(RESULT_FILE)