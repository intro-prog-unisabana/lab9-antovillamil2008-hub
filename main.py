from bank_account import BankAccount
from person import Person
from utils import person_data, balance_summary

def main():
    people = []  # List to store all Person objects

    while True:
        # Display menu
        print("Choose an option:")
        print("1. Add a new person")
        print("2. Add an account to a person")
        print("3. Show all balances")
        print("4. Quit")

        choice = input().strip()

        # Option 1: Add a new person
        if choice == "1":
            persona_nueva=person_data()
            people.append(persona_nueva)
            

        # Option 2: Add an account to an existing person
        elif choice == "2":
            nombre_encontrar=input("Enter the person's name:\n")
            encontrado = False
            for person in people:
                if person.name == nombre_encontrar:
                    acc_num = int(input("Enter a 4-digit account number:\n"))
                    init_balance = float(input("Enter the initial balance:\n"))
                    new_account = BankAccount(acc_num, init_balance)
                    person.add_account(new_account)
                    encontrado = True
                    break
            if not encontrado:
                    print("Person not found.")

        # Option 3: Show all balances
        elif choice == "3":
            if not people:
                print("No data to show.")
            else:
                balance_summary(people)

        # Option 4: Quit
        elif choice == "4":
            print("Goodbye!")
            break

        # Invalid input
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()

