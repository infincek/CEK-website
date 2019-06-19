import requests
import bs4
# from bs4 import BeautifulSoup

res = requests.get('http://ce-kgr.org/ojustl/', )
res.raise_for_status()
type(res)
noStarchSoup = bs4.BeautifulSoup(res.text, 'lxml')
type(noStarchSoup)
elems = noStarchSoup.select('td')
# print(elems)
det = []
for x in range(28):
    temp = elems[x].getText()
    det.append(temp)
print(det[:])

# det.pop(0)
# det.pop(1)
# det.pop(3)
# det.pop(4)
# det.pop(6)
# det.pop(7)
# det.pop(9)
# det.pop(10)
# det.pop(11)
# det.pop(13)
# det.pop(14)
# det.pop(16)
# det.pop(18)
# det.pop(19)
# det.pop(21)
# det.pop(22)
# det.pop(24)
# det.pop(25)
print(det[:])
res1 = requests.get('http://localhost/CEK-Website/ojustest.php')
res1.raise_for_status()
type(res1)
soup = bs4.BeautifulSoup(res1.text, 'lxml')
type(soup)
soup.title.string = det[2]
soup.title.string.insert_after(" | CEK")
soup.body.div.h2.span.string = det[2]

f = open("ojusfinal.php", "x")
f.write(soup)
# print(tag)
# soup.body.div.select('div [class="title center"]').string = "Ojumon"
# tag = soup.body.div.select('div [class="title center"]')
# print(tag)
