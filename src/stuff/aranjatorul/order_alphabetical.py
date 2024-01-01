file_content = []

sorted_lines = []

with open("directories.txt") as f:
    lines = f.readlines()
    # get max nr of characters
    biggest = len(max(lines, key=len))
    
    sorted_lines = sorted(lines)
    
with open("directories_out.txt", 'a') as f_out:
    for l in sorted_lines:
        f_out.write(l)
    
    # for idx, line in enumerate(lines):
    #     file_content.append({
    #         'path': line,
    #         'rank': idx,
    #         'length': len(line)
    #     })
    # print(file_content)
    # for x in range(biggest):
    #     for ln in file_content:
    #         for ln2 in 
    #        cur_path = ln['path']
    #        if cur_path[x]:
               
            
    
    # a = 'a'
    # b = 'b'
    # if a < b:
    #     print('da')
           
            