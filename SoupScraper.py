






import requests
import re
import csv
from bs4 import BeautifulSoup
#import scrapy
from csv import writer
page = requests.get('http://poea.gov.ph/cgi-bin/agList.asp?mode=allLB')
#page = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')
#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
#title=[]
#for t in soup.findAll('b'):
#	print (t)

#html = page.content[4501:6000].decode('utf-8')
#html = page.content[4501:].decode('utf-8')
html = page.content[4501:].decode('ISO-8859-1')

#head = [next(page.content) for x in range(10)]
#print(page.content[4501:6000])
#print(html)

#html = page.content.decode('utf-8')
#emailIDs = re.findall(r'Email Address</EM> : &nbsp.*?<br>',  html)
#emailIDs = [re.search(r'&nbsp.*?<br>', x).group[1] for x in tempList]
tempList = re.findall(r'Email Address</EM> : &nbsp.*?<br>',  html)
emailIDs = [x.partition("&nbsp")[2].partition("<br>")[0] for x in tempList]

tempList = re.findall(r'Website</EM> : &nbsp.*?<br>',  html)
webSites = [x.partition("&nbsp")[2].partition("<br>")[0] for x in tempList]

tempList = re.findall(r'Official Representative</EM> : .*?<br>',  html)
OffRep = [x.partition(" : ")[2].partition("<br>")[0] for x in tempList]

#emailIDs = emailIDs.index('&nbsp')[5:-4]
#print(emailIDs)
#print(webSites)

with open('index2.csv', 'a') as csv_file:
 writer = csv.writer(csv_file, lineterminator='\n')
 for i in range(0, len(emailIDs)):
    writer.writerow([emailIDs[i], webSites[i], OffRep[i]])
