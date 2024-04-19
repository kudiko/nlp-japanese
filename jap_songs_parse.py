#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 00:41:29 2023

@author: kudiko
"""

#from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
#import pandas as pd

#firefox_profile = webdriver.FirefoxProfile()
#firefox_profile.set_preference("browser.download.folderList",2)
#firefox_profile.set_preference("javascript.enabled", False)
#driver = webdriver.Chrome(executable_path='/home/kudiko/Downloads/chromedriver')

texts = []
year = []
musician_and_name = []

out_file = open("japanese_songs.txt", "w")
for i in range(1, 101):
    time.sleep(1)
    #driver.get('https://www.uta-net.com/song/' + str(i))
    content = requests.get('https://www.uta-net.com/song/' + str(i)).text
    #content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')
    name_unformatted = soup.title.string
    name_formatted = name_unformatted.replace('歌詞 - 歌ネット','') 
    if(name_formatted == 'uta-net.com'):
        continue;
    musician_and_name.append(name_formatted)
    text_unformatted = soup.find('div', id='kashi_area').get_text()
    text_formatted = text_unformatted.replace('\u3000', '')
    texts.append(text_formatted)
    print(str(i) + ' : ' + name_formatted + ' : ' + text_formatted)
    print('ID' + str(i) + ' completed.')
    out_file.write(str(i) + ' : ' + name_formatted + ' : ' + text_formatted)
    out_file.write('\n\n\n')
out_file.close()
#df = pd.DataFrame({'Musician and name': musician_and_name, 'Text' : texts})
#df