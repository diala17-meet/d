from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql

Base = declarative_base()

class Person(Base):
	__tablename__ = 'person'
	id = Column(Integer, primary_key=True)
	name = Column(String(60))
	username = Column(String(60))
	password = Column(String(60))
	gender = Column(String(30))
	nationality = Column(String(30))
	bio = Column(String(300))
	rating = Column(Integer)
	pic = Column(String(200))


class Event(Base):
	__tablename__ = 'event'
	id = Column(Integer, primary_key=True)
	title = Column(String(60))
	date = Column(Date)
	description = Column(String(300))
	location = Column(String(60))
	owner_id = Column(Integer, ForeignKey("person.id"))
	owner = relationship("Person")


class Attendance(Base):
	__tablename__ = 'attendance'
	id = Column(Integer, primary_key=True)
	person_id = Column(Integer, ForeignKey("person.id"))
	person = relationship("Person")
	event_id = Column(Integer, ForeignKey("event.id"))
	event = relationship("Event")
	chef_flag = Column(Boolean)
	

engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
dbsession = DBSession()