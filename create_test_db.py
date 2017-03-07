from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import ENUM, BOOLEAN
import sqlalchemy
from sqlalchemy.exc import ProgrammingError

Base = declarative_base()

engine = sqlalchemy.create_engine('mysql+pymysql://root:ThisTime43@localhost') # connect to server

try:
    engine.connect()
    engine.execute("CREATE DATABASE itequipdb") #create db
except ProgrammingError:
    pass

# MySQL
mysql_db_username = 'root'
mysql_db_password = 'ThisTime43'
mysql_db_name = 'itequipdb'
mysql_db_hostname = 'localhost'

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER=mysql_db_username,
                                                                                        DB_PASS=mysql_db_password,
                                                                                        DB_ADDR=mysql_db_hostname,
                                                                                        DB_NAME=mysql_db_name)



class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    create_ts = Column(DateTime)
    skill_level = Column(Integer)
    email_address = Column(String(128))
    trade = Column(String(128))

 #   children = relationship("Device")

class Device(Base):
    __tablename__ = 'device'
    id = Column(Integer, primary_key=True)
    history = Column(String(255))
    #parent_id = Column(Integer, ForeignKey('employee.id'))

class Ipads(Base):
    __tablename__ = 'ipads'
    serial = Column(String(128), primary_key=True)
    model = Column(String(128))
    storage_capacity = Column(String(128))
    date_purchased = Column(DateTime)
    #parent_id = Column(Integer, ForeignKey('device.id'))

class Fob(Base):
    __tablename__ = 'fob'
    num = Column(Integer, unique=True, primary_key=True)
    serial = Column(String(64), unique=True)

class Computers(Base):
    __tablename__ = 'computers'
    computer_id = Column(String(64), unique=True, primary_key=True)
    computer_name = Column(String(64), unique=True)
    brand = Column(ENUM('Acer','Custom','Dell','HP','Lenovo'))
    model = Column(String(64))
    serial = Column(String(128), unique=True)
    computer_type = Column(String(64))
    operating_system = Column(String(64))
    notes = Column(String(512))
    retired = Column(BOOLEAN())
    disposed = Column(BOOLEAN())
    disposed_date = Column(DateTime)
    aquired_date = Column(DateTime)
    purchase_price = Column(Integer)
    vendor_id = Column(ENUM('NewEggBusiness','Connection','Insight','Dell','HP','CDW'))
    warranty_start = Column(DateTime)
    warranty_length = Column(Integer)
    warranty_end = Column(DateTime)
    employee_id = Column(Integer)
    history = Column(String(255))
    
class Printers(Base):
    __tablename__ = 'printers'
    printer_id = Column(String(64), unique=True, primary_key=True)
    brand = Column(ENUM('Brother','Xerox','HP','Cannon'))
    model = Column(String(64))
    printer_type = Column(ENUM('Ink','Toner'))
    aquired_date = Column(DateTime)
    vendor_id = Column(ENUM('NewEggBusiness','Connection','Insight','Dell','HP','CDW'))

class Phone_Account(Base):
    __tablename__ = 'phone_account'
    phone_number = Column(String(16), unique=True, primary_key=True)
    phone_model = Column(String(16))
    phone_os = Column(ENUM('iOS', 'Android'))
    notes = Column(String(255))

class Vendors(Base):
    __tablename__ = 'vendors'
    vendor_id = Column(String(64), unique=True, primary_key=True)
    current_rep = Column(String(96))
    phone_number = Column(String(16))
    email_address = Column(String(128))
    
class Printer_Model(Base):
    __tablename__ = 'printer_model'
    printer_model = Column(String(64), unique=True, primary_key=True)
    brand = Column(String(64))
    printer_type = Column(ENUM('Ink','Toner'))

class Post(Base):
    __tablename__ = 'example'
    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    body = Column(Text)
        
        

if __name__ == "__main__":
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(bind=engine)