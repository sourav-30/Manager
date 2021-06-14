import sqlite3
import csv
import pandas as pd
from datetime import datetime as dt
#from accounting import debit, credit, get_account_no


class Customer():
    """Check customer in database"""

    def __init__(self, name):
        self.name = name
        
        self.check_status()
            
    def check_status(self):
        with open("customer_data.csv") as c_data_file:
            customer_data = csv.DictReader(c_data_file,)
            self.have_id = False
            for customer in customer_data:
                if customer["Name"] == self.name:
                    self.have_id = True
                    self.id = customer["ID"]
                    print("Customer in database with ID = ",self.id)
                    self.details = customer 
                    print("Details --\n", customer)
                

class AddCustomer():
    """Add new customers to database
        group : Individual/ Association/ Business/ Government"""
    
    def __init__(self, name, address, mobile_no, group='Individual'):
        print("Adding new Customer....")
        self.name = name
        
        self.id = self.generate_id(name, group, id_type = "C")
        self.add_entry(name, address, mobile_no, group)
        
        
    def generate_id(self, name, group, id_type = "O"):
         initials = name.split()
         ts = dt.now().strftime("%y%m%d%H%S")
         id_no = id_type+group[0]+initials[0][0]+initials[1][0]+ts
         return id_no
    
    def add_entry(self, name, address, mobile_no, group):
        with open("customer_data.csv","a") as c_data:
            c_data.write(f"\n{self.id},{name},{address},{mobile_no},{group}")
        




cstmr_name = "Somnath Pandit"
cstmr1 = Customer(cstmr_name)
if not cstmr1.have_id:
    address = "kamarpukur"#str(input("Enter Address.. : "))
    mobile_no = "7908784952"#str(input("Mobile No. : "))
    group = "Individual"#str(input("Customer Group :"))
    AddCustomer(cstmr_name, address, mobile_no, group=group)


         
        
