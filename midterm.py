# Guess the number Game

# import random


# num = random.randint(1,101)
# count = 1
# print("გამოიცანით რიცხვი 1-დან 100-მდე")
# while True:
#     try:
#         guess = int(input(f"რიცხვი (მცდელობა {count}): "))
#         if guess < 0:
#             print("რიცხვები უნდა იყოს მხოლოდ 1-დან 100-მდე!!")
#         else:
#             if guess > num:
#                 print("თქვენი რიცხვი მეტია გამოსაცნობ რიცხვზე!!")
#             elif guess < num:
#                 print("თქვენი რიცხვი ნაკლებია გამოსაცნობ რიცხვზე!!")
#             else:
#                 print("ყოჩაღ! თქვენ გამოიცანით რიცხვი!")
#                 break

 
        
#         count += 1
#     except ValueError:
#         print("შეიყვანეთ რიცხვი!!")

# ბანკომატი

from time import sleep

from time import sleep

balance = 1000

def bank_operations(action):

    global balance

    if action == "ბალანსი":
        return f"თქვენი ბალანსია {balance}"

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
    

print(bank_operations(input("აირჩიეთ ქმედება (ბალანსი, შეტანა, გამოტანა, გამოსვლა): ").lower()))

        
