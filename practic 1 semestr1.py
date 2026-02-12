class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "доступна"

class User:
    def __init__(self, name):
        self.name = name
        self.books = []

class Library:
    def __init__(self):
        self.books = []
        self.users = []
    
    # библиотекарь 
    def add_book(self):
        title = input("Название: ")
        author = input("Автор: ")
        self.books.append(Book(title, author))
        print("Добавлено")
    
    def delete_book(self):
        title = input("Название для удаления: ")
        for book in self.books:
            if book.title == title:
                if book.status == "выдана":
                    print("Нельзя удалить, тк книга выдана")
                else:
                    self.books.remove(book)
                    print(" Удалено")
                return
        print("Не найдено")
    
    def reg_user(self):
        name = input("Имя пользователя: ")
        for user in self.users:
            if user.name == name:
                print("Такое имя уже есть ")
                return
        self.users.append(User(name))
        print("Пользователь зарегистрирован")
    
    def show_users(self):
        if self.users == []:
            print("Нет пользователей")
            return
        print("Пользователи:")
        for u in self.users:
            print("-", u.name)
            
    def show_books(self):
        if not self.books:
            print("Нет книг")
            return
        print("Книги:")
        for b in self.books:
            print(f"- {b.title} ({b.author}) — {b.status}")
    
    # пользователи
    def show_available(self):
        print("Доступные:")
        found = False
        for b in self.books:
            if b.status == "доступна":
                print(f"- {b.title}")
                found = True
        if not found:
            print("Нет свободных книг")
    
    def take_book(self):
        name = input("Ваше имя: ")
        user = None
        for u in self.users:
            if u.name == name:
                user = u
                break
        if not user:
            print("Сначала зарегистрируйтесь у библиотекаря")
            return
        
        title = input("Какую книгу взять: ")
        for b in self.books:
            if b.title == title:
                if b.status == "доступна":
                    b.status = "выдана"
                    user.books.append(title)
                    print("Взял")
                else:
                    print("Уже выдана")
                return
        print("Нет такой книги")

# меню
 
lib = Library()

print("Библиотека")
print("Выберите вашу роль")
print("1 - Библиотекарь")
print("2 - Пользователь")
print("3 - Выход")
role = int(input("Введите число "))

while role != 3:

    if role == 1:
        print("БИБЛИОТЕКАРЬ — ВЫБЕРИТЕ ДЕЙСТВИЕ")
        print("1 — Добавить книгу")
        print("2 — Удалить книгу")
        print("3 — Зарегистрировать пользователя")
        print("4 — Показать пользователей")
        print("5 — Показать книги")
        choice = input("→ ")
        
        if choice == "1":
            lib.add_book()
        elif choice == "2":
            lib.del_book()
        elif choice == "3":
            lib.reg_user()
        elif choice == "4":
            lib.show_users()
        elif choice == "5":
            lib.show_books()
        else:
            print("Неверный выбор")

    elif role == 2:
        print("\n ПОЛЬЗОВАТЕЛЬ — ВЫБЕРИТЕ ДЕЙСТВИЕ")
        print("1 — Доступные книги")
        print("2 — Взять книгу")
        choice = input("→ ")
        
        if choice == "1":
            lib.show_available()
        elif choice == "2":
            lib.take_book()
        else:
            print("Неверный выбор")

    elif role == 3:
        print("Неверный выбор")

    print("\nПрограмма завершена. Для повтора запустите снова.")