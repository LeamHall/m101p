#!/usr/local/bin/python

import pymongo
from pymongo import MongoClient

connection = MongoClient("localhost", 27017)

db = connection.foobar
blog = db.blog
item = blog.find_one()
print item['title']
