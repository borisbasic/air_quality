from instagrapi import Client
import docs, os
from dotenv import load_dotenv
import pandas as pd
import datetime

load_dotenv()
BASE_URL = os.environ.get('BASE_URL_AIR_QUALITY')
df = pd.read_csv(BASE_URL+'zagadjenje_vazduha.csv')
df_ = df.iloc[-1][:-1]
lowest = df_.idxmin()
highest = df_.idxmax()

lista_drzava = ['_bih','_crna_gora','_hrvatska','_makedonija','_slovenija','_srbija']
path_ = BASE_URL+'pics/zagadjenje_vazduha'

datum = str(datetime.date.today().strftime("%d.%m.%Y"))
all_paths = [path_+datum+'.jpg']
for ld in lista_drzava:
    all_paths.append(path_+ld+datum+'.jpg')
cap = f"Najzagadjeniji grad je {highest} dok grad koji je danas najmanje zagadjen je {lowest} #banjaluka #beograd #zagreb #sarajevo #podgorica #ljubljana #{lowest} #{highest}"
cl = Client()

cl.login(docs.username, docs.password)
media = cl.album_upload(paths=all_paths, caption=cap)
cl.logout()