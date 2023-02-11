import bs4
from bs4 import BeautifulSoup
import re, requests
import pandas as pd
from pathlib import Path


def loading(load_from, img_num):                                                 ## выгрузка фотографий
        try:
            load = requests.get(load_from.text, timeout=15)                      ## в будущем можно добавить multithreading
            out = open(".\img{}.jpg".format(img_num), 'wb')
            out.write(load.content)
            out.close()
        except IOError:
            pass

folder = "758476599"
link = []

messages = 0
epoch = 1


def file_counter():
        folder_name = Path(folder)
        if folder_name.is_dir():
            return len([1 for file in folder_name.iterdir()])


files = file_counter()

while messages < files*50: 
    source = "./{}/messages{}.html".format(folder, messages)
    file = open(source, "r")
    page_response = bs4.BeautifulSoup(file.read(), "html.parser")
    trs0 = page_response.find_all("a", class_="attachment__link")
    n = 1
    print("Текущая итерация: ", epoch, " | ", "пройдено сообщений: ", messages)
    for n, i in enumerate(trs0, start=n):
        trs = page_response.find("a", class_="attachment__link")
        if "https://vk" in str(trs):                             ## в ссылку vk попадают документы и видео
            pass
        else:
            loading(trs, epoch)
            link.append(trs.text)
    file.close()
    messages += 50
    epoch += 1

df = pd.DataFrame(set(link))                                     ## distinct значения
df.to_csv('links.csv', index=False)

