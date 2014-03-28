from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData

''' CREATE ENGINE WITH LOGGING ON '''
engine = create_engine('sqlite:///:memory:', echo=True)

'''CREATE SESSION FACTORY BOUND TO ENGINE AND GET A SESSION "session" '''
Session = sessionmaker(bind=engine)
session = Session()

'''THE BASE FOR OUR APPLICATION'''
Base = declarative_base()

'''TEST ORM CLASS'''
class Test(Base):
    __tablename__ = 'test'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return "<User(name='%s')>" % self.name

'''Link ORM class'''
class Link(Base):
    __tablename__ = 'links'
    
    id = Column(Integer, primary_key=True)
    url = Column(String)
    parent = Column(String)
    depth = Column(Integer)
    
    def __repr__(self):
        return "<Link(url='%s')>" % self.url
'''CREATE ALL OF THE THINGS'''
Base.metadata.create_all(engine)

'''Method for adding objects to the db
'''
def add_obj_to_session(_object):
    session.add(_object)
    try:
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

testerlink = Link(url='blah',parent='', depth=1)
add_obj_to_session(testerlink)
print session.query(Link).filter_by(url='blah').first()

tester = Test(name='bob')
add_obj_to_session(tester)
print session.query(Test).filter_by(name='bob').first()
