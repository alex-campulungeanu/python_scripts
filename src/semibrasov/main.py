import pprint

def time_to_minutes(time: str):
    factors = [60, 1, 1/60]
    splitted_time = list(map(int, time.split(":")))
    zipped = zip(splitted_time, factors)
    total_time = sum(i*j for i, j in zipped)
    return total_time

with open("concurenti.txt") as file:
    concurent_list = []
    lines = file.readlines()
    for line in lines:
        # print(line)
        splitted_line = line.rstrip("\n").split("\t")
        if splitted_line[3] == '4':
            rank = splitted_line[0]
            nr = splitted_line[1]
            name = splitted_line[2]
            splits = splitted_line[3]
            time1 = splitted_line[4]
            time2 = splitted_line[5]
            time2_rank = splitted_line[0]
            concurent_list.append({
                "rank": rank,
                "nr": nr,
                "name": name,
                "splits": splits,
                "time1": time1,
                "time1_minutes": time_to_minutes(time1),
                "time2": time2,
                "time2_rank": time2_rank,
            })

# TODO: should be a better way to do this, for now it works
time1_sorted = sorted(concurent_list, key=lambda l: l['time1_minutes'] )
for idx, item in enumerate(time1_sorted):
    item["time1_rank"] = idx

time2_sorted = sorted(time1_sorted, key=lambda d: int(d['time2_rank']))    

for x in time2_sorted:
    x['diff'] = int(x['time1_rank']) - int(x['time2_rank'])
    
for y in time2_sorted:
    print(y)

print("\n")    

concurent = input("for what concurent want to find the details?: ")

if concurent:
    conc = [c for c in time2_sorted if concurent in c['name'].lower()][0]
    pprint.pprint(conc)
