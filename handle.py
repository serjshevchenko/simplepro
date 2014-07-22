import os
from ladon.server.wsgi import LadonWSGIApplication 
PATH = os.path.abspath(os.path.dirname(__file__))
application = LadonWSGIApplication(['calculator'], [os.path.join(PATH, 'modules')])

#~ def application (env, res) :
	#~ res('200 OK', [('Content-Type','text/html')])
	#~ return [b'hi there.']
