class BankAccount():
    def __init__(self, balance, username, password, minimum_balance=0):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False
        self.minimum_balance = minimum_balance
        
        
    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            # print(self.authenticated)
        
    def deposit(self, amount):
        if self.authenticated == True:
            if amount > 0:
                self.balance += amount
                print("Le dépôt a été effectuée, votre nouvreau solde est:",self.balance,"francs")
            
            else:
                print("La somme n'est pas valide")
        else:
            print("Veuillez vous authentifier d'abord")    
                   
    def withdraw(self, amount):
        if self.authenticated == True:
            if amount > 0:
                self.balance -= amount
                print("Le retrait a été effectuée, votre nouveau solde est:",self.balance,"francs")

            else:
                print("La somme n'est pas valide")
        else:
            print("Veuillez vous authentifier d'abord")     
            
            
class  MinimumBalanceAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance > self.minimum_balance and self.balance > amount:
            self.balance -= amount
            print("Le retrait a été effectuée, votre nouveau solde est:",self.balance,"francs")

        else:
            print("Retrait Impossible")


class DAB:
    def __init__(self, account_list, try_limit):
        self.account_list = account_list
        self.try_limit = try_limit

        for account in account_list:
            if not isinstance(account, (BankAccount, MinimumBalanceAccount)):
                raise TypeError("account_list doit contenir une liste de BankAccount ou MinimumBalanceAccount instances.")
        self.account_list = account_list
        
        try:
            self.try_limit = int(try_limit)
            if self.try_limit <= 0:
                raise ValueError("try_limit doit être un nombre positif.")
        except ValueError:
            print("Entrée invalide pour try_limit, la valeur par défaut 2 sera utilisée.")
            self.try_limit = 2
