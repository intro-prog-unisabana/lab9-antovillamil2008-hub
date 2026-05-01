from person import Person
from bank_account import BankAccount

def person_data():
    name = input("Enter the person's name:\n")
    persona = Person(name)
    
    done = ""
    while done != "yes":
        acc_num = int(input("Enter a 4-digit account number:\n"))
        balance = float(input("Enter the initial balance:\n"))
        
        nueva_cuenta = BankAccount(acc_num, balance)
        persona.add_account(nueva_cuenta)
        
        done = input("Are you done adding accounts? (yes/no):\n")
    
    return persona

def balance_summary(person_list):
    for person in person_list:
        total = sum(acc.balance for acc in person.accounts)
        print(f"{person.name} : {total:.2f}")