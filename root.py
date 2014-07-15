#!/usr/bin/env python

import os

import cherrypy
from cherrypy.process.plugins import Daemonizer
from jinja2 import Environment, PackageLoader

import modules

# CONSTANTS*
PATH = os.path.dirname(__file__)
#*

os.chdir(PATH)

env = Environment(loader=PackageLoader('simplepro', './public/templates'))

class Root (object) :

    settings = modules.Settings()

    @cherrypy.expose
    def index (self) :
        
        template = env.get_template('index.html')
        #~ html = '''<html>
                        #~ <head>
                            #~ <title> Index Page</title>
                            #~ <link type="text/css" rel="stylesheet" href="/static/css/style.css" />
                            #~ <script src="/static/js/script.js" text="text/javascript"></script>
                        #~ </head>
                        #~ <body>
                            #~ <h1>Hi there.</h1>
                        #~ </body>
                    #~ </html>
                #~ ''';
        #~ return html
        return template.render(locals())



        
cherrypy.config.update({
                    'server.socket_host': '0.0.0.0',
                    'server.socket_port': 8080,
                    'log.access_file': './log/access.log',
                    'log.error_file': './log/error.log',
                })        
        
config = {
            '/': {
                    #~ 'tools.sessions.on': True,
                    'tools.staticdir.root': PATH
                    
            },
            '/static': {
                    'tools.staticdir.on': True,
                    'tools.staticdir.dir': './public/static'
            },
         }

Daemonizer(cherrypy.engine).subscribe()
                    
cherrypy.quickstart(Root(), '/', config)

