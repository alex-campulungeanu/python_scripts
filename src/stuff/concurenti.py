import asyncio
import random

podium_list = []
concurenti = 5 

c = (
    "\033[0m"	,  # End of color
    "\033[31m",  # Red
    "\033[32m",  # Magenta
    "\033[33m",  # Magenta
    "\033[34m",  # Magenta
    "\033[35m",  # Magenta
    "\033[36m",  # Magenta
    "\033[37m",  # Magenta
)


def generate_color():
    rc = random.randint(20, 100)
    return r"\033" + f"[{rc}m"

async def makerandom(idx: int, threshod: int) -> int:
    curr_rand = c[idx + 1]
    print(curr_rand + f"initated makerandom({idx})")
    i = random.randint(0, 10)
    while i <= threshod:
        print(f"{curr_rand} makerandom({idx}) == {i} to low ({threshod}), retrying")
        await asyncio.sleep(1)
        i = random.randint(0, 10)
    print(f"{curr_rand} --> finished: makerandom({idx}) == {i} + {c[0]}")
    global podium_list
    podium_list.append(idx)
    return i

def generate_podium(competitors: int):
    podium = {}
    for i in range(competitors):
        podium.update({
            i: 0
        })
    return podium

async def main():
    res = await asyncio.gather(*(makerandom(i, 10 -i - 1) for i in range(concurenti)))
    print(podium_list)
    return res

if __name__ == "__main__":
    # random.seed(444)
    re = asyncio.run(main())
    print()
    print(re)
    # print(f"r1: {r1}, r2: {r2}, r3: {r3}")
