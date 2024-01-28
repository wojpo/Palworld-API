import random
from datetime import date

# Hardcoded xd
PAL_LIST = ["Lamball", "Cattiva", "Chikipi", "Lifmunk", "Foxparks", "Fuack", "Sparkit", "Tanzee", "Rooby", "Pengullet",
            "Penking", "Jolthog", "Jolthog Cryst", "Gumoss", "Vixy", "Hoocrates", "Teafant", "Depresso", "Cremis",
            "Daedream", "Rushoar", "Nox", "Fuddler", "Killamari", "Mau", "Mau Cryst", "Celaray", "Direhowl", "Tocotoco",
            "Flopie", "Mozzarina", "Bristla", "Gobfin", "Hangyu", "Mossanda", "Woolipop", "Caprity", "Melpaca",
            "Eikthyrdeer", "Nitewing", "Ribunny", "Incineram", "Cinnamoth", "Arsox", "Dumud", "Cawgnito", "Leezpunk",
            "Loupmoon", "Galeclaw", "Robinquill", "Gorirat", "Beegarde", "Elizabee", "Grintale", "Swee", "Sweepa",
            "Chillet", "Univolt", "Pyrin", "Reindrix", "Rayhound", "Dazzi", "Lunaris", "Dinossom", "Surfent", "Maraith",
            "Digtoise", "Tombat", "Lovander", "Flambelle", "Vanwyrm", "Bushi", "Beakon", "Ragnahawk", "Katress",
            "Wixen", "Verdash", "Vaelet", "Sibelyx", "Elphidran", "Kelpsea", "Azurobe", "Cryolinx", "Blazehowl",
            "Relaxaurus", "Broncherry", "Petallia", "Reptyro", "Kingpaca", "Mammorest", "Wumpo", "Warsect", "Fenglope",
            "Felbat", "Quivern", "Blazamut", "Helzephyr", "Astegon", "Menasting", "Anubis", "Jormuntide", "Suzaku",
            "Grizzbolt", "Lyleen", "Faleris", "Orserk", "Shadowbeak", "Frostallion", "Jetragon"]


async def RandomPal():
    random.seed(date.today().ctime())
    return random.choice(PAL_LIST)
