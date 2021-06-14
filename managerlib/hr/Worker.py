import csv
import pandas as pd
from datetime import datetime as dt

# from accounting import debit, credit, get_account_no


class Worker:
    def __init__(self, name):
        self.name = name

        self.check_database()
        self.check_attendance()
        self.check_balance()

    def check_database(self):
        """Check the database to find the Worker details and
            update the status of Worker object"""
            
        w_data = pd.read_csv("worker_data.csv", index_col="NAME")
        try:
            self.id = w_data.loc[self.name, "ID"]
            self.have_id = True
            self.details = w_data.loc[self.name, :]
            print(self.details)
        except:
            self.have_id = False

    def refresh_data(self):
        self.check_database()
        self.check_attendance()
        self.check_balance()
    
    def update_details(self, detail, new_value):
        """Update details of a Worker"
        
        Parameters
        ------------
        detail: str, list of str
            Name, Age, Address, Mobile_no, Pay_rate, Group
        new_value: str, list of str
            new value of the detail
        """
        
        if type(detail)!= list:
            detail=[detail]
            new_value=[new_value]
            print("Details Updated :\n", detail)
            
        w_data = pd.read_csv("worker_data.csv", index_col="ID")
        w_data.at[self.id, detail+["LAST_MODIFIED"]] = new_value + [dt.now()]
        w_data.to_csv("worker_data.csv")
        self.check_database()
        
        
    def update_pay_rate(self, new_rate):
        w_data = pd.read_csv("worker_data.csv", index_col="ID")
        w_data.at[self.id, ["PAY_RATE", "LAST_MODIFIED"]] = [new_rate, dt.now()]
        w_data.to_csv("worker_data.csv")
        self.check_database()

    def check_attendance(self):
        pass

    def check_balance(self):
        pass

    def update_attendance(self):
        pass

    # with open("attendance_sheet.csv") as a_data:


class AddWorker:
    """Add new workers to database
    group : Permanent/ Temporary"""

    def __init__(
        self, name, age, address, mobile_no, join_date, pay_r, group="Temporary"
    ):
        print("Adding new Worker....")
        self.name = name

        self.id = self.generate_id(name, group, id_type="W")
        self.add_entry(name, age, address, mobile_no, join_date, pay_r, group)
        

    def generate_id(self, name, group, id_type="X"):
        initials = name.split()
        ts = dt.now().strftime("%y%m%S")
        id_no = id_type + group[0] + initials[0][0] + initials[1][0] + ts
        return id_no

    def add_entry(self, name, age, address, mobile_no, join_date, pay_r, group):
        with open("worker_data.csv", "a") as c_data:
            c_data.write(
                f"\n{self.id},{name},{age},{address},{mobile_no},{join_date},{pay_r},{group},{dt.now()}"
            )


worker_name = "Gurupada Pandit"
worker1 = Worker(worker_name)

if not worker1.have_id:
    address = "kamarpukur"  # str(input("Enter Address.. : "))
    age = 46
    mobile_no = "7908795631"  # str(input("Mobile No. : "))
    join_date = "20/03/2012"
    pay_r = 350.0
    group = "Owner"  # str(input("Worker Group :"))
    AddWorker(worker_name, age, address, mobile_no, join_date, pay_r, group=group)
    Worker(worker_name).check_database()


worker1.update_details(["MOBILE_NO", "ADDRESS"], ["756024831", "Kamarpukur"])
"""
worker1.update_pay_rate(256)
worker1.update_address("Kamarpukur")
worker1.update_mobile_no("7905646223")
"""
