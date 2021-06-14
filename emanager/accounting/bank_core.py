import os
import uuid
from constants import*
import pandas as pd

acc_path = os.path.dirname(os.path.realpath(__file__))

class Transaction:
    #TODO
    """acts as a mediator between two parties and returns them transaction details so that they can update their accounts"""
    
    def __init__(self):
        print(super().__name__)
        
    def deposit(self, amount, payer, remarks="Self Deposit"):
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
        trans_data.to_csv(f"{acc_path}/treasury.csv", mode="a", header=False, index=False)
        self.check_vault_status()

    def withdrawl(self, amount, benifactor, remarks="Self Withdrawl"):
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
        trans_data.to_csv(f"{acc_path}/treasury.csv", mode="a", header=False, index=False)
        self.check_vault_status()

    def transaction_id(self):
        """Generate transaction id"""
        
        transaction_id = uuid.uuid4().hex
        return transaction_id

class AccountCaller:
    pass

class Ledger:
    pass
       
class Bank(Transaction, AccountCaller, Ledger):
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
        acc_data.to_csv(f"{acc_path}/chart_of_accounts.csv", mode="a", header=False, index=False)


class Treasury(Transaction):
    def __init__(self): 
        self.acc_no = 3000001
        self.check_vault_status()

    def check_vault_status(self):
        vault = pd.read_csv(f"{acc_path}/treasury.csv")
        self.treasure_money = vault.tail(1)["CR_BALANCE"]
        print(self.treasure_money)
        self.last_10_transaction = vault.tail(10)


class CreateAccount:
    def __init__(self, name, address, mobile_no, first_deposit=0.0):
        acc_chart = pd.read_csv(f"{acc_path}/chart_of_accounts.csv")
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
            acc_data.to_csv(f"{acc_path}/chart_of_accounts.csv", mode="a", header=False, index=False)
        else:
            print("Account already exist.")
            if any(acc_chart["NAME"]==name):
                print(acc_chart[acc_chart["NAME"]==name])
            elif any(acc_chart["MOBILE_NO"]==mobile_no):
                print(acc_chart[acc_chart["MOBILE_NO"]==mobile_no])
                
    def get_acc_no(self):
        last_acc_no = pd.read_csv(f"{acc_path}/chart_of_accounts.csv")["ACCOUNT_NO"].max()
        self.acc_no=last_acc_no+1
        

class Account(Transaction):
    def __init__(self, acc_no):
        self.acc_no = acc_no

    def cr_balance():
        pass

    def view_statement(last_transactions=10):
        pass

    def generate_passbook():
        pass


