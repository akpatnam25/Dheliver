# Author: Srini Rangarajan
import re
import urllib.request
from bs4 import BeautifulSoup

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True

message_body = "eggs"

cowell = 'http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=05&locationName=Cowell&sName=&naFlag='
ten = 'http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=College+Nine+%26+Ten&sName=&naFlag='
merill = 'http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=20&locationName=Crown+Merrill&sName=&naFlag='
porter = 'http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=25&locationName=Porter&sName=&naFlag='
rcc = 'http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&sName=&naFlag='

#cowell
end_array=[]
breakfastIndex=0
lunchIndex=0
dinnerIndex=0
lateNightIndex=0

html = urllib.request.urlopen(cowell)
soup = BeautifulSoup(html, "html.parser")
data = soup.findAll(text=True)
result = filter(visible, data)
raw_code = list(result)
length = len(raw_code)

breakfastArray_cowell=[]
lunchArray_cowell=[]
dinnerArray_cowell=[]
lateNightArray_cowell=[]

wordbank=["\n","Recipe Name Is Displayed Here","Nutrition Info","\xa0"]

for x in raw_code:
    for y in wordbank:
        if y in x:
            break
    else:
        end_array.append(x)
for x in end_array:
    if 'No Data Available' in x:
        break
    if "Breakfast" in x:
        breakfastIndex=end_array.index(x)
    elif "Lunch" in x:
        lunchIndex=end_array.index(x)
    elif "Dinner" in x:
        dinnerIndex=end_array.index(x)
    #elif "Late Night" in x:
    #    lateNightIndex=end_array.index(x)

breakfastArray_cowell=end_array[breakfastIndex:lunchIndex]
lunchArray_cowell=end_array[lunchIndex+1:dinnerIndex]
dinnerArray_cowell=end_array[dinnerIndex+1:-9]
#lateNightArray_cowell=end_array[lateNightIndex+1:-9]

#ten
end_array=[]
breakfastIndex=0
lunchIndex=0
dinnerIndex=0
lateNightIndex=0

html = urllib.request.urlopen(ten)
soup = BeautifulSoup(html, "html.parser")
data = soup.findAll(text=True)
result = filter(visible, data)
raw_code = list(result)
length = len(raw_code)

breakfastArray_ten=[]
lunchArray_ten=[]
dinnerArray_ten=[]
lateNightArray_ten=[]

wordbank=["\n","Recipe Name Is Displayed Here","Nutrition Info","\xa0"]

for x in raw_code:
    for y in wordbank:
        if y in x:
            break
    else:
        end_array.append(x)
for x in end_array:
    if 'No Data Available' in x:
        break
    if "Breakfast" in x:
        breakfastIndex=end_array.index(x)
    elif "Lunch" in x:
        lunchIndex=end_array.index(x)
    elif "Dinner" in x:
        dinnerIndex=end_array.index(x)
    elif "Late Night" in x:
        lateNightIndex=end_array.index(x)


breakfastArray_ten=end_array[breakfastIndex:lunchIndex]
lunchArray_ten=end_array[lunchIndex+1:dinnerIndex]
dinnerArray_ten=end_array[dinnerIndex+1:lateNightIndex]
lateNightArray_ten=end_array[lateNightIndex+1:-9]

#merill
end_array=[]
breakfastIndex=0
lunchIndex=0
dinnerIndex=0
lateNightIndex=0

html = urllib.request.urlopen(merill)
soup = BeautifulSoup(html, "html.parser")
data = soup.findAll(text=True)
result = filter(visible, data)
raw_code = list(result)
length = len(raw_code)

breakfastArray_merill=[]
lunchArray_merill=[]
dinnerArray_merill=[]
lateNightArray_merill=[]

wordbank=["\n","Recipe Name Is Displayed Here","Nutrition Info","\xa0"]

for x in raw_code:
    for y in wordbank:
        if y in x:
            break
    else:
        end_array.append(x)
for x in end_array:
    if 'No Data Available' in x:
        break
    if "Breakfast" in x:
        breakfastIndex=end_array.index(x)
    elif "Lunch" in x:
        lunchIndex=end_array.index(x)
    elif "Dinner" in x:
        dinnerIndex=end_array.index(x)
    elif "Late Night" in x:
        lateNightIndex=end_array.index(x)

breakfastArray_merill=end_array[breakfastIndex:lunchIndex]
lunchArray_merill=end_array[lunchIndex+1:dinnerIndex]
dinnerArray_merill=end_array[dinnerIndex+1:lateNightIndex]
lateNightArray_merill=end_array[lateNightIndex+1:-9]

#porter
end_array=[]
breakfastIndex=0
lunchIndex=0
dinnerIndex=0
lateNightIndex=0

html = urllib.request.urlopen(porter)
soup = BeautifulSoup(html, "html.parser")
data = soup.findAll(text=True)
result = filter(visible, data)
raw_code = list(result)
length = len(raw_code)

breakfastArray_porter=[]
lunchArray_porter=[]
dinnerArray_porter=[]
lateNightArray_porter=[]

wordbank=["\n","Recipe Name Is Displayed Here","Nutrition Info","\xa0"]

for x in raw_code:
    for y in wordbank:
        if y in x:
            break
    else:
        end_array.append(x)
for x in end_array:
    if 'No Data Available' in x:
        break
    if "Breakfast" in x:
        breakfastIndex=end_array.index(x)
    elif "Lunch" in x:
        lunchIndex=end_array.index(x)
    elif "Dinner" in x:
        dinnerIndex=end_array.index(x)
    elif "Late Night" in x:
        lateNightIndex=end_array.index(x)

breakfastArray_porter=end_array[breakfastIndex:lunchIndex]
lunchArray_porter=end_array[lunchIndex+1:dinnerIndex]
dinnerArray_porter=end_array[dinnerIndex+1:lateNightIndex]
lateNightArray_porter=end_array[lateNightIndex+1:-9]

#rcc
end_array=[]
breakfastIndex=0
lunchIndex=0
dinnerIndex=0
lateNightIndex=0

html = urllib.request.urlopen(rcc)
soup = BeautifulSoup(html, "html.parser")
data = soup.findAll(text=True)
result = filter(visible, data)
raw_code = list(result)
length = len(raw_code)

breakfastArray_rcc=[]
lunchArray_rcc=[]
dinnerArray_rcc=[]
lateNightArray_rcc=[]

wordbank=["\n","Recipe Name Is Displayed Here","Nutrition Info","\xa0"]

for x in raw_code:
    for y in wordbank:
        if y in x:
            break
    else:
        end_array.append(x)
for x in end_array:
    if 'No Data Available' in x:
        break
    if "Breakfast" in x:
        breakfastIndex=end_array.index(x)
    elif "Lunch" in x:
        lunchIndex=end_array.index(x)
    elif "Dinner" in x:
        dinnerIndex=end_array.index(x)
    #elif "Late Night" in x:
    #    lateNightIndex=end_array.index(x)

breakfastArray_rcc=end_array[breakfastIndex:lunchIndex]
lunchArray_rcc=end_array[lunchIndex+1:dinnerIndex]
dinnerArray_rcc=end_array[dinnerIndex+1:-9]
#lateNightArray_rcc=end_array[lateNightIndex+1:-9]

#lowering all

breakfastArray_merill=[x.lower() for x in breakfastArray_merill]
lunchArray_merill=[x.lower() for x in lunchArray_merill]
dinnerArray_merill=[x.lower() for x in dinnerArray_merill]
lateNightArray_merill=[x.lower() for x in lateNightArray_merill]
breakfastArray_ten = [x.lower() for x in breakfastArray_ten]
lunchArray_ten=[x.lower() for x in lunchArray_ten]
dinnerArray_ten=[x.lower() for x in dinnerArray_ten]
lateNightArray_ten=[x.lower() for x in lateNightArray_ten]
breakfastArray_cowell=[x.lower() for x in breakfastArray_cowell]
lunchArray_cowell=[x.lower() for x in lunchArray_cowell]
dinnerArray_cowell=[x.lower() for x in dinnerArray_cowell]
lateNightArray_cowell=[x.lower() for x in lateNightArray_cowell]
breakfastArray_porter=[x.lower() for x in breakfastArray_porter]
lunchArray_porter=[x.lower() for x in lunchArray_porter]
dinnerArray_porter=[x.lower() for x in dinnerArray_porter]
lateNightArray_porter=[x.lower() for x in lateNightArray_porter]
breakfastArray_rcc=[x.lower() for x in breakfastArray_rcc]
lunchArray_rcc=[x.lower() for x in lunchArray_rcc]
dinnerArray_rcc=[x.lower() for x in dinnerArray_rcc]
lateNightArray_rcc=[x.lower() for x in lateNightArray_rcc]

new_path = '//Users/srini/Documents/CMPS183/web2py/applications/Dheliver/resources/dRCC.txt'
new_days = open(new_path,'w')
new_days.write(str(dinnerArray_rcc))
print (dinnerArray_rcc)