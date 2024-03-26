import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import datetime, os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
BASE_URL = os.environ.get('BASE_URL_AIR_QUALITY')
lista_gradova = ['Zagreb', 'Zadar','Osijek','Rijeka','Karlovac']
op = webdriver.FirefoxOptions()
op.add_argument('--headless')
link = 'https://waqi.info/'
driver = webdriver.Firefox(options=op)
driver.get(link)
lista_rezultata = []
for l in lista_gradova:
    bank = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'search-in-menu')))
    input_ = WebDriverWait(bank, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'input')))
    input_[0].send_keys(l)
    time.sleep(2)
    result = WebDriverWait(bank, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'result')))
    f_result = WebDriverWait(result[1], 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'span')))
    if f_result[0].text.isnumeric():
        lista_rezultata.append(int(f_result[0].text))
    else:
        lista_rezultata.append(0)
    input_[0].clear()
    time.sleep(3)
driver.close()
# RJECNIK i EXCEL
rjecnik = {}
l = []
for i in range(len(lista_gradova)):
    str_ = int(lista_rezultata[i])
    l.append(str_)
    rjecnik[lista_gradova[i]] = l
    l = []
date = pd.to_datetime(pd.Timestamp.now().date())
dejta_frejm = pd.DataFrame.from_dict(rjecnik)
dejta_frejm['date'] = date
zagadjenje_vazduhacsv = pd.read_csv(BASE_URL+'zagadjenje_vazduha_hrvatska.csv')
zagadjenje_vazduhacsv = pd.concat([zagadjenje_vazduhacsv, dejta_frejm])
zagadjenje_vazduhacsv.to_csv(BASE_URL+'zagadjenje_vazduha_hrvatska.csv', index=None)
# GRAFIKON
fig, ax = plt.subplots(figsize=(15, 10))
for i in range(len(lista_rezultata)):
    if lista_rezultata[i]<50:
        color='#009966'
        ax.text(i - 0.05, 10, lista_rezultata[i], color=color, style='oblique', backgroundcolor='white')
    elif lista_rezultata[i]>=50 and lista_rezultata[i]<100:
        color='#FFD700'
        ax.text(i - 0.05, 10, lista_rezultata[i], color=color,style='oblique', backgroundcolor='white')
    elif lista_rezultata[i]>=100 and lista_rezultata[i]<150:
        color='orange'
        ax.text(i - 0.05, 10, lista_rezultata[i], color=color,style='oblique', backgroundcolor='white')
    elif lista_rezultata[i]>=150 and lista_rezultata[i]<200:
        color='red'
        ax.text(i - 0.05, 10, lista_rezultata[i], color=color,style='oblique', backgroundcolor='white')
    elif lista_rezultata[i]>=200 and lista_rezultata[i]<300:
        color='#660099'
        ax.text(i - 0.05, 10, lista_rezultata[i], color=color,style='oblique', backgroundcolor='white')
    else:
        color='#7e0023'
        ax.text(i - 0.05, 10, lista_rezultata[i], color=color,style='oblique', backgroundcolor='white')
    ax.add_patch(Rectangle((-0.4+i, lista_rezultata[i]), 0.9, -lista_rezultata[i], facecolor=color, alpha=0.8, edgecolor='grey'))

ax.plot(lista_gradova, lista_rezultata,'black', linewidth=1)
ax.axis([-1,5,0,500])
ax.axhline(50,color='#009966',label='Dobar', alpha=0.9)
ax.axhline(100,color='#FFD700',label='Prihvatljiv', alpha=0.9)
ax.axhline(150,color='orange',label='Nezdrav za osjetljive osobe', alpha=0.9)
ax.axhline(200,color='red',label='Nezdrav', alpha=0.9)
ax.axhline(300,color='#660099',label='Vrlo nezdrav', alpha=0.9)
ax.axhline(500,color='#7e0023',label='Štetan po zdravlje', alpha=0.9)
ax.legend()
plt.title('Zagađenje vazduha u regionu', fontsize=15)
plt.yticks([0,50,100,150,200,250,300,350,400,450,500])
plt.xlabel('Gradovi Hrvatske', fontsize=15)
plt.ylabel('Zagađenost vazduha', fontsize=15)
ax.set_facecolor('#e5e6e3')
ax.text(-0.9, 470, 'zagađenje_vazduha_region_hrvatska_'+str(datetime.date.today().strftime("%d.%m.%Y")), color='gray', alpha=0.5, fontsize=20)
plt.savefig(BASE_URL+'/pics/'+'zagadjenje_vazduha_hrvatska'+str(datetime.date.today().strftime("%d.%m.%Y"))+'.jpg')


