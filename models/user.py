from . import orm

class User (orm.getBase()) :
    
    __tablename__ = 'myuser'
    
    def __init__ (self, name='', fullname='', pwd='') :
        self.name = name
        self.fullname = fullname
        self.password = pwd
    
    id = orm.Column(orm.Integer, primary_key=True)
    name = orm.Column(orm.String)
    fullname = orm.Column(orm.String)
    password = orm.Column(orm.String)
    
    def __repr__ (self) :
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)

    def save (self) :
        if (self.name and self.password) :
            orm.getSession('user').add(self)
            orm.getSession('user').commit()

