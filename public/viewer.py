#!/usr/bin/env python
import types, os

from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('public', 'templates'))


def getEnvironment () :
    return env


def display (func=None, template=None) :  
    
    def _display (func) :
        
        def display_decor (*args, **kargs) :
            path = 'pages';
            if template is None:
                self = args[0]
                classname = self.__class__.__name__.lower()
                if func.__name__ in self.__class__.__dict__:
                    method_name = func.__name__.lower()
                else :
                    for (key, val) in self.__class__.__dict__.items() :
                        if val == display_decor :
                            method_name = key.lower()
                path = os.path.join(path, os.path.normcase(classname+'/'+method_name+'.html'))
            else : path = os.path.join(path, os.path.normcase(template))

            temp = env.get_template(path)
            vars = func(*args, **kargs) or {}
            return temp.render(**vars)

        for attr in dir(func) :
                if not attr.startswith('__') or not attr.endswith('__') :
                    setattr(display_decor, attr, getattr(func, attr))
                
        return display_decor       

    if isinstance(func, (types.FunctionType, types.MethodType)):
        return _display(func)

    return _display

