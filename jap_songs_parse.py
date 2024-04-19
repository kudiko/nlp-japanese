from bs4 import BeautifulSoup
import time
import requests
import re



for i in range(1, 353300):
    time.sleep(1)
    content = requests.get('https://www.uta-net.com/song/' + str(i)).text
    
    out_file = open(str(i) + ".txt", "w")
    soup = BeautifulSoup(content, 'html.parser')
    name_unformatted = soup.title.string
    name_formatted = name_unformatted.replace('歌詞 - 歌ネット','') 
    if(name_formatted == 'uta-net.com'):
        continue;
    text_unformatted = soup.find('div', id='kashi_area').get_text()
    text_formatted = text_unformatted.replace('\u3000', '')
    
    date_text = soup.find('p', class_ ="ms-2 ms-md-3 detail mb-0").get_text()
    p = re.compile(r'([0-9]+)\/[0-9]+\/[0-9]+')
    m = re.search(p, date_text)
    if not m:
        continue
    
    out_file.write(name_formatted)
    out_file.write(m.group(1))
    out_file.write(text_formatted)
    out_file.close()
    print('ID' + str(i) + ' completed.')

