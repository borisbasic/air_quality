from dotenv import load_dotenv
import os, time
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import pandas as pd
from dotenv import load_dotenv
import datetime
load_dotenv()
BASE_URL = os.environ.get('BASE_URL_AIR_QUALITY')
TOKEN = os.environ.get('TOKEN_AIR_QUALITY')
import requests

list_of_files = os.listdir(BASE_URL+'pics')
for lof in list_of_files:
    if (datetime.datetime.fromtimestamp(os.path.getctime(BASE_URL+'pics/'+lof)).date()<datetime.datetime.today().date()):
        os.remove(BASE_URL+'pics/'+lof)


lista_gradova = ['Bijeljina', 'Tuzla','Doboj','Mostar','Bihac']
lista_rezultata = []
try:
    data_bijeljina = requests.get('https://api.waqi.info/feed/A461950/?token='+TOKEN)
    lista_rezultata.append(data_bijeljina.json()['data']['iaqi']['pm25']['v'])
except: 
    lista_rezultata.append(0)
try:
    data_tuzla = requests.get('https://api.waqi.info/feed/@9319/?token='+TOKEN)
    lista_rezultata.append(data_tuzla.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_doboj = requests.get('https://api.waqi.info/feed/A87475/?token='+TOKEN)
    lista_rezultata.append(data_doboj.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_mostar = requests.get('https://api.waqi.info/feed/@14726/?token='+TOKEN)
    lista_rezultata.append(data_mostar.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_bihac = requests.get('https://api.waqi.info/feed/@13578/?token='+TOKEN)
    lista_rezultata.append(data_bihac.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)

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
zagadjenje_vazduhacsv = pd.read_csv(BASE_URL+'zagadjenje_vazduha_bih.csv')
zagadjenje_vazduhacsv = pd.concat([zagadjenje_vazduhacsv, dejta_frejm])
zagadjenje_vazduhacsv.to_csv(BASE_URL+'zagadjenje_vazduha_bih.csv', index=None)
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
plt.xlabel('Gradovi Bosne i Hercegovine', fontsize=15)
plt.ylabel('Zagađenost vazduha', fontsize=15)
ax.set_facecolor('#e5e6e3')
ax.text(-0.9, 470, 'zagađenje_vazduha_region_bih_'+str(datetime.date.today().strftime("%d.%m.%Y")), color='gray', alpha=0.5, fontsize=20)
plt.savefig(BASE_URL+'/pics/'+'zagadjenje_vazduha_bih'+str(datetime.date.today().strftime("%d.%m.%Y"))+'.jpg')



lista_gradova = ['Budva','Bar','Nikšić','Bijelo Polje', 'Pljevlja']
lista_rezultata = []
try:
    data_budva = requests.get('https://api.waqi.info/feed/A473170/?token='+TOKEN)
    lista_rezultata.append(data_budva.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_bar = requests.get('https://api.waqi.info/feed/@12634/?token='+TOKEN)
    lista_rezultata.append(data_bar.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_niksic = requests.get('https://api.waqi.info/feed/@12632/?token='+TOKEN)
    lista_rezultata.append(data_niksic.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_bijelo_polje = requests.get('https://api.waqi.info/feed/@12633/?token='+TOKEN)
    lista_rezultata.append(data_bijelo_polje.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:    
    data_pljevlja = requests.get('https://api.waqi.info/feed/@12631/?token='+TOKEN)
    lista_rezultata.append(data_pljevlja.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)

l = []
for i in range(len(lista_gradova)):
    str_ = int(lista_rezultata[i])
    l.append(str_)
    rjecnik[lista_gradova[i]] = l
    l = []
date = pd.to_datetime(pd.Timestamp.now().date())
dejta_frejm = pd.DataFrame.from_dict(rjecnik)
dejta_frejm['date'] = date
zagadjenje_vazduhacsv = pd.read_csv(BASE_URL+'zagadjenje_vazduha_crna_gora.csv')
zagadjenje_vazduhacsv = pd.concat([zagadjenje_vazduhacsv, dejta_frejm])
zagadjenje_vazduhacsv.to_csv(BASE_URL+'zagadjenje_vazduha_crna_gora.csv', index=None)
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
plt.xlabel('Gradovi Crne Gore', fontsize=15)
plt.ylabel('Zagađenost vazduha', fontsize=15)
ax.set_facecolor('#e5e6e3')
ax.text(-0.9, 470, 'zagađenje_vazduha_region_crna_gora_'+str(datetime.date.today().strftime("%d.%m.%Y")), color='gray', alpha=0.5, fontsize=20)
plt.savefig(BASE_URL+'/pics/'+'zagadjenje_vazduha_crna_gora'+str(datetime.date.today().strftime("%d.%m.%Y"))+'.jpg')


lista_gradova = ['Dubrovnik', 'Pula','Osijek','Rijeka','Karlovac']
lista_rezultata=[]
try:
    data_dubrovnik = requests.get('https://api.waqi.info/feed/A415807/?token='+TOKEN)
    lista_rezultata.append(data_dubrovnik.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_pula = requests.get('https://api.waqi.info/feed/@12481/?token='+TOKEN)
    lista_rezultata.append(data_pula.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_osijek = requests.get('https://api.waqi.info/feed/@14685/?token='+TOKEN)
    lista_rezultata.append(data_osijek.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_rijeka = requests.get('https://api.waqi.info/feed/@5145/?token='+TOKEN)
    lista_rezultata.append(data_rijeka.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_karlovac= requests.get('https://api.waqi.info/feed/A178390/?token='+TOKEN)
    lista_rezultata.append(data_karlovac.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)

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




lista_gradova = ['Tetovo','Kumanovo','Bitola','Gevgelija','Strumica']
lista_rezultata = []
try:
    data_tetovo = requests.get('https://api.waqi.info/feed/@8102/?token='+TOKEN)
    lista_rezultata.append(data_tetovo.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_kumanovo = requests.get('https://api.waqi.info/feed/A464536/?token='+TOKEN)
    lista_rezultata.append(data_kumanovo.json()['data']['iaqi']['pm25']['v'])
except: 
    lista_rezultata.append(0)
try:
    data_bitola = requests.get('https://api.waqi.info/feed/@8098/?token='+TOKEN)
    lista_rezultata.append(data_bitola.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_gevgelija = requests.get('https://api.waqi.info/feed/@13575/?token='+TOKEN)
    lista_rezultata.append(data_gevgelija.json()['data']['iaqi']['o3']['v'])
except:
    lista_rezultata.append(0)
try:
    data_strumica= requests.get('https://api.waqi.info/feed/@10094/?token='+TOKEN)
    lista_rezultata.append(data_strumica.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)

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
zagadjenje_vazduhacsv = pd.read_csv(BASE_URL+'zagadjenje_vazduha_makedonija.csv')
zagadjenje_vazduhacsv = pd.concat([zagadjenje_vazduhacsv, dejta_frejm])
zagadjenje_vazduhacsv.to_csv(BASE_URL+'zagadjenje_vazduha_makedonija.csv', index=None)
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
plt.xlabel('Gradovi Sjeverne Makedonije', fontsize=15)
plt.ylabel('Zagađenost vazduha', fontsize=15)
ax.set_facecolor('#e5e6e3')
ax.text(-0.9, 470, 'zagađenje_vazduha_region_makedonija_'+str(datetime.date.today().strftime("%d.%m.%Y")), color='gray', alpha=0.5, fontsize=20)
plt.savefig(BASE_URL+'/pics/'+'zagadjenje_vazduha_makedonija'+str(datetime.date.today().strftime("%d.%m.%Y"))+'.jpg')



lista_gradova = ['Koper','Novo Mesto','Celje','Maribor','Nova Gorica']
lista_rezultata = []
try:
    data_koper = requests.get('https://api.waqi.info/feed/@5140/?token='+TOKEN)
    lista_rezultata.append(data_koper.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_novo_mesto = requests.get('https://api.waqi.info/feed/@13341/?token='+TOKEN)
    lista_rezultata.append(data_novo_mesto.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_celje = requests.get('https://api.waqi.info/feed/@14554/?token='+TOKEN)
    lista_rezultata.append(data_celje.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_maribor = requests.get('https://api.waqi.info/feed/@13347/?token='+TOKEN)
    lista_rezultata.append(data_maribor.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_nova_gorica= requests.get('https://api.waqi.info/feed/@13342/?token='+TOKEN)
    lista_rezultata.append(data_nova_gorica.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)


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
zagadjenje_vazduhacsv = pd.read_csv(BASE_URL+'zagadjenje_vazduha_slovenija.csv')
zagadjenje_vazduhacsv = pd.concat([zagadjenje_vazduhacsv, dejta_frejm])
zagadjenje_vazduhacsv.to_csv(BASE_URL+'zagadjenje_vazduha_slovenija.csv', index=None)
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
plt.xlabel('Gradovi Slovenije', fontsize=15)
plt.ylabel('Zagađenost vazduha', fontsize=15)
ax.set_facecolor('#e5e6e3')
ax.text(-0.9, 470, 'zagađenje_vazduha_region_slovenija_'+str(datetime.date.today().strftime("%d.%m.%Y")), color='gray', alpha=0.5, fontsize=20)
plt.savefig(BASE_URL+'/pics/'+'zagadjenje_vazduha_slovenija'+str(datetime.date.today().strftime("%d.%m.%Y"))+'.jpg')


lista_gradova = ['Niš','Subotica','Čačak','Kragujevac','Zaječar']
lista_rezultata = []
try:
    data_nis = requests.get('https://api.waqi.info/feed/@12644/?token='+TOKEN)
    lista_rezultata.append(data_nis.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_subotica = requests.get('https://api.waqi.info/feed/A367828/?token='+TOKEN)
    lista_rezultata.append(data_subotica.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_cacak = requests.get('https://api.waqi.info/feed/A189766/?token='+TOKEN)
    lista_rezultata.append(data_cacak.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_kragujevac = requests.get('https://api.waqi.info/feed/A216391/?token='+TOKEN)
    lista_rezultata.append(data_kragujevac.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_zajecar= requests.get('https://api.waqi.info/feed/A473710/?token='+TOKEN)
    lista_rezultata.append(data_zajecar.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)


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
zagadjenje_vazduhacsv = pd.read_csv(BASE_URL+'zagadjenje_vazduha_srbija.csv')
zagadjenje_vazduhacsv = pd.concat([zagadjenje_vazduhacsv, dejta_frejm])
zagadjenje_vazduhacsv.to_csv(BASE_URL+'zagadjenje_vazduha_srbija.csv', index=None)
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
plt.xlabel('Gradovi Srbije', fontsize=15)
plt.ylabel('Zagađenost vazduha', fontsize=15)
ax.set_facecolor('#e5e6e3')
ax.text(-0.9, 470, 'zagađenje_vazduha_region_srbija_'+str(datetime.date.today().strftime("%d.%m.%Y")), color='gray', alpha=0.5, fontsize=20)
plt.savefig(BASE_URL+'/pics/'+'zagadjenje_vazduha_srbija'+str(datetime.date.today().strftime("%d.%m.%Y"))+'.jpg')



lista_gradova = ['Beograd', 'Banja Luka', 'Sarajevo', 'Novi Sad', 'Zagreb', 'Ljubljana', 'Podgorica', 'Split',
                 'Skopje', 'Zenica']
lista_rezultata = []
try:
    data_beograd = requests.get('https://api.waqi.info/feed/A127555/?token='+TOKEN)
    lista_rezultata.append(data_beograd.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_banja_luka = requests.get('https://api.waqi.info/feed/A236194/?token='+TOKEN)
    lista_rezultata.append(data_banja_luka.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_sarajevo = requests.get('https://api.waqi.info/feed/@9264/?token='+TOKEN)
    lista_rezultata.append(data_sarajevo.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_novi_sad = requests.get('https://api.waqi.info/feed/A115834/?token='+TOKEN)
    lista_rezultata.append(data_novi_sad.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_zagreb = requests.get('https://api.waqi.info/feed/@5150/?token='+TOKEN)
    lista_rezultata.append(data_zagreb.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_zenica = requests.get('https://api.waqi.info/feed/@13579/?token='+TOKEN)
    lista_rezultata.append(data_zenica.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_ljubljana = requests.get('https://api.waqi.info/feed/@14556/?token='+TOKEN)
    lista_rezultata.append(data_ljubljana.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_podgorica = requests.get('https://api.waqi.info/feed/@12630/?token='+TOKEN)
    lista_rezultata.append(data_podgorica.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)
try:
    data_split = requests.get('https://api.waqi.info/feed/@5749/?token='+TOKEN)
    lista_rezultata.append(data_split.json()['data']['iaqi']['no2']['v'])
except:
    lista_rezultata.append(0)
try:
    data_skopje = requests.get('https://api.waqi.info/feed/A412345/?token='+TOKEN)
    lista_rezultata.append(data_skopje.json()['data']['iaqi']['pm25']['v'])
except:
    lista_rezultata.append(0)


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
zagadjenje_vazduhacsv = pd.read_csv(BASE_URL+'zagadjenje_vazduha.csv')
zagadjenje_vazduhacsv = pd.concat([zagadjenje_vazduhacsv, dejta_frejm])
zagadjenje_vazduhacsv.to_csv(BASE_URL+'zagadjenje_vazduha.csv', index=None)
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
ax.axis([-1,10,0,500])
ax.axhline(50,color='#009966',label='Dobar', alpha=0.9)
ax.axhline(100,color='#FFD700',label='Prihvatljiv', alpha=0.9)
ax.axhline(150,color='orange',label='Nezdrav za osjetljive osobe', alpha=0.9)
ax.axhline(200,color='red',label='Nezdrav', alpha=0.9)
ax.axhline(300,color='#660099',label='Vrlo nezdrav', alpha=0.9)
ax.axhline(500,color='#7e0023',label='Štetan po zdravlje', alpha=0.9)
ax.legend()
plt.title('Zagađenje vazduha u regionu', fontsize=15)
plt.yticks([0,50,100,150,200,250,300,350,400,450,500])
plt.xlabel('Gradovi regiona', fontsize=15)
plt.ylabel('Zagađenost vazduha', fontsize=15)
ax.set_facecolor('#e5e6e3')
ax.text(-0.9, 470, 'zagađenje_vazduha_region_'+str(datetime.date.today().strftime("%d.%m.%Y")), color='gray', alpha=0.5, fontsize=20)
plt.savefig(BASE_URL+'/pics/'+'zagadjenje_vazduha'+str(datetime.date.today().strftime("%d.%m.%Y"))+'.jpg')

