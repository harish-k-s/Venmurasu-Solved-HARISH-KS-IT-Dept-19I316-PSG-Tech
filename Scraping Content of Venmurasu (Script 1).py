#pip install requests in order to obtain the following 'get' function
#pip install bs4 in order to obtain the following 'BeautifulSoup' function
#pip install tqdm in order to monitor the PROGRAM PROGRESS, as it will take a long time to run

from requests import get
from bs4 import BeautifulSoup

from sys import exit #Relatively better than the usual exit()
from calendar import _monthlen
from tqdm import tqdm
import os
import re

os.mkdir('Venmurasu Blogs Fully Scraped')
os.chdir('Venmurasu Blogs Fully Scraped')
print('Started Scraping')

for year in tqdm(range(2014, 2020+1)):
    print('Status: Currently Scraping Blogs From '+str(year))
    os.mkdir('வருடம் '+str(year))
    os.chdir('வருடம் '+str(year))

    for month in range(1, 12+1):
        for day in range(1, _monthlen(year,month)+1):

            if year == 2020 and month == 7 and day >= 17:
                print('Successfully Scraped All Blogs From 1st January 2014 To 16th July 2020')
                exit(0) #Terminating this script as we cross 16th July 2020
            try:
                shortLink = "https://venmurasu.in/{}/{:0=2d}/{:0=2d}/".format(year, month, day)
                shortBlog = get(shortLink).text
                fullLink = BeautifulSoup(shortBlog, 'html.parser').article.a.get_attribute_list('href')[0]
                #Note - The above step is mandatory because SOME BLOGS are NOT FULLY DISPLAYED in the FIRST LINK
                #There is a (மேலும்…) Link below the FIRST PARAGRAPH to CONTINUE READING
                #So, I discovered this way to use the EXTENDED LINK to ENABLE COMPLETE SCRAPING of the whole blog
                #The above technique will relatively slow down the program, but no other go
            except:
                continue #Just in case any particular date does not contain a Blog article, we can except that situation

            Blog = get(fullLink).text
            Article = str(BeautifulSoup(Blog, 'html.parser').article)
            Paragraphs = re.findall(r'>([^<]*)</p>', Article)
            #Alternate Method : We can also use bs4 object methods like findChildren('p') and then use .text individually
            #But I chose to use Regular Expressions here due to their simplicity, efficiency & dependability

            ScrapedFile = shortLink[-3:-1] + '-' + shortLink[-6:-4] + '-' + shortLink[-11:-7] + '.txt'

            with open(ScrapedFile, 'w', encoding='utf-8') as F:
                for Para in Paragraphs:
                    if Para.strip() != '': F.write('\n'+Para+'\n')
                F.close() #Closing is optional here due to the 'with' keyword
    print('Status: Finished Scraping Blogs From '+str(year))
    os.chdir('..')
