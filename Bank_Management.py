from random import random
from datetime import datetime
class User:
    def __init__(self,name, email,address,account_type,role="user") -> None:
        self.name=name
        self.email=email
        self.address=address
        self.balance=0
        self.account_no=None
        self.transaction_history=[]
        self.loan_limit=2
        self.total_lone=0
        self.bankrupt=False
        self.loan_status="on"
        self.account_type=account_type
        self.role=role
    def generate_account(self):
        self.account_no=f"{self.email}_{int(random()*100)}"
        print()
        print(f"--> account create successful and account No : {self.account_no}")
        print()
    def check_balance(self):
        print("#----------------------#")
        print(f"Your total balance : {self.balance} Tk")
        print("#----------------------#")
    
    def deposit(self,amount):
        if(amount>0):
            self.balance+=amount
            print("#----------------------#")
            print(f"Deposit amount : {amount} Tk")
            print("#----------------------#")
            tnx_h=f"Deposit amount :{amount} time:{datetime.now()}"
            self.transaction_history.append(tnx_h)
        else:
            print("#----------------------#")
            print(f"Invalid deposit amount")
            print("#----------------------#")

    def withdraw(self, amount):
        if amount >= 0 and amount <= self.balance:
            self.balance -= amount
            tnx_h=f"withdraw amount :{amount} time:{datetime.now()}"
            self.transaction_history.append(tnx_h)
            print("#----------------------#")
            print(f"Withdrew {amount}. New balance: {self.balance}")
            print("#----------------------#")
        else:
            print("#----------------------#")
            print("Withdrawal amount exceeded")
            print("#----------------------#")

    def take_loan(self,amount):
        if self.loan_limit>0:
            self.balance+=amount
            self.loan_limit-=1
            self.total_lone +=amount
            tnx_h=f"take loan amount :{amount} time:{datetime.now()}"
            self.transaction_history.append(tnx_h)
            print("#----------------------#")
            print(f"Loan ${amount}. New balance: ${self.balance}")
            print("#----------------------#")
        else:
            print("#----------------------#")
            print(f"Loan limit cross")
            print("#----------------------#")

    def transaction_history_f(self):
        print("#----------------------#")
        print(f"Name {self.name} account No : {self.account_no}")
        if len(self.transaction_history)>0:
            for history in self.transaction_history:
                print(history)
        else:
            print("transaction history not available")
        print("#----------------------#")


class SavingAccount(User):
    def __init__(self, name, email, address, account_type,interestRate) -> None:
        super().__init__(name, email, address, account_type)
        self.interestRate = interestRate
        def apply_interest(self):
            interest = self.balance*(self.interestRate/100)
            print("\n--> Interest is applied !")
            self.deposit(interest)

class CurrentAccount(User):
    def __init__(self, name, email, address, account_type) -> None:
        super().__init__(name, email, address, account_type)

    # hire currentAccount some method


class Bank:
    def __init__(self,name) -> None:
        self.name=name
        self.account_list=[]

    def create_account(self,name, email,address,account_type,role="user",interestRate="op"):
        account=None
        if account_type=="saving account":
            account=SavingAccount(name,email,address,account_type,interestRate)
            account.generate_account()
        elif account_type=="current account":
            account=CurrentAccount(name, email,address,account_type,role)
            account.generate_account()
        # for admin
        else:
            account=User(name, email,address,account_type,role)
            print(email,name)
            account.account_no=f"{email}_123"
            print(account.account_no)
        self.account_list.append(account)
        return account
    
    def delete_account(self,account_no):
        for account in self.account_list:
            if account_no in account.account_no:
                self.account_list.remove(account)
                print(f"Delete account successful")
                break
    def show_users(self):
        print("#----------------------#")
        if len(self.account_list)>0:
            for account in self.account_list:
                print(f"User name:{account.name}, account no: {account.balance}, account No {account.account_no}")
        else:
            print("User not available")
        print("#----------------------#")
    def show_balance(self,account_no):
         for account in self.account_list:
            if account_no == account.account_no:
                print(f"This user Balance : {account.balance}")
                break

    def total_lone(self,account_no):
        for account in self.account_list:
            if account_no == account.account_no:
                print(f"total loan are: {account.total_loan}")
                break

    def control_lone(self,account_no):
        a=False
        for account in self.account_list:
            if account_no == account.account_no:
                a=True
                if account.loan_status=="on":
                    account.loan_status="off"
                    print(f"user nae:{account.name} lone status {account.loan_status}")
                else:
                    account.loan_status="on"
                    print(f"user nae:{account.name} lone status {account.loan_status}")
                break
        if a==False:
            print("account is not found")



    def transfer_balance(self,from_account,to_account_no,amount):
        to_account=None
        for account in self.account_list:
            if to_account_no == account.account_no:
                to_account=account

        if to_account is not None:
            if from_account.balance>=amount and amount>0:
                from_account.balance -=amount
                to_account.balance+=amount
                print(f"Balance Transfer amount{amount} successful")
                tnx_h1=f"transfer amount :{amount} time:{datetime.now()}"
                from_account.transaction_history.append(tnx_h1)
                tnx_h2=f"transfer amount :{amount} time:{datetime.now()}"
                to_account.transaction_history.append(tnx_h2)
            else:
                print("Invalid amount")

        else: 
            print(f"{to_account_no} Account does not exist")



abc_bank=Bank("Abc Bank")
admin=abc_bank.create_account("Fahim Al Imran","fahim@gaiml.com","Dahka","admin","admin")

###########################################
#                                         #
#  admin account no: fahim@gaiml.com_123  #
#                                         #
###########################################

current_user=None

while True:
    if current_user==None:
        print("\n--> No user logged in !")
        ch=input("\n--> Register/Login (R/L) : ")
        if ch=="R":
            name=input("Name:")
            email=input("email:")
            address=input("address:")
            a=input("Savings Account or Current Account (sa/ca) :")
            if a=="sa":
                ir=int(input("Interest rate:"))
                current_user=abc_bank.create_account(name,email,address,"saving account","user",ir)
            else:
                current_user=abc_bank.create_account(name,email,address,"current account","user")
        elif ch=="L":
            no=input("Account Number:")
            for account in abc_bank.account_list:
                if no == account.account_no:
                    current_user=account
                    break
    else:
        if current_user.role=="user":
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Take Lone")
            print("5. Transfer Balance")
            print("6. Transaction History")
            print("7. Logout")
            
            op=int(input("Enter Option:"))
            if op==1:
                current_user.check_balance()
            elif op==2:
                amount=int(input("Enter amount "))
                current_user.deposit(amount)
            elif op==3:
                if current_user.bankrupt ==False:
                    amount=int(input("Enter withdraw amount "))
                    current_user.withdraw(amount)
                else:
                    print("This user are bankrupt")
            elif op==4:
                if current_user.loan_status=="on":
                    amount=int(input("Enter loan amount "))
                    current_user.take_loan(amount)
                else:
                    print("You can not take Lone")
            elif op==5:
                if current_user.bankrupt ==False:
                    account_no=input("Enter Account No :")
                    amount=int(input("Enter transfer amount:"))
                    abc_bank.transfer_balance(current_user,account_no,amount)
                else:
                   print("You can not take Lone")

            elif op==6:
                current_user.transaction_history_f()
            elif op==7:
                current_user=None

        elif current_user.role=="admin":
            print("1. Create Account")
            print("2. Delete Account")
            print("3. Show Account")
            print("4. Show a User Balance")
            print("5. Show a User Total lone")
            print("6. One of a User lone")
            print("7. Logout")

            op=int(input("Enter Option:"))
            if op==1:
                name=input("Name:")
                email=input("email:")
                address=input("address:")
                a=input("Savings Account or Current Account (sa/ca) :")
                if a=="sa":
                    ir=int(input("Interest rate:"))
                    abc_bank.create_account(name,email,address,"saving account","user",ir)
                else:
                    current_user=abc_bank.create_account(name,email,address,"current account","user")
            elif op==2:
                account_no=input("Enter account No :")
                abc_bank.delete_account(account_no)
            elif op==3:
                abc_bank.show_users()
            elif op==4:
                account_no=input("Enter account No :")
                abc_bank.show_balance(account_no)
            elif op==5:
                account_no=input("Enter account No :")
                abc_bank.total_lone(account_no)
            elif op==6:
                account_no=input("Enter account No :")
                abc_bank.control_lone(account_no)
            elif op==7:
                current_user=None


