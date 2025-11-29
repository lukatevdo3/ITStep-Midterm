import json
from time import sleep

class Book:

    def __init__(self, title : str, author : str, date : int):
        '''
        ეს არის წიგნის კლასი სადაც ვქმნით წიგნის ობიექტს სახელით, ავტორით და გამოშვების თარიღით
        '''
        self._title = title
        self._author = author
        self._date = date



class BookManager:

    def __init__(self, file = "library.json"):
        '''
        ეს არის ერთგვარი ბიბლიოთეკა, რომელშიც ასახულია 4 მეთოდი, წიგნის დამატება, მისი შენახვა
        json ფაილში, ყველა წიგნის ნახვა, და წიგნის ძებნა სათაურის მიხედვით. მთავარი მეთოდი კი არის 
        სტატიკური მეთოდი, რომელიც არის კლასის ნაწილი და ასრულებს interface ფუნქციებს რათა კლასი გახდეს
        მომხმარებლზე მორგებული. ინტერფეისში და კლასში დაცულია შესაბამისი ვალიდაციები. 

        '''
        self.__shelf = []
        self.file = file

    def add_book(self, book):
        book1 = {"Author" : book._author, "Title" : book._title, "Date" : book._date}
        self.__shelf.append(book1)
        self.save_book()
        print(f"\nწიგნი \"{book._title}\" დაემატა ბიბლიოთეკაში\n")

    def save_book(self):
        with open(self.file, 'w', encoding = 'utf') as f:
            json.dump(self.__shelf, f, indent = 2)

    def show_books(self):
        count = 0
        if self.__shelf == []:
            print("\nწიგნები არ არის დამატებული ბიბლიოთეკაში!\n")
        else:
            print("\n--- თქვენი წიგნებია ---\n")
            for book in self.__shelf:
                count += 1
                print(f"{count}. წიგნი - {book["Title"]}, ავტორი - {book["Author"]}, გამოშვების თარიღი - {book["Date"]}")
            
            print("\n")
    
    def find_book(self, title):
        count = 0
        books = [book for book in self.__shelf if title.lower() in book["Title"].lower()]
        if self.__shelf == []:
            print("\nწიგნები არ არის დამატებული ბიბლიოთეკაში!\n")
        else:
            for book in books:
                count += 1
                print(f"\n{count}. წიგნი - {book["Title"]}, ავტორი - {book["Author"]}, გამოშვების თარიღი - {book["Date"]}")
    
            print(f"\nთქვენი სასურველი წიგნების რაოდენობაა {count}\n")    

    @staticmethod
    def interface():
        manager = BookManager()
        while True:
            print("--- ბიბლიოთეკა ---")
            print("1. წიგნის დამატება")
            print("2. წიგნების ნახვა")
            print("3. წიგნის ძებნა")
            print("4. გამოსვლა")

            choice = input("აირჩიე: ")
            if choice.strip() == "1":
                try:
                    title = input("შეიყვანეთ წიგნის სახელი: ").title()
                    if title == "":
                        print("\n--- წიგნს უნდა გააჩნდეს სახელი! ---\n")
                        continue
                    author = input("შეიყვანეთ ავტორის სახელი: ").title()
                    if not author.replace(" ", "").isalpha(): # ამოწმებს არის თუ არა ავტორის სახელში ყველა ასო
                        print("\n--- ავტორის სახელი უნდა შედგებოდეს ასოებისგან! ---\n") 
                        continue              
                    date = int(input("შეიყვანეთ თარიღი: "))
                    if date > 2025:
                        print("\n--- არასწორი თარიღი! სცადეთ ხელახლა! ---\n")
                        continue

                    book1 = Book(title, author, date)
                    manager.add_book(book1)
                    continue
                except ValueError:
                    print("\n--- არასწორი პარამეტრები! სცადეთ ხელახლა ---\n")
            elif choice.strip() == "2":
                manager.show_books()
            elif choice.strip() == "3":
                title_search = input("\nშეიყვანეთ წიგნის დასახელება: ")
                manager.find_book(title_search)
            elif choice.strip() == "4":
                sleep(1)
                print("\nმადლობა მოხმარებისთვის!")
                sleep(0.75)
                print("ბიბლიოთეკა იხურება!")  
                sleep(1)
                break
            else:
                print("\n--- თქვენი არჩევანი არ არსებობს! სცადეთ ხელახლა! ---\n")
                continue

                

manager = BookManager()
manager.interface()


    