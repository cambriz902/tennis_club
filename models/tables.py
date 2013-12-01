#Final Project tables
# IMPORTS DATE AND TIME WHEN ACCESSED
from datetime import datetime
from gluon.tools import Auth
# SET DATABASE
db = DAL("sqlite://storage.sqlite")
#===============================================================
# GET() METHODS:
#               RETRIEVES FIRST AND LAST NAME OF USER
#               RETRIEVES USER'S EMAIL
#===============================================================
def get_name():
    if auth.user:
        return auth.user.first_name + " " + auth.user.last_name
    else:
        return 'No Name Specified'
def get_email():
    if auth.user:
        return auth.user.email
    else:
        return 'No E-mail Specified'
#***************************************************************
# DEFINE A TABLE FOR TO-DO-LIST:
#***************************************************************
db.define_table ('roster',
   Field('Name','text'),
   Field('year', 'text'),
   Field('studying', 'text'),
   Field('hometown', 'text'),
   Field('profile_pic', 'upload'),
   format = '%(Title)s')

db.define_table ('hitting_partner_list',
   Field(
         'Username',
         writable = False,
         default  = get_name,
         unique   = True
         ),
   Field(
         'Email',
         writable = False,
         default  = get_email,
         unique   = True
         ),
   Field('rating', 'double', default = 0.0),
   format = '%(Title)s')

db.roster.hometown.requires = IS_NOT_EMPTY()
db.roster.year.requires  = IS_NOT_EMPTY()



