# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

#########################################################################
## New pages added
#########################################################################
@auth.requires_login()
def roster():
    if auth.user.email == "ucsantacruztennisclub@gmail.com":
        posts = SQLFORM.grid(db.roster,
                 fields=[
                         db.roster.Name,
                         db.roster.studying,
                         db.roster.year,
                         db.roster.hometown,
                         ],
                 deletable=True,
                 csv = False,
                 details = False,
                 create = True,
                 editable = True,
                 searchable = False,
                 )
    else:
        posts = SQLFORM.grid(db.roster,
                     fields=[
                             db.roster.Name,
                             db.roster.studying,
                             db.roster.year,
                             db.roster.hometown,
                             ],
                     deletable=True,
                     csv = False,
                     details = False,
                     create = False,
                     editable = True,
                     searchable = False,
                     )
    pass
    return dict(posts=posts)

@auth.requires_login()
def add_to_roster():
    form = SQLFORM(db.roster)
    if form.process().accepted:
        redirect(URL('default', 'roster'))
        session.flash = T('Inserted')
    return dict(form=form)

def calendar():
    message = T('This will show tournament schedule')
    return dict(message=message)

@auth.requires_login()
def hitting_partner_list():
    if db(db.hitting_partner_list.Email == auth.user.email, db.hitting_partner_list.rating == 0.0).isempty() :
        hpl_grid = SQLFORM.grid(db.hitting_partner_list,
             fields=[
                     db.hitting_partner_list.Username,
                     db.hitting_partner_list.Email,
                     db.hitting_partner_list.rating,
                     ],
             deletable=False,
             csv = False,
             details = False,
             create = True,
             editable = False,
             searchable = False,
             )
    elif auth.user.email == "ucsantacruztennisclub@gmail.com":
        hpl_grid = SQLFORM.grid(db.hitting_partner_list,
             fields=[
                     db.hitting_partner_list.Username,
                     db.hitting_partner_list.Email,
                     db.hitting_partner_list.rating,
                     ],
             deletable=True,
             csv = False,
             details = False,
             create = False,
             editable = True,
             searchable = False,
             )
    else:
        hpl_grid = SQLFORM.grid(db.hitting_partner_list,
             fields=[
                     db.hitting_partner_list.Username,
                     db.hitting_partner_list.Email,
                     db.hitting_partner_list.rating,
                     ],
             deletable=False,
             csv = False,
             details = False,
             create = False,
             editable = False,
             searchable = False,
             )
    pass
    return dict(hpl_grid=hpl_grid)

def faq():
    message = T('This will answer frequently asked questions')
    return dict(message=message)

def contact():
    message = T('This will have contact information')
    return dict(message=message)

#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.title = T("UC Santa Cruz Tennis Club")
    response.flash = T("Welcome to web2py!")
    return dict(message=T('Hello World'))


def user():
    
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
