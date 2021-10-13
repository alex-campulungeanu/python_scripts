import os
from glob import glob

PATH = os.path.join(os.getcwd(), 'client', 'src')
LINE = '// @ts-nocheck'

for x in os.walk(PATH):
  for y in glob(os.path.join(x[0], '*.ts')):
    with open(y, 'r+') as file:
      print(file)
      old = file.read()
      first_line = old.split('\n')[0]
      print(first_line)
      if first_line != LINE:
        file.seek(0)
        file.write(f'{LINE}\n' + old)
  #     break
  # break