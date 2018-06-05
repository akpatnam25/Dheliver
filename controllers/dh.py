
import requests

cowell = 'http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=05&locationName=Cowell&sName=&naFlag=', 'Cowell/Stevenson Dining Hall'
ten = 'http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=40&locationName=College+Nine+%26+Ten&sName=&naFlag=', 'Colleges Nine & Ten Dining Hall'
merill = 'http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=20&locationName=Crown+Merrill&sName=&naFlag=', 'Merill Cowell'
porter = 'http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=25&locationName=Porter&sName=&naFlag=', 'Porter College'
rcc = 'http://nutrition.sa.ucsc.edu/menuSamp.asp?locationNum=30&locationName=Rachel+Carson+Oakes+Dining+Hall&sName=&naFlag=', 'Rachel Carson College'

found = 'Found in '
array = [cowell,ten,merill,porter,rcc]
page = requests.get(cowell[0])
foundFlag = False
for college in array:
    page = requests.get(college[0])
    if "eggs" in page.content.lower():
        print("found in " + college[1])

