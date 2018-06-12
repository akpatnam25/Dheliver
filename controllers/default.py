# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
import os

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/order.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """

    return dict()


def no_swearing(form):
    if 'fool' in form.vars.Delivery_Time:
        form.errors.memo = T('No swearing please')

@auth.requires_login()
def add():
    """Adds a checklist."""
    form = SQLFORM(db.checklist)
    if form.process(onvalidation=no_swearing).accepted:
        session.flash = T("Checklist added.")
        redirect(URL('default','index'))
    elif form.errors:
        session.flash = T('Please correct the info')
    return dict(form=form)

def test():
    print "HELLO"

@auth.requires_login()
@auth.requires_signature()
def delete():

    q = ((db.checklist.user_email == auth.user.email) &
         (db.checklist.id == request.args(0)))
    db(q).delete()
    redirect(URL('default', 'index'))

@auth.requires_login()
def togglePublic():
    if request.args(0) is not None:
        q = ((db.checklist.user_email == auth.user.email) &
             (db.checklist.id == request.args(0)))
        cl = db(q).select().first()

        cl.update_record(is_public= not cl.is_public)
    redirect(URL('default', 'index'))


@auth.requires_login()
def edit():
    """
    - "/edit/3" it offers a form to edit a checklist.
    'edit' is the controller (this function)
    '3' is request.args[0]
    """
    if request.args(0) is None:
        # We send you back to the general index.
        redirect(URL('default', 'index'))
    else:
        q = ((db.checklist.user_email == auth.user.email) &
             (db.checklist.id == request.args(0)))
        # I fish out the first element of the query, if there is one, otherwise None.
        cl = db(q).select().first()
        if cl is None:
            session.flash = T('Not Authorized')
            redirect(URL('default', 'index'))
        # Always write invariants in your code.
        # Here, the invariant is that the checklist is known to exist.
        # Is this an edit form?
        form = SQLFORM(db.checklist, record=cl, deletable=False)
        if form.process(onvalidation=no_swearing).accepted:
            # At this point, the record has already been edited.
            session.flash = T('Checklist edited.')
            redirect(URL('default', 'index'))
        elif form.errors:
            session.flash = T('Please enter correct values.')
    return dict(form=form)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

@auth.requires_login()
def togglePublic():
    q = ((db.checklist.user_email == auth.user.email) &
         (db.checklist.id == request.args(0)))
    cl = db(q).select().first()


    redirect(URL('default', 'deliveries'))


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def order():


    return dict(cowellBreakfast = getCowellBreakFast(),
                cowellLunch = getCowellLunch(),
                cowellDinner = getCowellDinner(),
                crownBreakfast = getMerillBreakfast(),
                crownLunch = getMerillLunch(),
                crownDinner = getMerillDinner(),
                tenBreakfast = getTenBreakfast(),
                tenLunch = getTenLunch(),
                tenDinner = getTenDinner(),
                porterBreakfast = getPorterBreakfast(),
                porterLunch = getPorterLunch(),
                porterDinner = getPorterDinner(),
                rccBreakfast = getRccBreakfast(),
                rccLunch = getRccLunch(),
                rccDinner = getRccDinner()
            )

def about():

    return dict()

def checkout():

    if request.vars.item == None:
        return dict()
    else:
        print request.vars.item
        print request.vars.in_cart
        in_cart = request.vars.in_cart
        item_selected = request.vars.item
        loc = request.vars.location
        time = request.vars.time
        print item_selected
        db.orderlist.insert(user_email=auth.user.email, dh=loc, times=time, menu_item=item_selected)
        return dict()


def faq():
    return dict()

def deliveries():
    publists = db().select(db.checklist.ALL)
    orderlists = db().select(db.orderlist.ALL)
    return dict(publists=publists, orderlists=orderlists)

def getCowellBreakFast():
    infile = open(os.path.join(request.folder, 'controllers', 'cowellBreakfast.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    if 'breakfast' in words:
        words.remove('breakfast')
    return words


def getCowellLunch():
    infile = open(os.path.join(request.folder, 'controllers', 'cowellLunch.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    if 'lunch' in words:
        words.remove('breakfast')
    return words


def getCowellDinner():
    infile = open(os.path.join(request.folder, 'controllers', 'cowellDinner.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    if 'dinner' in words:
        words.remove('breakfast')
    return words


def getCowellLateNight():
    infile = open(os.path.join(request.folder, 'controllers', 'cowellLateNight.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return words


def getMerillBreakfast():
    infile = open(os.path.join(request.folder, 'controllers', 'merillBreakfast.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    if 'breakfast' in words:
        words.remove('breakfast')
    return words


def getMerillLunch():
    infile = open(os.path.join(request.folder, 'controllers', 'merillLunch.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    if 'lunch' in words:
        words.remove('breakfast')
    return words

def getMerillDinner():
    infile = open(os.path.join(request.folder, 'controllers', 'merillDinner.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    if 'dinner' in words:
        words.remove('breakfast')
    return words

def getMerillLateNight():
    infile = open(os.path.join(request.folder, 'controllers', 'merillLateNight.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return words

def getPorterBreakfast():
    infile = open(os.path.join(request.folder, 'controllers', 'porterBreakfast.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    if 'breakfast' in words:
        words.remove('breakfast')
    return words

def getPorterLunch():
    infile = open(os.path.join(request.folder, 'controllers', 'porterLunch.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    if 'lunch' in words:
        words.remove('breakfast')
    return words

def getPorterDinner():
    infile = open(os.path.join(request.folder, 'controllers', 'porterDinner.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    if 'dinner' in words:
        words.remove('breakfast')
    return words


def getPorterLateNight():
    infile = open(os.path.join(request.folder, 'controllers', 'porterLateNight.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return words


def getRccBreakfast():
    infile = open(os.path.join(request.folder, 'controllers', 'rccBreakfast.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    if 'breakfast' in words:
        words.remove('breakfast')
    return words


def getRccLunch():
    infile = open(os.path.join(request.folder, 'controllers', 'rccLunch.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    if 'lunch' in words:
        words.remove('breakfast')
    return words


def getRccDinner():
    infile = open(os.path.join(request.folder, 'controllers', 'rccDinner.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    if 'dinner' in words:
        words.remove('breakfast')
    return words


def getRccLateNight():
    infile = open(os.path.join(request.folder, 'controllers', 'rccLateNight.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return words


def getTenBreakfast():
    infile = open(os.path.join(request.folder, 'controllers', 'tenBreakfast.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    if 'breakfast' in words:
        words.remove('breakfast')
    return words


def getTenLunch():
    infile = open(os.path.join(request.folder, 'controllers', 'tenLunch.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    if 'lunch' in words:
        words.remove('breakfast')
    return words


def getTenDinner():
    infile = open(os.path.join(request.folder, 'controllers', 'tenDinner.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    if 'dinner' in words:
        words.remove('breakfast')
    return words


def getTenLateNight():
    infile = open(os.path.join(request.folder, 'controllers', 'tenLateNight.txt'))
    message = infile.read()
    strMessage = str(message)
    finalStr = ""
    for i in range(len(strMessage)-3):
        if strMessage[i].isalpha() :
            finalStr += strMessage[i]
        else:
            finalStr += " "
    words = finalStr.split("    ")
    words[0] = words[0].replace(" ", "")
    return words
