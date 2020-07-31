import os # To navigate back & forth whilst collecting words across the years
import re # re.sub() to get rid of punctuations and non-Tamil characters; re.split() for Efficient Splitting
import csv # For creating output file in CSV format
from tqdm import tqdm #For monitoring PROGRAM PROGRESS
from tamil.utf8 import get_letters

def TamilLength(TamilWord):
    return len(get_letters(TamilWord))

WordPlanet = []

Root = 'Venmurasu Blogs Fully Scraped'
YearWise = os.listdir(Root)
os.chdir(Root)

print("Started Word by Word Extraction")
for Year in tqdm(YearWise):
    Articles = os.listdir(Year)
    os.chdir(Year)
    for A in Articles:
        with open(A, 'r', encoding='utf-8') as EachBlog:
            for Para in EachBlog.readlines():
                #The below RegExp pattern also contains numbers & letters because there are also some English content
                #For example, refer the Blog Entry on 21st February 2014 - It contains info such as Email addresses
                #Also, some characters like quotes, spaces,  seem to have more than one expected forms
                #Such forms have been identified upon trial & error and their occurences have been FIXED
                Words = [(re.sub(r'[@—\[\]\(\)\\*\.,!?""“”\'‘’:;–\-_+=a-zA-Z0-9]', '', EachWord.strip())) for EachWord in re.split(' | |…', Para)]
                WordPlanet.extend([EachWord for EachWord in Words if EachWord!=''])
            EachBlog.close()
    os.chdir('..') #Going back to the Root directory to go through the next Year

WordPlanet = list(set(WordPlanet))
WordPlanet.sort(key=TamilLength,reverse=True)

os.chdir('..')

#Output Choice (1) - Text file - Length <Tab> Word
with open('Venmurasu Final Text Solution.txt', 'w', encoding='utf-8') as output1:
    print("Creating TEXT Output File")
    for TamilWord in tqdm(WordPlanet):
        output1.write(str(TamilLength(TamilWord))+'\t'+TamilWord+'\n')
    output1.close()

#Output Choice (2) - CSV file - Column 1 : Length, Column 2 : Word
with open('Venmurasu Final CSV Solution.csv', 'w', encoding='utf-8') as output2:
    outputCSV = csv.writer(output2)
    outputCSV.writerow(['Length','Word'])
    print("Creating CSV Output File")
    for TamilWord in tqdm(WordPlanet):
        outputCSV.writerow([TamilLength(TamilWord), TamilWord])
    output2.close()

print("Successfully Extracted Words (with Lengths) Into Text & CSV\nNumber of Unique Words = "+str(len(WordPlanet)))
