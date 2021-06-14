import uuid
import pandas as pd
from datetime import datetime as dt

TIMESTAMP = dt.now()


class Transaction:
    def deposit(self, amount, payee, remarks="Credited in treasury"):
        trans_details = {
            "DATE": TIMESTAMP,
            "TRANSACTION_ID": self.transaction_id(),
            "REMARKS": remarks,
            "DEBITED": 0.00,
            "CREDITED": amount,
            "CR_BALANCE": self.treasure_money + amount,
        }
        trans_data = pd.DataFrame.from_dict(trans_details)
        print(trans_data)
        trans_data.to_csv("Treasury.csv", mode="a", header=False, index=False)
        self.check_vault_status()

    def withdrawl(self, amount, debiter, remarks="Debited from treasury"):
        trans_details = {
            "DATE": TIMESTAMP,
            "TRANSACTION_ID": self.transaction_id(),
            "REMARKS": remarks,
            "DEBITED": amount,
            "CREDITED": 0.00,
            "CR_BALANCE": self.treasure_money - amount,
        }
        trans_data = pd.DataFrame.from_dict(trans_details)
        print(trans_data)
        trans_data.to_csv("Treasury.csv", mode="a", header=False, index=False)
        self.check_vault_status()

    def transaction_id(self):
        transaction_id = uuid.uuid4().hex
        return transaction_id


class Bank:
    def __init__(self):
        pass
        
    #def chart_of_accounts(self):
    #    accounts = pd.read_csv("chart_of_accounts.csv")
    
    def update_account_chart(self,acc_no, detalis):
    #TODO
        pass
        acc_details = {
            "ACCOUNT_NO":self.acc_no,
            "NAME":name,
            "ADDRESS":address,
            "MOBILE_NO":mobile_no,
            "CR_BALANCE":first_deposit,
            "LAST_UPDATED":TIMESTAMP,
            "OPENING_DATE":TIMESTAMP,
        }
        acc_data = pd.DataFrame.from_dict(acc_details)
        print(acc_data)
        acc_data.to_csv("chart_of_accounts.csv", mode="a", header=False, index=False)


class Treasury(Transaction):
    def __init__(self): 
        self.acc_no = 3000001
        self.check_vault_status()

    def check_vault_status(self):
        vault = pd.read_csv("Treasury.csv")
        self.treasure_money = vault.tail(1)["CR_BALANCE"]
        print(self.treasure_money)
        self.last_10_transaction = vault.tail(10)


class CreateAccount:
    def __init__(self, name, address, mobile_no, first_deposit=0.0):
        acc_chart = pd.read_csv("chart_of_accounts.csv")
        if not acc_chart.isin([name, mobile_no]).any().any():
            self.get_acc_no()
            acc_details = {
                "ACCOUNT_NO":self.acc_no,
                "NAME":name,
                "ADDRESS":address,
                "MOBILE_NO":mobile_no,
                "CR_BALANCE":first_deposit,
                "LAST_UPDATED":TIMESTAMP,
                "OPENING_DATE":TIMESTAMP,
            }
            acc_data = pd.DataFrame.from_dict([acc_details])
            print(acc_data)
            acc_data.to_csv("chart_of_accounts.csv", mode="a", header=False, index=False)
        else:
            print("Account already exist.")
            if any(acc_chart["NAME"]==name):
                print(acc_chart[acc_chart["NAME"]==name]) 
            if any(acc_chart["MOBILE_NO"]==mobile_no):
                print(acc_chart[acc_chart["MOBILE_NO"]==mobile_no])
                
    def get_acc_no(self):
        last_acc_no = pd.read_csv("chart_of_accounts.csv")["ACCOUNT_NO"].max()
        self.acc_no=last_acc_no+1
        

class Account(Transaction):
    def __init__(self, acc_no):
        self.acc_no = acc_no

    def cr_balance():
        pass

    def view_statement():
        pass

    def generate_passbook():
        pass


ca = CreateAccount("Somnath Pandit", "Kamarpukur", 302112564)
