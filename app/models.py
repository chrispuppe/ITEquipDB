from app import db
from sqlalchemy.dialects.mysql import BOOLEAN
import datetime

class Post(db.Model):
    __tablename__ = 'example'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    body = db.Column(db.Text)
 	
    def __init__(self, title, body, id):
        self.title = title
        self.body = body
        self.id = id

class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer,unique=True, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    create_ts = db.Column(db.DateTime)
    skill_level = db.Column(db.Integer)
    email_address = db.Column(db.String(128))
    trade = db.Column(db.String(128))

    def __init__(self, name, skill_level, email_address, trade):
    	self.name = name
    	self.create_ts = datetime.datetime.now()
    	self.skill_level = skill_level
    	self.email_address = email_address
    	self.trade = trade

 #   children = relationship("Device")

class Device(db.Model):
    __tablename__ = 'device'
    id = db.Column(db.Integer, primary_key=True)
    history = db.Column(db.String(255))
    #parent_id = db.Column(db.Integer, ForeignKey('employee.id'))

class Ipads(db.Model):
    __tablename__ = 'ipads'
    serial = db.Column(db.String(128), primary_key=True)
    model = db.Column(db.String(128))
    storage_capacity = db.Column(db.String(128))
    date_purchased = db.Column(db.DateTime)
    #parent_id = db.Column(db.Integer, ForeignKey('device.id'))

class Fob(db.Model):
    __tablename__ = 'fob'
    num = db.Column(db.Integer, unique=True, primary_key=True)
    serial = db.Column(db.String(64), unique=True)

class Computers(db.Model):
    __tablename__ = 'computers'
    computer_id = db.Column(db.Integer, unique=True, primary_key=True)
    computer_name = db.Column(db.String(64))
    brand = db.Column(db.String(64))
    model = db.Column(db.String(64))
    serial = db.Column(db.String(128))
    computer_type = db.Column(db.String(64))
    operating_system = db.Column(db.String(64))
    notes = db.Column(db.String(512))
    retired = db.Column(db.BOOLEAN())
    disposed = db.Column(db.BOOLEAN())
    disposed_date = db.Column(db.Date)
    aquired_date = db.Column(db.Date)
    purchase_price = db.Column(db.Integer)
    vendor_id = db.Column(db.String(64))
    warranty_start = db.Column(db.Date)
    warranty_length = db.Column(db.Integer)
    warranty_end = db.Column(db.Date)
    employee_id = db.Column(db.Integer)
    history = db.Column(db.String(255))

    def __init__(self, computer_name, brand, model, serial, computer_type, 
                operating_system, notes, aquired_date, purchase_price, 
                vendor_id, warranty_start, warranty_length, warranty_end):

        self.computer_name = computer_name
        self.brand = brand
        self.model = model
        self.serial = serial
        self.computer_type = computer_type
        self.operating_system = operating_system
        self.notes = notes
        self.aquired_date = aquired_date
        self.purchase_price = purchase_price
        self.vendor_id = vendor_id
        self.warranty_start = warranty_start
        self.warranty_length = warranty_length
        self.warranty_end = warranty_end
    
class Printers(db.Model):
    __tablename__ = 'printers'
    printer_id = db.Column(db.String(64), unique=True, primary_key=True)
    brand = db.Column(db.String(64))
    model = db.Column(db.String(64))
    printer_type = db.Column(db.String(64))
    aquired_date = db.Column(db.DateTime)
    vendor_id = db.Column(db.String(64))

class Phone_Account(db.Model):
    __tablename__ = 'phone_account'
    phone_number = db.Column(db.String(16), unique=True, primary_key=True)
    phone_model = db.Column(db.String(16))
    phone_os = db.Column(db.String(64))
    notes = db.Column(db.String(255))

class Vendors(db.Model):
    __tablename__ = 'vendors'
    vendor_id = db.Column(db.String(64), unique=True, primary_key=True)
    current_rep = db.Column(db.String(96))
    phone_number = db.Column(db.String(16))
    email_address = db.Column(db.String(128))
    
class Printer_Model(db.Model):
    __tablename__ = 'printer_model'
    printer_model = db.Column(db.String(64), unique=True, primary_key=True)
    brand = db.Column(db.String(64))
    printer_type = db.Column(db.String(64))
