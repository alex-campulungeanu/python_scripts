houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house", "Alex house"]

def iterate_recursive(houses):
    l = len(houses)
    if len(houses) == 1:
        print(f'House: {houses[0]}')
        return
    print(f'House: {houses[0]}')
    iterate_recursive(houses[1:])
        
iterate_recursive(houses)