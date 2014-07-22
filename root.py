#!/usr/bin/env python
import os
import cherrypy
from cherrypy.process.plugins import Daemonizer
from jinja2 import Environment, PackageLoader
from ladon.server.wsgi import LadonWSGIApplication 
import modules

PATH = os.path.abspath(os.path.dirname(__file__))

os.chdir(PATH)

app = LadonWSGIApplication(['calculator'], [os.path.join(PATH, 'modules')])


env = Environment(loader=PackageLoader('public', 'templates'))

class Root (object) :

    settings = modules.Settings()

    @cherrypy.expose
    def index (self) :
        template = env.get_template('index.html')
        return template.render(message='Hi There!')



        
cherrypy.config.update({
                    'server.socket_host': '0.0.0.0',
                    'server.socket_port': 8080,
                    'log.access_file': './log/access.log',
                    'log.error_file': './log/error.log',
                })        
        
config = {
            '/': {
                    'tools.sessions.on': True,
                    'tools.staticdir.root': PATH
                    
            },
            '/static': {
                    'tools.staticdir.on': True,
                    'tools.staticdir.dir': './public/static'
            },
         }

                    


from cherrypy import _cptree
from cherrypy.wsgiserver import CherryPyWSGIServer
from cherrypy.process.servers import ServerAdapter

#~ cherrypy.server.unsubscribe()

wsgiapp = cherrypy.Application(modules.Settings())
wsgiServer = CherryPyWSGIServer(('0.0.0.0', 8070), wsgiapp)
ServerAdapter(cherrypy.engine, wsgiServer).subscribe()

wsgiServer = CherryPyWSGIServer(('0.0.0.0', 8090), app)
ServerAdapter(cherrypy.engine, wsgiServer).subscribe()

cherrypy.tree.mount(Root(), '/', config)

Daemonizer(cherrypy.engine).subscribe()

cherrypy.engine.signals.subscribe()
cherrypy.engine.start()


#~ cherrypy.quickstart(Root(), '/', config)



#NOTE how must be done
#~ cherrypy.server.unsubscribe()
#~ 
#~ from cherrypy import _cptree
#~ from cherrypy.wsgiserver import CherryPyWSGIServer
#~ 
#~ tree = _cptree.Tree()
#~ app = tree.mount(modules.Settings())
#~ 
#~ from cherrypy.process.servers import ServerAdapter
#~ 
#~ wsgiServer = CherryPyWSGIServer(('0.0.0.0', 8090), app.wsgiapp)
#~ ServerAdapter(cherrypy.engine, wsgiServer).subscribe()
#~ Daemonizer(cherrypy.engine).subscribe()
#~ cherrypy.engine.start()
