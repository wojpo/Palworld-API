from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests

app = FastAPI()


@app.get("/Pal='{Pal}'")
async def root(Pal: str):
    global PalNumber, PalElement, PalDrops, paldrop1, paldrop2
    url = f'https://palworld.fandom.com/wiki/{Pal}'
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        PalStats = soup.find_all('div', class_='pi-data-value pi-font')
        PalFood = soup.find_all('img',class_='wsgray lazyload')
        PalDescriptions = soup.find_all('p')
        print(PalDescriptions)

        palelement1 = ''
        palelement2 = ''
        palelements = []
        paldrop1 = ''
        paldrop2 = ''
        paldrop3 = ''
        paldrops = []
        foodneed= 10

        for PalNumber in PalStats[0]:
            PalNumber.text = PalNumber.text

        for PalElement in PalStats[1]:
            palelements.append(PalElement.text)


        try:
            if len(palelements[0]) > 1:
                palelement1 = str(palelements[0])
                palelement1 = palelement1.replace(' ', '')
        except:
            palelement1 = None

        try:
            if len(palelements[2]) > 1:
                palelement2 = str(palelements[2])
                palelement2 = palelement2.replace(' ','')
        except:
            palelement2 = None

        for PalDrops in PalStats[2]:
            paldrops.append(PalDrops.text)


        try:
            if len(paldrops[0]) > 1:
                paldrop1 = str(paldrops[0])
                paldrop1 = paldrop1.replace(' ','')
        except:
            paldrop1 = None


        try:
            if len(paldrops[2]) > 1:
                paldrop2 = str(paldrops[2])
                paldrop2 = paldrop2.replace(' ', '')
        except:
            paldrop2 = None


        try:
            if len(paldrops[4]) > 1:
                paldrop3 = str(paldrops[4])
                paldrop3 = paldrop3.replace(' ','')
        except:
            paldrop3 = None

        for Palfood in PalFood:
            foodneed -= 1




        return {
                "Name": f'{Pal}',
                "Paldeck Number": f"{PalNumber.text}",
                "Paldeck Entry": f'',
                "Element 1": f'{palelement1}',
                "Element 2": f'{palelement2}',
                "Drop 1": f'{paldrop1}',
                "Drop 2": f'{paldrop2}',
                "Drop 3": f'{paldrop3}',
                "Food Need": f'{foodneed}',
                "Partner Skill": f'',
                "Work Suitability": f'',

            }

