#!/usr/bin/env python

import cherrypy
from public import viewer
from models import user

class Settings (object) :
    
    @cherrypy.expose
    @viewer.page
    def index (self) :
        #~ bob = user.User('Timmy', 'T. Dog', '1111')
        #~ bob.save()
        return {
            'message':'Settings'
        }
    
    @viewer.page
    @cherrypy.expose
    def edit (self, id) :
        return {'id':id}
