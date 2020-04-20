import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

file_name = input('Where to save: ')
text = ''

for story_heading in soup.find_all(class_="balancedHeadline"): 
    if story_heading.a: 
        text = print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        text = print(story_heading.contents[0].strip())

with open(file_name, 'w') as open_file:
    open_file.write(text)





