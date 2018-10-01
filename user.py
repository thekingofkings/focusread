#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 22:33:47 2018

@author: hj
"""
from google.appengine.ext import ndb
from flask_login import UserMixin


class User(UserMixin, ndb.Model):
    """Models an individual registered user"""
    name = ndb.StringProperty()
    pwd = ndb.StringProperty()
    
    def get_id(self):
        return self.name