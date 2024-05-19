#!/usr/bin/python3

from models import User, Link

newone: User = User.get(7)
link:list[Link]=  newone.links
print(link[0].user)