from zipfile import ZipFile
import os

ARCHIVE_DIR_LOCATION = '.' # CURRENT DIR
ARCHIVE_EXTENSION = '.zip'
EXTRACT_DIR_ROOT = os.path.join(os.getcwd(), 'extract_dir')

def get_dir_list(path='.', search=''):
    list_dir = [name for name in os.listdir(path) if os.path.isdir(name) and search in name]
    return list_dir

ld = get_dir_list(path=ARCHIVE_DIR_LOCATION)

for d in ld:
    for root, d_names, f_names in os.walk(d):
        for f_name in filter(lambda x: x.endswith(ARCHIVE_EXTENSION), f_names):
            with ZipFile(os.path.join(root, f_name), 'r') as zipObj:
                new_extract_dir = os.path.splitext(os.path.join(EXTRACT_DIR_ROOT, root, f_name))[0]
                zipObj.extractall(new_extract_dir)
                print(new_extract_dir)
