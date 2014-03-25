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

'''TEST CLASS'''
class Test(Base):
    __tablename__ = 'test'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return "<User(name='%s')>" % self.name

Base.metadata.create_all(engine)
tester = Test(name='bob')

session.add(tester)
obj = session.query(Test).filter_by(name='bob').first()
print obj


