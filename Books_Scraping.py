import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import gspread
import json

from oauth2client.service_account import ServiceAccountCredentials

result = requests.get("https://www.marefa.org/قائمة_أفضل_الكتب_العربية", verify=False)
results = result.content
soup = BeautifulSoup(results, "lxml")
order = []
book_tag = []
author = []
country = []
image = []
cov = []


book_tags = soup.find('table', class_ = 'wikitable').find('tbody').find_all('tr')[1:]

for i in range(len(book_tags)):
    kotb = book_tags[i].text
    data =  kotb.split("\n\n")
    order.append(data[0][1:])
    book_tag.append(data[1])
    author.append(data[2])
    country.append(data[3])
 

link = soup.find('table', class_ = 'wikitable').find('tbody').find_all('tr')[1:]

for cover in link:
    try:
        link1 = cover.find('div', class_= 'floatleft').find('img').attrs["alt"]
    except AttributeError:
        link1 = ('Name1')
    try:
        link0 = cover.find('div', class_= 'floatleft').find('img').attrs["src" or "srcset"][15:21]
    except AttributeError:
        link0 = ('Name1')
    link2 = "https://www.marefa.org/w/images"
    if link1 == "Name1":
        link4 = "Cover Image Not Found"
    else:
        link4 = link2 +link0 +  link1
    link5 = link4.replace(" ", "_")
    image.append(link5)
    cov.append(link1)

def make_hyperlink(link, value):
    return f'=HYPERLINK("{link}", "{value}")'


df = pd.DataFrame({"الترتيب" : order,
                  "الاسم" : book_tag,
                   "المؤلف" : author,
                   "البلد" : country,
                   "الرواية" : image,
                   "covers" : cov})

links_list = []

for index, row in df.iterrows():
    links_list.append(make_hyperlink(row['الرواية'],row['covers']))
df['الغلاف'] = pd.Series(links_list)
df.drop(columns=['الرواية', 'covers'], inplace= True, axis= 1)

df.to_excel('books.xlsx', index=False, header=True)
df.to_csv('books.csv', index=False, header=True, encoding= 'utf-8-sig')



scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file']
creds = ServiceAccountCredentials.from_json_keyfile_name('scraping-375112-d97c86538c10.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Scraping').sheet1
spreadsheet_key = "1Uf3ls0oeeTTLyxDiZjDLOtwcP__VY3tUhpy-J2QFz3o"

from df2gspread import df2gspread as d2g
wks_name = 'sheet1'
cell_of_start_df = 'A1'
d2g.upload(df,
           spreadsheet_key,
           wks_name,
           credentials = creds,
           col_names=False,
           row_names=False,
           start_cell = cell_of_start_df,
           clean=False)

# *********************************************************************
url2 = 'https://www.marefa.org/قائمة_أفضل_الكتب_العربية'
response = requests.get(url2,verify=False)
soup = BeautifulSoup(response.content, 'lxml')
Title = soup.find('table', class_='wikitable')
list_data2 = []
list_data3 = []
for tr in Title.find_all('tr')[1:]:
    tds = tr.find_all('td')
    book = tds[1].a.contents[0]
    Title_link = f"https://www.marefa.org{tds[1].a.get('href')}"
    list_data2.append({'صفحة_الرواية': Title_link})
    list_data3.append(Title_link)


df = pd.DataFrame(list_data2)

df.to_excel('titles.xlsx', index=False, header=False)
df.to_csv('titles.csv', index=False, header=False, encoding= 'utf-8-sig')
# print(list_data3)
# exit()

# *******************************************************************************************************

import qrcode # Import QR Code library with pip install qrcode[pil]
import sys #To exit the program if QR data is not given
import os #To create the save folder if not already there
import csv #CSV file support
from PIL import Image, ImageDraw, ImageFont #Display the image
import time #For the waiting

qrName = 'qr'

csvFile = 'titles.csv'
qrLabel = 'N'
qrFolder = 'QRs'
boxPixels = "7"
imageType = "7"

if len(str(csvFile)) == 0:
    print('You did not pick a data file.  Using the demo.csv file as a data source.')
    print('===============================================')
    csvFile = 'titles.csv'
#Make a sub folder for saved QRcodes from this run:
if not os.path.exists(csvFile):
    print('Could not locate any data file named ' + str(csvFile) + '.  Exiting Program...')
    sys.exit()

#Are we doing captions?
doCaption = 0
if qrLabel == 'Y' or qrLabel == "y" or qrLabel == "yes" or qrLabel == "YES":
    doCaption = 1
    fontFile = 'fonts/FreeMono.ttf'
    fontName = 'FreeMono.ttf'
if doCaption:
    if not os.path.exists(fontFile):
        doCaption = 0
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('I could not find a font file to make your caption!\nPlease download ' + fontName + ' and put it in the fonts folder.')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

if len(str(qrFolder)) == 0:
    print('You did not pick a folder name.  Using "QRs" as the folder name.')
    print('===============================================')
    qrFolder = 'QRs/'
else:
    qrFolder = qrFolder + '/'

if len(str(boxPixels)) == 0:
    print('You did not set a pixel size for boxes. I will use 7')
    print('===============================================')
    boxPixels = 7

#Set the image type:
if imageType == "1":
    imageExt = '.jpg'
elif imageType == "2":
    imageExt = '.jpeg'
elif imageType == "3":
    imageExt = '.bmp'
else:
    imageExt = '.png'

#Make a folder for saved QRcodes
if not os.path.exists('QRs'):
    os.makedirs('QRs')
    print('Creating folder: "QRs"')
    print('===============================================')

#Make a sub folder for saved QRcodes from this run:
if not os.path.exists(qrFolder):
    os.makedirs(qrFolder)
    print('Creating folder: ' + qrFolder)
    print('===============================================')

#Open the CSV file, loop through each line and create a QR code:
lineCount = 0
with open(csvFile) as f:
    lines = csv.reader(f)
    for line in lines:
        lineCount += 1
        qrFilename = qrName + str(lineCount)

        #Check to see if we already have a previously created file with the same name:
        if os.path.exists(qrFolder + str(qrFilename) + imageExt):
            print('You already have a code named ' + qrFilename + '. I am renaming it ' + qrFilename + '-COPY')
            print('===============================================')
            qrFilename = qrFilename + '-COPY'

        # Create qr code instance
        qr = qrcode.QRCode()

        # Add data
        qr.box_size = int(boxPixels)
        qr.add_data(line[0]) #Add the data from column 1 of the CSV
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image()

        #Are we adding a caption?
        if doCaption:
            draw = ImageDraw.Draw(img)
            QRwidth, QRheight = img.size
            fontSize = 1 #starting font size
            qrLabel = line[1] #Get the caption from the 2nd column of the CSV file
            img_fraction = 0.90 # portion of image width you want text width to be
            fontHeightMax = qr.border * qr.box_size - 10 #Maximum height for captions
            captionX = 0 #Where to start the caption X coordinate
            captionY = 0 #Where to start the caption y coordinate
            print('Font height max is set to: ' + str(fontHeightMax))
            font = ImageFont.truetype(fontFile, fontSize)
            while font.getsize(qrLabel)[0] < img_fraction*QRwidth and font.getsize(qrLabel)[1] < fontHeightMax:
                fontSize += 1
                font = ImageFont.truetype(fontFile, fontSize)
            captionX = int(QRwidth - font.getsize(qrLabel)[0]) / 2 #Center the label
            print('Offset: ' + str(captionX))
            draw.text((captionX, captionY), qrLabel, font=font)

        # Save it somewhere, change the extension as needed:
        img.save(qrFolder + qrFilename + imageExt)
        print('QR Code successfully save as ' + qrFolder + qrFilename + imageExt)

print('Created ' + str(lineCount) + ' QR codes!')
print('=' *47)


import arabic_reshaper 
from bidi.algorithm import get_display 
from fpdf import FPDF

title = 'قائمة أفضل الكتب العربية'

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.add_font('trado', '', 'trado/trado.ttf', uni=True)
pdf.set_font('trado', '', 25)


class PDF(FPDF):
    def header(self):
        # self.image('site_logo.png', 10, 8, 25)
        self.set_font('helvetica', 'B', 25)
        self.cell(50)      # for padding
        title_w = self.get_string_width(title) + 7
        doc_w = self.w
        self.set_x ((doc_w - title_w)/2)

        self.set_draw_color(0, 80, 180) # border color
        self.set_fill_color(230, 230, 0) # background color
        self.set_text_color(220, 50, 50) # text color

        self.set_line_width(1.5)  # thickness of border

        self.cell(title_w, 25, title, border = True, ln=1, align='C', fill = 1)
        self.ln(20) # linebreak space
    
    def footer(self):
        self.set_y(-25) # position of the footer
        self.set_font('helvetica', 'I', 10)
        self.set_text_color(169, 169, 169) # text color
        self.cell(0, 15, f'Page {self.page_no()}', align='C')
    

    def QR_image(self,name):
        with open(name, 'rb') as fh:
            imgq = fh.read().decode('latin-1')
        
        self.multi_cell(0, 5, imgq)
        self.ln()
        self.set_font('trado', 'I', 25)
        self.cell(0, 5, 'End')
        self.add_page()



# pdf = PDF('P', 'mm', 'letter')
# pdf.add_page()

pdf.alias_nb_pages()  # for getting page number

pdf.set_auto_page_break(auto=True, margin = 21)
pdf.set_font('trado', '', 33)
# pdf.set_text_color(100,50,235)


print(list_data2)
exit()
x = 1
while x <= len(list_data2):
    titl = book_tag[x-1]
    auth = author[x-1]
    lst_data3 = list_data3[x-1]
    pdf.ln(60)
    pdf.cell(55)
    pdf.set_link(lst_data3)
    pdf.image(f'QRs/qr{x}.png', w=120, h=120, link=lst_data3)
    pdf.cell(120, 15, get_display(arabic_reshaper.reshape(titl)), ln=2, align='C')
    pdf.cell(120, 15, get_display(arabic_reshaper.reshape(auth)), ln=2, align='C')
    pdf.add_page()
    x +=1
    

pdf.output("Books.pdf")