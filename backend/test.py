#!/usr/bin/python3

from models import User, Link

ud = User(name='liry', username='ddsi', age=21)
ud.save()
us = User.get(1)

print(us)