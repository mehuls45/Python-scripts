#! python3
# lucky.py - Opens several Google search results.

import requests,bs4,sys,webbrowser

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# retrieve top search result links.

soup = bs4.BeautifulSoup(res.text,'lxml')

# open a browser tab for each result

linkElems = soup.select('.r a')
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    print('http://google.com' +linkElems[i].get('href'))




