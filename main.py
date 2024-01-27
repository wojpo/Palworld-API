

from fastapi import FastAPI
from bs4 import BeautifulSoup
import requests
import json


app = FastAPI()


@app.get("/paldeckUpdate")
async def root():
    url = f'https://www.gameleap.com/articles/every-pal-in-palworld-a-complete-paldeck-list'
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    u = 1
    pallist = []
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        paldeck = soup.find_all('strong')
        while u < 650:
            for paldecklist in paldeck[u]:
                print(paldecklist.text)
                pallist.append(paldecklist.text)
            u += 6
        print(pallist)
        file_path = 'PalList.json'
        with open(file_path, 'w') as json_file:
            json.dump(pallist, json_file)

@app.get("/PalList")
async def root():
    file_path = 'PalList.json'
    with open(file_path, 'r') as json_file:
        PalList = json.load(json_file)
    return {
        'PalList': f'{PalList}'
    }
@app.get("/Pal='{Pal}'")
async def root(Pal: str):
    global PalNumber, PalElement, PalDrops, paldrop1, paldrop2, PalAppereance, Palwyglond, DeckEntry, Palzahowanie, PartnerSkill, PartnerSkillDesc, kindling, planting, handiwork, lumbering, medicine, transporting, watering, electricity, gathering, mining, cooling, farming
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
        PalFood = soup.find_all('img', class_='wsgray lazyload')
        ppal = soup.find_all('p')
        PalEntryDeck = soup.find_all('div', class_='decktext')
        PalSkillDesc = soup.find_all('div',
                                     class_='pi-smart-data-value pi-data-value pi-font pi-item-spacing pi-border-color')
        print(PalSkillDesc)

        palelement1 = ''
        palelement2 = ''
        palelements = []
        paldrop1 = ''
        paldrop2 = ''
        paldrop3 = ''
        paldrop4 = ''
        paldrops = []
        foodneed = 10

        for PartnerSkill in PalStats[4]:
            print(PartnerSkill.text)
        for PartnerSkillDesc in PalSkillDesc[1]:
            print(PartnerSkillDesc.text)
        for kindling in PalSkillDesc[2]:
            kindling = kindling.text
            kindling = str(kindling)
            kindling = kindling.replace('Kindling', '')
            kindling = kindling.replace(' ', '')
            if kindling == '':
                kindling = '0'
        for watering in PalSkillDesc[3]:
            watering = watering.text
            watering = str(watering)
            watering = watering.replace('Watering', '')
            watering = watering.replace(' ', '')
            if watering == '':
                watering = '0'
        for planting in PalSkillDesc[4]:
            planting = planting.text
            planting = str(planting)
            planting = planting.replace('Planting', '')
            planting = planting.replace(' ', '')
            if planting == '':
                planting = '0'
        for electricity in PalSkillDesc[5]:
            electricity = electricity.text
            electricity = str(electricity)
            electricity = electricity.replace('Generating Electricity', '')
            electricity = electricity.replace(' ', '')
            if electricity == '':
                electricity = '0'
        for handiwork in PalSkillDesc[6]:
            handiwork = handiwork.text
            handiwork = str(handiwork)
            handiwork = handiwork.replace('Handiwork', '')
            handiwork = handiwork.replace(' ', '')
            if handiwork == '':
                handiwork = '0'
        for gathering in PalSkillDesc[7]:
            gathering = gathering.text
            gathering = str(gathering)
            gathering = gathering.replace('Gathering', '')
            gathering = gathering.replace(' ', '')
            if gathering == '':
                gathering = '0'
        for lumbering in PalSkillDesc[8]:
            lumbering = lumbering.text
            lumbering = str(lumbering)
            lumbering = lumbering.replace('Lumbering', '')
            lumbering = lumbering.replace(' ', '')
            if lumbering == '':
                lumbering = '0'
        for mining in PalSkillDesc[9]:
            mining = mining.text
            mining = str(mining)
            mining = mining.replace('Mining', '')
            mining = mining.replace(' ', '')
            if mining == '':
                mining = '0'
        for medicine in PalSkillDesc[10]:
            medicine = medicine.text
            medicine = str(medicine)
            medicine = medicine.replace('Medicine Production', '')
            medicine = medicine.replace(' ', '')
            if medicine == '':
                medicine = '0'
        for cooling in PalSkillDesc[11]:
            cooling = cooling.text
            cooling = str(cooling)
            cooling = cooling.replace('Cooling', '')
            cooling = cooling.replace(' ', '')
            if cooling == '':
                cooling = '0'
        for transporting in PalSkillDesc[12]:
            transporting = transporting.text
            transporting = str(transporting)
            transporting = transporting.replace('Transporting', '')
            transporting = transporting.replace(' ', '')
            if transporting == '':
                transporting = '0'
        for farming in PalSkillDesc[13]:
            farming = farming.text
            farming = str(farming)
            farming = farming.replace('Farming', '')
            farming = farming.replace(' ', '')
            if farming == '':
                farming = '0'

        for DeckEntry in PalEntryDeck:
            print(DeckEntry.text)
        for PalAppereance in ppal[5]:
            Palwyglond = PalAppereance.text
            Palwyglond = str(Palwyglond)
            Palwyglond = Palwyglond.replace('\n', '')

        for PalNumber in PalStats[0]:
            print(PalNumber.text)

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
                palelement2 = palelement2.replace(' ', '')
        except:
            palelement2 = None

        for PalDrops in PalStats[2]:
            paldrops.append(PalDrops.text)

        try:
            if len(paldrops[0]) > 1:
                paldrop1 = str(paldrops[0])
                paldrop1 = paldrop1.replace(' ', '')
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
                paldrop3 = paldrop3.replace(' ', '')
        except:
            paldrop3 = None

        try:
            if len(paldrops[6]) > 1:
                paldrop4 = str(paldrops[6])
                paldrop4 = paldrop4.replace(' ', '')
        except:
            paldrop4 = None

        for Palfood in PalFood:
            foodneed -= 1

        return {
            "Paldeck": {
                "PalName": f'{Pal}',
                "PaldeckNumber": f"{PalNumber.text}",
                "PaldeckEntry": f'{DeckEntry.text}',
                "PalAppearance": f'{Palwyglond}'},
            "Elements": {
                "Element1": f'{palelement1}',
                "Element2": f'{palelement2}'},
            "Drops": {
                "Drop1": f'{paldrop1}',
                "Drop2": f'{paldrop2}',
                "Drop3": f'{paldrop3}',
                "Drop4": f'{paldrop4}'
            },
            "FoodNeed": f'{foodneed}',
            "PartnerSkill": {
                "PartnerSkillName": f'{PartnerSkill.text}',
                "PartnerSkillDescription": f'{PartnerSkillDesc.text}'},
            "WorkSuitability": {
                'Kindling': f'{kindling}',
                'Planting': f'{planting}',
                'Handiwork': f'{handiwork}',
                'Lumbering': f'{lumbering}',
                'Medicine Production': f'{medicine}',
                "Transporting": f'{transporting}',
                "Watering": f'{watering}',
                "Generating Electricity": f'{electricity}',
                'Gathering': f'{gathering}',
                'Mining': f'{mining}',
                'Cooling': f'{cooling}',
                'Farming': f'{farming}'

            }

        }








