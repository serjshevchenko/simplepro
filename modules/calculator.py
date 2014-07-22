#~ import cherrypy
from ladon.ladonizer import ladonize

class Calculator (object) :
    
    #~ @cherrypy.expose
    @ladonize(int, int, rtype=int)
    def add (self, a, b) :
        return a+b
        
    #~ @cherrypy.expose
    def index (self) :
        return 'calculator page'
    
