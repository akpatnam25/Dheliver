def getCowellBreakFast():
    f = open('cowellBreakfast.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(cowellBreakfast=words)


def getCowellLunch():
    f = open('cowellLunch.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(cowellLunch=words)



def getCowellDinner():
    f = open('cowellDinner.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
   return dict(cowellDinner=words)


def getCowellLateNight():
    f = open('cowellLateNight.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(cowellLateNight=words)


def getMerillBreakfast():
    f = open('merillBreakfast.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(merillBreakfast=words)


def getMerillLunch():
    f = open('merillLunch.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(merillLunch=words)

def getMerillDinner():
    f = open('merillDinner.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(merillDinner=words)

def getMerillLateNight():
    f = open('merillLateNight.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(merillLateNight=words)

def getPorterBreakfast():
    f = open('porterBreakfast.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(porterBreakfast=words)

def getPorterLunch():
    f = open('porterLunch.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(porterLunch=words)

def getPorterDinner():
    f = open('porterDinner.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(porterDinner=words)


def getPorterLateNight():
    f = open('porterLateNight.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(porterLateNight=words)


def getRccBreakfast():
    f = open('rccBreakfast.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(rccBreakfast=words)


def getRccLunch():
    f = open('rccLunch.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(rccLunch=words)


def getRccDinner():
    f = open('rccDinner.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(rccDinner=words)


def getRccLateNight():
    f = open('rccLateNight.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(rccLateNight=words)


def getTenBreakfast():
    f = open('tenBreakfast.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(tenBreakfast=words)


def getTenLunch():
    f = open('tenLunch.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(tenLunch=words)


def getTenDinner():
    f = open('tenDinner.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(tenDinner=words)


def getTenLateNight():
    f = open('tenLateNight.txt','r')
    message = f.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return dict(tenLateNight=words)