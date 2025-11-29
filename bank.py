# ბანკომატი
import os
from time import sleep

file = "atm_balance.txt"


if not os.path.exists(file):
    '''
    ამოწმებს არსებობს თუ არა ესეთი ფაილი რათა მომხმარებელს აღარ შეამნევინოს ზედმეტი
    და არ დაახარჯინოს მეხსიერება. შეაყვანინებს მომხმარებელს თავის სასურველ ბალანსს.
    '''
    while True:
        try:
            balance = float(input("შეიყვანე საწყისი ბალანსი:  "))
            if balance < 0:
                print("ბალანსი შეუძლებელია იყოს უარყოფითი!!")
                continue
            break
        except ValueError:
            print("შეიყვანეთ რიცხვი!!")
    with open(file, "w", encoding = 'utf-8') as f:
        f.write(str(balance))


def get_balance():
    '''
    კიტხულობს ბალანსს ტექსტური ფაილიდან
    '''
    with open(file, "r", encoding = 'utf-8') as f:
        return float(f.read().strip())


def withdraw(amount):
    '''
    მომხმარებელს გამოაქვს თანხა იმ შემთხვევაში თუ ბალანსზე არსებობს 
    საკმარისი თანხა
    '''
    balance = get_balance()
    if amount > balance:
        print("არასაკმარისი ბალანსი")
        return
    balance -= amount
    with open(file, "w", encoding = 'utf-8') as f:
        f.write(str(balance))
    print(f"თანხის გატანა წარმატებით შესრულდა! ახალი ბალანსია: {balance}")


def deposit(amount):
    '''
    მომხმარებელს შეაქვს ნებისმიერი თანხა და ეს თანხა იწერება ტექსტურ ფაილში
    '''
    balance = get_balance()
    balance += amount
    with open(file, "w", encoding = 'utf-8') as f:
        f.write(str(balance))
    print(f"თანხის შეტანა წარმატებით შესრულდა! ახალი ბალანსია: {balance}")

# მენიუ
def atm():

    '''
    ეს არის interface სადაც მომხმარებელს აქვს შესაძლებლობა გამოიყენოს 
    ბანკომატი თავისი სურვილისამებრ. გააჩნია ვალიდაციები, რომლებიც ხელს უწყობს
    მომხმარებელს, რომ სწორი ინფორმაცია შეიყვანოს
    '''
    while True:
        print("\n--- ATM ---")
        print("1. ბალანსი")
        print("2. თანხის გატანა")
        print("3. თანხის შეტანა")
        print("4. Exit")
        choice = input("აირჩიე: ")

        if choice == "1":
            print(f"\nშენი ბალანსია: {get_balance()}")
        elif choice == "2":
            try:
                amount = float(input("\nშეიყვანე გასატანი თანხა: "))
                if amount <= 0:
                    print("შეიყვანე დადებითი რიცხვი!")
                    continue
                withdraw(amount)
            except ValueError:
                print("თანხა უნდა იყოს რიცხვი!!")
        elif choice == "3":
            try:
                amount = float(input("\nშეიყვანე შესატანი თანხა: "))
                if amount <= 0:
                    print("შეიყვანე დადებითი რიცხვი!")
                    continue
                deposit(amount)
            except ValueError:
                print("თანხა უნდა იყოს რიცხვი!!")
        elif choice == "4":
            sleep(1)
            print("\nგამოსვლა...")
            sleep(1)
            break
        else:
            print("არჩევანი არასწორია! ხელახლა სცადეთ")

atm()

