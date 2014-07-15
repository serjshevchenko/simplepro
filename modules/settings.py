#!/usr/bin/env python

import cherrypy

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('public', 'templates'))

class Settings (object) :
    
    @cherrypy.expose
    def index (self) :
        temp = env.get_template('pages/settings/index.html')
        return temp.render(message='Settings')
    
    @cherrypy.expose
    def edit (self, id) :
        return 'Edit info of record # %s' % (id or 0);
