import sys
import requests

from bs4 import BeautifulSoup
#url = f'https://kidkodschool.github.io/welcome.html'

#response = requests.get(url)

#with open("./python_is_cool.html", 'wb') as f:
 #   f.write(response.content)

#import requests

#from bs4 import BeautifulSoup
#Используем аргументы если они есть,иначе серез input
query = sys.argv[1] if len(sys.argv) > 1 else input('Type avatar: ')
url = f'https://www.kiddle.co/s.php?q={query}'

page = requests.get(url).text
soup = BeautifulSoup(page, 'html.parser')
#print(soup)
#print(dir(soup))

for raw_img in soup.find_all('img'):
    link = raw_img.get('src')
    if link and link.startswith('https'):
        response = requests.get(link)
        with open("./today_avatar.jpg", 'wb') as f:
            f.write(response.content)
        print('Avatar nashelsa - today_avatar.jpg')
        break
else:
    print('Avatar ne nashelsa - today_avatar.jpg')