from django.contrib.admin import display
from datetime import  datetime

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author =  author
        self.genre = genre
        self.available = True

    def display(self):
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"Genre:{self.genre}")
        print(f"Status:{"Available" if self.available else "Borrowed"} ")
        print("="*30)

book_list =[]

def add_book(title, author, genre):
    book_list.append(Book(title,author,genre))
    print(f"{title} by {author} added successfully!")




def remove_book(title):
    for book in book_list:
        if book.title.lower() == title.lower():
            book_list.remove(book)
            print(f"The {title} is removed")
            return
    print(f"No such book:{title} found! ")




def borrow_book(title):

    for book in book_list:
        if book.title.lower() == title.lower():
            if book.available:
                book.available = False
                print(f"You can  borrow {title}")
            else:
                print(f"{title} is already borrowed ")

            return
    print(f"{title} is not found")



def return_book(title):
    for book in book_list:
        if book.title.lower() == title.lower():
            if not book.available:
                book.available = True
                print(f"Thanks for returning {title}")

            else:
                print(f"{title} was not borrowed")

            return

    print(f"{title} not found")

def search_books(title):
    for book in book_list:
        if book.title.lower() == title.lower():
            book.display()
            return
    print(f"{title} not found")




def display_all():
    if not book_list:

        print("No books are found")
        return
    for book in book_list:
        book.display()
    return


def statistics():
    total_book  = len(book_list)

    count = 0
    borrow = 0
    for book in book_list:
        if book.available:
            count +=1

        else:
            borrow += 1

    genres = []
    for book in book_list:
        genres.append(book.genre.lower())
    most_genres = max(genres, key = genres.count)



    print(f"There are {total_book} books")
    print(f"Total available book are {count}")
    print(f"Total borrowed book are {borrow}")
    print(f"The most genre are {most_genres.capitalize()}")




def save_book(filename = "book.txt"):



    with open(filename, "w") as f:
        for book in book_list:
            f.write(",".join([book.title, book.author, book.genre, str(book.available)]) + "\n")


    now = datetime.now()
    todays_time = now.strftime("%d:%m:%Y at %H:%M:%S")
    print(f"{len(book_list)} is saved at {todays_time}")






def load_book (filename ="book.txt"):
    try:
        new_book_list = []
        with open (filename, "r") as f:

            for l in f:
                line = l.strip()

                parts = line.split(",")
                new_book = Book(parts[0], parts[1], parts[2])
                if parts[3] == "True":
                    new_book.available = True
                else:
                    new_book.available = False
                new_book_list.append(new_book)

    except FileNotFoundError:
        print(f"No book found")
    print(f"Loaded {len(new_book_list)} book!")

    return  new_book_list






def main():
    print("╔══════════════════════════════╗")
    print("║   Library Book Management    ║")
    print("╚══════════════════════════════╝")

    global book_list
    book_list = load_book()
    while True:
        print("\n1.Add a book")
        print("2.Remove a book ")
        print("3.Borrow a book")
        print("4. Return a book")
        print("5.Search books")
        print("6.Display all books")
        print("7.Show statistics")
        print("0.Exit")

        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                name = input("Enter the name of book: ")
                author_name = input("Enter the autor name: ")
                genre = input("Enter what is the genre of book :")

                add_book(name,author_name,genre)

            elif choice == "2":
                name = input("Enter the book name: ")
                remove_book(name)



            elif choice == "3":
                name = input("Enter the name of book: ")
                borrow_book(name)


            elif choice == "4":
                name = input("Enter the name of book: ")
                return_book(name)

            elif choice == "5":
                name = input("Enter the name of book: ")
                search_books(name)

            elif choice == "6":

                display_all()
            elif choice == "7":

                statistics()

            elif choice == "8":
                save_book()



            elif choice == "0":
                save_book()
                print("Good Bye!!")
                break

            else:
                print("Invalid option! Choose 0-8")
        except ValueError:
            print("Enter the valid number...")
if __name__ == "__main__":
    main()




