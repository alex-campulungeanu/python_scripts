from PIL import Image
import os
import glob

QUALITY = 50
ORIGINAL = 'original'
DECREASED = 'decreased'
RESIZED_RENAME = '_resized'
SIZE = 640, 480

if __name__ == '__main__':
	data = []
	data_path = os.path.join(f'./{ORIGINAL}', '*g')
	files = glob.glob(data_path)
	for file in files:
		file_name = file.rsplit('/', 1)[1].split('.', 1)[0]
		print(file_name)
		img = Image.open(file)
		width, height = img.size
		img_resized = img.resize(SIZE, Image.ANTIALIAS)
		img_resized.save(f'./{DECREASED}/{file_name}{RESIZED_RENAME}.jpg', optimize=True, quality=QUALITY)