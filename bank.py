# ბანკომატი

from time import sleep

balance = 1000

def bank_operations(action):

    global balance

    if action == "ბალანსი":
        return f"თქვენი ბალანსია: {balance}"

    elif action == "გატანა":
        try:
            amount = int(input("რამდენის გამოტანა გსურთ?: "))
            if amount > balance:
                return "არ გაქვთ საკმარისი თანხა"
            balance -= amount
            return f"ახალი ბალანსია: {balance}"
        except ValueError:
            return "არასწორი შეყვანის ტიპი !"

    elif action == "შეტანა":
        try:
            amount = int(input("რამდენის შეტანა გსურთ?: "))
            if amount <= 0:
                return "უარყოფითი რიცხვის შეტანა შეუძლებელია!"
            balance += amount
            return f"ახალი ბალანსი: {balance}"
        except ValueError:
            return "არასწორი შეყვანის ტიპი!"
    elif action == "გამოსვლა":
        sleep(1)
        return "გამოსვლა..."

    else:
        return "ესეთი ქმედება არ არსებობს! სცადეთ ხელახლა"
    

print(bank_operations(input("აირჩიეთ ქმედება (ბალანსი, შეტანა, გატანა, გამოსვლა): ").lower()))