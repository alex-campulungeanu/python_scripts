from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
from loguru import logger
import re

CLONE_URL = 'https://github.com/GorvGoyl/Clone-Wars'
DOWNLOAD_DIR = 'clone_wars_projects'

def get_project_list():
    json_list = []
    page = urlopen(CLONE_URL)
    soup = BeautifulSoup(page, 'html.parser')
    tables = soup.find_all('table', limit=2)
    logger.info(tables)
    for idx_table, table in enumerate(tables):
        table_body = table.find('tbody')
        table_rows = table_body.find_all('tr')
        for idx, row in enumerate(table_rows):
            cols = row.find_all('td')
            name = cols[0].text
            live_url = cols[1].text
            if idx_table == 0:
                repo_column_idx = 3
                tech_column_idx = 4
            elif idx_table == 1:
                repo_column_idx = 2
                tech_column_idx = 3
            github_url = [url['href'] for url in cols[repo_column_idx].find_all('a')]
            tehnologies = cols[tech_column_idx].text
            json_list.append({
                'name': name,
                'live_url': live_url,
                'github_url': github_url,
                'tehnologies': tehnologies,
            })
            # if idx == 1:
            #     break
    return json_list

def extract_project_infos(url):
    # logger.info(url)
    info = re.split(r"https://(?:github.com|gitlab.com)", url)[1]
    return info.split('/')[1] + '_'+ info.split('/')[2]

def git_clone(url, name):
    logger.info(url)
    cmd = f'git clone {url} {os.path.join(DOWNLOAD_DIR, name)}'
    os.system(cmd)

# make download dir
if not os.path.isdir(DOWNLOAD_DIR):
    os.mkdir(DOWNLOAD_DIR)


if __name__=='__main__':
    project_list = get_project_list()
    not_cloned = []
    for project in project_list:
        for url in project['github_url']:
            try:
                proj_info = extract_project_infos(url)
                project_path = os.path.join(os.getcwd(), DOWNLOAD_DIR, proj_info)
                if not os.path.isdir(project_path): # and len(os.listdir(project_path)) == 0:
                    try:
                        git_clone(url, proj_info)
                    except Exception as e:
                        print(e)
            except Exception as e:
                logger.error(e)
                not_cloned.append(url)
                continue
    logger.info(not_cloned)
            
