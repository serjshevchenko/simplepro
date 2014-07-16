#!/usr/bin/env python

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('public', 'templates'))


def getEnvironment () :
    return env


def page (func) :  
    def _page (*args, **kargs) :
        self = args[0]
        template = None
        if func.__name__ in self.__class__.__dict__:
            template = func.__name__
        else :
            for (key, val) in self.__class__.__dict__.items() :
                if val == _page :
                    template = key
        temp = env.get_template('pages/'+self.__class__.__name__.lower()+'/'+template+'.html')
        vars = func(*args, **kargs) or {}
        return temp.render(**vars)

    for attr in dir(func) :
            if not attr.startswith('__') or not attr.endswith('__') :
                setattr(_page, attr, getattr(func, attr))
    return _page
