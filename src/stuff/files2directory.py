import os
import shutil

PATH_DIR = r'/app/src/stuff/cinee'


res = []

if __name__ == "__main__":
    for file in os.listdir(PATH_DIR):
        current_file_path = os.path.join(PATH_DIR, file)
        # print(path)
        if os.path.isfile(current_file_path):
            current_file = file
            current_file_name = file.rsplit('.')[0]
            current_file_new_dir = os.path.join(PATH_DIR, current_file_name)
            os.mkdir(current_file_new_dir)
            shutil.move(current_file_path, os.path.join(current_file_new_dir, current_file))