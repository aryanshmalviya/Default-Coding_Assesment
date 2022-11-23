import requests
import pandas as pd 
import urllib.parse
from bs4 import BeautifulSoup



url = 'https://clutch.co/developers/react-native?geona_id=356'

sa_key = '914a3d7c86d54573a6816303498267dc' # paste here
sa_api = 'https://api.scrapingant.com/v2/general'
qParams = {'url': url, 'x-api-key': sa_key}
reqUrl = f'{sa_api}?{urllib.parse.urlencode(qParams)}'  

r = requests.get(reqUrl)
# print(r.text) # --> html
soup = BeautifulSoup(r.content, 'html.parser')
file = open('index.html', 'w')
# print(soup.prettify())


name_elements = soup.find_all('a', class_="company_title")

names = []

for element in name_elements:
    names.append(str(element.text).strip())

website_elements = soup.find_all('a', class_="website-link__item")

websites =  []

for element in website_elements:
    x = str(element).split('href=')
    a = str(x[1]).split('rel')
    websites.append(str(a[0]))
        
# location_elements = soup.find_all('span', class_='locality')

# locations = []

# for element in location_elements:
#     locations.append(str(element.string).strip())


module_elements = soup.find_all('div' , class_= "module-list")

Hourly_rate = []
min_project_size = []
employee_size = []
locality = []
for element in module_elements:
    x = element.find_all('span')
    min_project_size.append(str(x[0].text))
    Hourly_rate.append(str(x[1].text))
    employee_size.append(str(x[2].text))
    locality.append(str(x[3].text))


rating_element = soup.find_all('span' , class_= "rating sg-rating__number")
ratings = []  
for element in rating_element:
    x = str(element.text).split('\n')
    ratings.append(str(x[1]).strip())
# print(ratings)


    




df= pd.DataFrame()
df['Company'] = names
df['website'] = websites
df['Hourly rate'] = Hourly_rate
df['Ratings'] = ratings
df['Employee Size'] = employee_size
df['Min project size'] = min_project_size
df['Location'] = locality
df.to_excel('ReactNativeDevelopment.xlsx',index=False)
