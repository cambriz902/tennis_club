#Final Project tables
from gluon.tools import Auth

db = DAL("sqlite://storage.sqlite")

db.define_table('hitting_partner',
   Field('name', 'text'),
   Field('email', 'text'),
   Field('rating', 'text')
   )

