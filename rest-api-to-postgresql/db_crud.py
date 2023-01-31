import db_connection
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
import db_connection
from db_models import Launch, Base, Mission, Rocket
from db_schemavalidation import *
from sqlalchemy.orm import sessionmaker
from get_data import Data
load_dotenv()

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)



url_connection = db_connection.get_url_postgres(os.environ['DATABASE_USER'],
               os.environ['DATABASE_PWD'],
               os.environ['DATABASE_HOST'],
               5432,
               'spatial')

engine = create_engine(url_connection)

#creating session
Session = sessionmaker(bind=engine)
s = Session()

if __name__=="__main__":

    recreate_database()
    data_obj = Data()
    data = data_obj.get("https://ll.thespacedevs.com/2.2.0/launch/upcoming/")
    treated_data = data_obj.return_treated_data(data)

    
    for launch in treated_data[0]:
        if(data_obj.validate_schema(my_data=launch, my_schema=launch_schema)):
            row = Launch(**launch)
            s.add(row)
            print("Rows Inserted")
        else:
            print("Register did not pass data validation. Rows not inserted")
        
    for mission in treated_data[1]:
        if(data_obj.validate_schema(my_data=mission, my_schema=mission_schema)):
            row = Mission(**mission)
            s.add(row)
            print("Rows Inserted")
        else:
            print("Register did not pass data validation. Rows not inserted")
    
    for rocket in treated_data[2]:
        if(data_obj.validate_schema(my_data=rocket, my_schema=rocket_schema)):
            row = Rocket(**rocket)
            s.add(row)
            print("Rows Inserted")
        else:
            print("Register did not pass data validation. Rows not inserted")

    s.commit()
    s.close()

