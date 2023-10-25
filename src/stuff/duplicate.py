result = []

with open('data.txt') as file:
    ips = file.read().splitlines()

stripped_ips = [x.strip() for x in ips]

duplicates = set([y for y in stripped_ips if stripped_ips.count(y) > 1])

for duplicate in duplicates:
    duplicate_tuple = (duplicate, 'nr of duplicates: ' + str(stripped_ips.count(duplicate)))
    result.append(duplicate_tuple)

print(result)
