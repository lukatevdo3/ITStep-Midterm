# Guess the number Game

import random


num = random.randint(1,101)
count = 1
print("გამოიცანით რიცხვი 1-დან 100-მდე")
while True:
    try:
        guess = int(input(f"რიცხვი (მცდელობა {count}): "))
        if guess < 0:
            print("რიცხვები უნდა იყოს მხოლოდ 1-დან 100-მდე!!")
        else:
            if guess > num:
                print("თქვენი რიცხვი მეტია გამოსაცნობ რიცხვზე!!")
            elif guess < num:
                print("თქვენი რიცხვი ნაკლებია გამოსაცნობ რიცხვზე!!")
            else:
                print("ყოჩაღ! თქვენ გამოიცანით რიცხვი!")
                break

 
        
        count += 1
    except ValueError:
        print("შეიყვანეთ რიცხვი!!")

# ბანკომატი