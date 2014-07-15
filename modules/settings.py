#!/usr/bin/env python

import cherrypy

class Settings (object) :
    
    @cherrypy.expose
    def index (self) :
        return 'settigns info...'
    
    @cherrypy.expose    
    def edit (self, id) :
        return 'Edit info of record # %s' % (id or 0);
