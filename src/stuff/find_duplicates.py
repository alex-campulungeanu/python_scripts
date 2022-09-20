import os
import collections

file_path = os.path.join(os.path.dirname(__file__), 'data.txt')

with open(file_path) as f:
    data = f.readlines()

data_list = [vpc.strip() for vpc in data]

duplicates = [duplicate for duplicate, count in collections.Counter(data_list).items() if count > 1]

print(len(duplicates))

# 1420 vs 107