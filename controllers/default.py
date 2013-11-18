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
def roster():
    #query = ((auth.user.email == db.list.Assignee)
     #       & ( (db.list.Accept == False)
     #         & (db.list.Decline == False)
     #         & (db.list.Completed == False)
     #         & (db.list.Later == False)
     #         )
     #       )
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
             upload = URL('download'),
             #links=[dict(header=T('Edit Post'),body = lambda r:
             #A('Edit', _class='btn', _href=URL('default', 'edit', args=[r.id])))]
             )
    return dict(posts=posts)

def add_to_roster():
    form = SQLFORM(db.roster)
    if form.process().accepted:
        redirect(URL('default', 'roster'))
        session.flash = T('Inserted')
    return dict(form=form)

def calendar():
    message = T('This will show tournament schedule')
    return dict(message=message)

def hitting_partner_list():
    message = T('This will help people find hitting partners')
    return dict(message=message)

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
