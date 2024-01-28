import random
from datetime import date


def RandomPal(PalList: [str]):
    random.seed(date.today().ctime())
    return random.choice(PalList)
