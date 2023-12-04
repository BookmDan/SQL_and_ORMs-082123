#!/usr/bin/env python3

from __init__ import db_connection, db_cursor
from pet import Pet
from owner import Owner

import ipdb;

def reset_database():
    Pet.drop_table()
    Pet.create_table()
    Owner.drop_table()
    Owner.create_table()

reset_database()
print("")
elsie = Pet("Elsie", "dog")
print(elsie)

elsie.save()
print(elsie)

snoopy = Pet("Snoopy", "dog")
snoopy.save()

lemon = Pet.create("Lemon", "dog")


print("")

ipdb.set_trace()
