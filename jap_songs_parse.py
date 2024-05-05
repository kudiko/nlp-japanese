from bs4 import BeautifulSoup
import time
import requests
import re
import os
cwd = os.getcwd()


from datetime import datetime

logfile = open("log.txt", "a")


for i in range(195000, 200000):
   # time.sleep(1)
    
    content = None
    while True:
        try:
            content = requests.get('https://www.uta-net.com/song/' + str(i)).text
        except:
            print("Error in requests.get in id " + str(i) + ", retrying ...")
            continue
        break
    
    
    out_file = open(cwd + "/parse_results/" + str(i) + ".txt", "w")
    soup = BeautifulSoup(content, 'html.parser')
    name_unformatted = soup.title.string
    name_formatted = ""
    
    if (isinstance(name_unformatted, str)):
    	name_formatted = name_unformatted.replace('歌詞 - 歌ネット','')
    	
    if(name_formatted == 'uta-net.com'):
        continue
    
    div_tag = soup.find('div', id='kashi_area')
    if div_tag is None:
    	continue
    text_unformatted = div_tag.get_text()
    text_formatted = text_unformatted.replace('\u3000', '')
    
    date_text = soup.find('p', class_ ="ms-2 ms-md-3 detail mb-0").get_text()
    p = re.compile(r'([0-9]+)\/[0-9]+\/[0-9]+')
    m = re.search(p, date_text)
    if not m:
        continue
        
    
    out_file.write(name_formatted)
    out_file.write('\n')
    out_file.write(m.group(1))
    out_file.write('\n')
    out_file.write(text_formatted)
    out_file.write('\n')
    out_file.close()
    
    now = datetime.now()
    logfile.write(str(now) + ': ' + 'ID' + str(i) + ' completed. \n')
    
    
    print('ID' + str(i) + ' completed.')

