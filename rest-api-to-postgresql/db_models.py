from sqlite3 import Timestamp
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import *



Base = declarative_base()

class Launch(Base):
    __tablename__ = "launch"
    launch_id = Column(String, primary_key=True)
    launch_name = Column(String)
    launch_status= Column(String)
    launch_status_description = Column(String)
    launch_window_start = Column(DateTime)
    launch_window_end= Column(DateTime)
    launch_provider_name= Column(String)

class Rocket(Base):
    __tablename__ = "rocket"
    rocket_id = Column(Integer, primary_key=True)
    launch_id = Column(String, ForeignKey(Launch.launch_id))
    rocket_fullname = Column(String)
    rocket_family = Column(String)
    rocket_variant = Column(String)

class Mission(Base):
    __tablename__ = "mission"
    mission_id = Column(Integer, primary_key=True)
    launch_id = Column(String, ForeignKey(Launch.launch_id))
    mission_name = Column(String)
    mission_description = Column(String)
    mission_type = Column(String)
   

