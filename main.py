from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime, timedelta
import json
import os

class DatabaseManager:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string, server_api=ServerApi('1'))
        self.database = self.client[database_name]
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(f"Connection failed: {e}")

    def get_current_borrowings(self):
        borrowing_collection = self.database['Borrowing']
        current_borrowings = borrowing_collection.find({"ReturnDate": None})
        return list(current_borrowings)

    # -------------------- BOOKS --------------------
    def add_book(self, title, authors, categories, published_year, average_rating, num_pages):
        books_collection = self.database['Books']
        last_book = books_collection.find_one(sort=[("ID", -1)])
        last_id = last_book["ID"] if last_book else 0
        new_book = {
            "ID": last_id + 1,
            "title": title,
            "authors": authors,
            "categories": categories,
            "published_year": published_year,
            "average_rating": average_rating,
            "num_pages": num_pages
        }
        books_collection.insert_one(new_book)
        print(f"Book '{title}' added successfully!")

    def display_books(self):
        books_collection = self.database['Books']
        books = books_collection.find()
        print("\nBooks Collection:")
        for book in books:
            print(
                f"ID: {book['ID']}, "
                f"title: {book['title']}, "
                f"authors: {book['authors']}, "
                f"categories: {book['categories']}, "
                f"published_year: {book['published_year']}, "
                f"average_rating: {book['average_rating']}, "
                f"num_pages: {book['num_pages']}"
            )

    def display_last_10_books(self):
        books_collection = self.database['Books']
        books = books_collection.find().sort("ID", -1).limit(10)
        print("\nLast 10 Books:")
        for book in books:
            print(
                f"ID: {book['ID']}, "
                f"title: {book['title']}, "
                f"authors: {book['authors']}, "
                f"categories: {book['categories']}, "
                f"published_year: {book['published_year']}, "
                f"average_rating: {book['average_rating']}, "
                f"num_pages: {book['num_pages']}"
            )

    def update_book(self,
                    book_id,
                    new_title=None,
                    new_authors=None,
                    new_categories=None,
                    new_published_year=None,
                    new_average_rating=None,
                    new_num_pages=None):
        books_collection = self.database['Books']
        update_fields = {
            "title": new_title,
            "authors": new_authors,
            "categories": new_categories,
            "published_year": new_published_year,
            "average_rating": new_average_rating,
            "num_pages": new_num_pages
        }
        update_fields = {k: v for k, v in update_fields.items() if v is not None}

        if update_fields:
            books_collection.update_one({"ID": book_id}, {"$set": update_fields})
            print(f"Book with ID={book_id} was updated.")
        else:
            print("No fields to update.")

    def delete_book(self, book_id):
        books_collection = self.database['Books']
        result = books_collection.delete_one({"ID": book_id})
        if result.deleted_count == 1:
            print(f"Book with ID={book_id} deleted.")
        else:
            print(f"No book found with ID={book_id}.")

    # -------------------- READERS --------------------
    def add_reader(self, first_name, last_name, email, gender, birth_year):
        """
        Dodaj nowego czytelnika z polami:
        library_card_id, first_name, last_name, email, gender, birth_year
        """
        readers_collection = self.database['Readers']
        # Znajdujemy najwyższy istniejący library_card_id:
        last_reader = readers_collection.find_one(sort=[("library_card_id", -1)])
        last_card_id = last_reader["library_card_id"] if last_reader else 0

        new_reader = {
            "library_card_id": last_card_id + 1,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "gender": gender,
            "birth_year": birth_year
        }
        readers_collection.insert_one(new_reader)
        print(f"Reader '{first_name} {last_name}' added successfully!")

    def display_readers(self):
        readers_collection = self.database['Readers']
        readers = readers_collection.find()
        print("\nReaders Collection:")
        for reader in readers:
            print(
                f"library_card_id: {reader['library_card_id']}, "
                f"first_name: {reader['first_name']}, "
                f"last_name: {reader['last_name']}, "
                f"email: {reader.get('email', 'N/A')}, "
                f"gender: {reader.get('gender', 'N/A')}, "
                f"birth_year: {reader.get('birth_year', 'N/A')}"
            )

    def display_last_10_readers(self):
        readers_collection = self.database['Readers']
        readers = readers_collection.find().sort("library_card_id", -1).limit(10)
        print("\nLast 10 Readers:")
        for reader in readers:
            print(
                f"library_card_id: {reader['library_card_id']}, "
                f"first_name: {reader['first_name']}, "
                f"last_name: {reader['last_name']}, "
                f"email: {reader.get('email', 'N/A')}, "
                f"gender: {reader.get('gender', 'N/A')}, "
                f"birth_year: {reader.get('birth_year', 'N/A')}"
            )

    def update_reader(self,
                      library_card_id,
                      new_first_name=None,
                      new_last_name=None,
                      new_email=None,
                      new_gender=None,
                      new_birth_year=None):
        """
        Aktualizuj czytelnika według library_card_id, pozwalając na modyfikację:
        first_name, last_name, email, gender, birth_year
        """
        readers_collection = self.database['Readers']
        update_fields = {
            "first_name": new_first_name,
            "last_name": new_last_name,
            "email": new_email,
            "gender": new_gender,
            "birth_year": new_birth_year
        }
        update_fields = {k: v for k, v in update_fields.items() if v is not None}

        if update_fields:
            readers_collection.update_one({"library_card_id": library_card_id}, {"$set": update_fields})
            print(f"Reader with library_card_id={library_card_id} was updated.")
        else:
            print("No fields to update.")

    def delete_reader(self, library_card_id):
        readers_collection = self.database['Readers']
        result = readers_collection.delete_one({"library_card_id": library_card_id})
        if result.deleted_count == 1:
            print(f"Reader with library_card_id={library_card_id} deleted.")
        else:
            print(f"No reader found with library_card_id={library_card_id}.")



    # -------------------- BORROWING --------------------
    def add_borrowing(self, library_card_id, book_id, borrowing_date):
        borrowing_collection = self.database['Borrowing']
        last_borrowing = borrowing_collection.find_one(sort=[("ID", -1)])
        last_id = last_borrowing["ID"] if last_borrowing else 0

        # Jeśli borrowing_date jest obiektem datetime, konwertujemy na string
        if isinstance(borrowing_date, datetime):
            borrowing_date = borrowing_date.strftime('%Y-%m-%d')

        # Automatyczne wyliczenie return_date (30 dni później) w formacie string
        return_date = (
            (datetime.strptime(borrowing_date, '%Y-%m-%d') + timedelta(days=30))
            .strftime('%Y-%m-%d')
        )

        new_borrowing = {
            "ID": last_id + 1,
            "borrowing_date": borrowing_date,
            "return_date": return_date,
            "book_id": book_id,
            "library_card_id": library_card_id
        }
        borrowing_collection.insert_one(new_borrowing)
        print(f"Borrowing added for library_card_id={library_card_id} and book_id={book_id}.")


    def display_borrowings(self):
        borrowing_collection = self.database['Borrowing']
        borrowings = borrowing_collection.find()
        print("\nBorrowings Collection:")
        for borrowing in borrowings:
            borrowing_ID = borrowing.get('ID', 'Unknown')
            borrowing_date = borrowing.get('borrowing_date', 'None')
            return_date = borrowing.get('return_date', 'None')
            library_card_id = borrowing.get('library_card_id', 'Unknown')
            book_id = borrowing.get('book_id', 'Unknown')

            print(
                f"ID: {borrowing_ID}, "
                f"library_card_id: {library_card_id}, "
                f"book_id: {book_id}, "
                f"borrowing_date: {borrowing_date}, "
                f"return_date: {return_date}"
            )


    def display_last_10_borrowings(self):
        borrowing_collection = self.database['Borrowing']
        borrowings = borrowing_collection.find().sort("borrowing_date", -1).limit(10)
        print("\nLast 10 Borrowings:")
        for borrowing in borrowings:
            print(
                f"ID: {borrowing['ID']}, "
                f"library_card_id: {borrowing['library_card_id']}, "
                f"book_id: {borrowing['book_id']}, "
                f"borrowing_date: {borrowing['borrowing_date']}, "
                f"return_date: {borrowing['return_date']}"
            )


    def update_borrowing(self, library_card_id, book_id, new_borrowing_date=None, new_return_date=None):
        borrowing_collection = self.database['Borrowing']

        # Konwersja dat do string w formacie "YYYY-MM-DD", jeśli są datetime
        if isinstance(new_borrowing_date, datetime):
            new_borrowing_date = new_borrowing_date.strftime('%Y-%m-%d')
        if isinstance(new_return_date, datetime):
            new_return_date = new_return_date.strftime('%Y-%m-%d')

        update_fields = {
            "borrowing_date": new_borrowing_date,
            "return_date": new_return_date
        }
        update_fields = {k: v for k, v in update_fields.items() if v is not None}

        if update_fields:
            borrowing_collection.update_one(
                {"library_card_id": library_card_id, "book_id": book_id},
                {"$set": update_fields}
            )
            print(f"Borrowing for library_card_id={library_card_id} and book_id={book_id} updated.")
        else:
            print("No fields to update.")


    def delete_borrowing(self, library_card_id):
        borrowing_collection = self.database['Borrowing']
        result = borrowing_collection.delete_one({"library_card_id": library_card_id})
        if result.deleted_count == 1:
            print(f"Borrowing with library_card_id={library_card_id} deleted.")
        else:
            print(f"No borrowing found with library_card_id={library_card_id}.")


    # -------------------- IMPORT / EXPORT --------------------

    def export_to_json(self):
        show_export_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                collection_name = "Books"
            elif choice == 2:
                collection_name = "Readers"
            elif choice == 3:
                collection_name = "Borrowing"
            else:
                print("Invalid choice. Export canceled.")
                return

            collection = self.database[collection_name]
            data = list(collection.find())

            file_path = input(
                "Paste the full file path (without .json) where you want to save the file, or just paste the folder path (e.g., C:\\Users\\YourName\\Desktop): ")

            if os.path.isdir(file_path):
                file_path = os.path.join(file_path, f"{collection_name.lower()}.json")

            if not file_path.endswith(".json"):
                file_path += ".json"

            try:
                # Zapis danych do pliku
                with open(file_path, 'w') as file:
                    json.dump(data, file, default=str, indent=4)
                absolute_path = os.path.abspath(file_path)
                print(f"Data from '{collection_name}' exported to {absolute_path}")
            except Exception as e:
                print(f"Error writing to file: {e}")
        except Exception as e:
            print(f"Failed to export data: {e}")

    def import_from_json(self):
        show_import_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                collection_name = "Books"
            elif choice == 2:
                collection_name = "Readers"
            elif choice == 3:
                collection_name = "Borrowing"
            else:
                print("Invalid choice. Import canceled.")
                return

            file_path = input(
                "Paste the full file path of the JSON file to import (e.g., C:\\Users\\YourName\\Desktop\\books.json): ")

            if not os.path.isfile(file_path):
                print(f"The file '{file_path}' does not exist. Please check the path and try again.")
                return

            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    collection = self.database[collection_name]

                    last_item = collection.find_one(sort=[("ID", -1)])
                    last_id = last_item["ID"] if last_item else 0
                    for index, item in enumerate(data):
                        item["ID"] = last_id + index + 1

                    collection.insert_many(data)
                print(f"Data imported to collection '{collection_name}' from {file_path}")
            except Exception as e:
                print(f"Error reading from file: {e}")
        except Exception as e:
            print(f"Failed to import data: {e}")

# -------------------- MENU --------------------

def show_main_menu():
    print("\nWelcome to the Library Management System! Choose an option:")
    print("1. Display Data")
    print("2. Enter Data")
    print("3. Modify Data")
    print("4. Export Data")
    print("5. Import Data")
    print("6. Exit")

def show_display_data_menu():
    print("\nChoose a data type to display:")
    print("1. All Books")
    print("2. All Readers")
    print("3. All Borrowings")
    print("4. Last 10 Books")
    print("5. Last 10 Readers")
    print("6. Last 10 Borrowings")

def show_export_menu():
    print("\nChoose a collection to export:")
    print("1. Books")
    print("2. Readers")
    print("3. Borrowings")

def show_import_menu():
    print("\nChoose a collection to import into:")
    print("1. Books")
    print("2. Readers")
    print("3. Borrowings")

def show_enter_data_menu():
    print("\nChoose a data type to enter:")
    print("1. Book")
    print("2. Reader")
    print("3. Borrowing")

def show_modify_data_menu():
    print("\nChoose a data type to modify:")
    print("1. Book")
    print("2. Reader")
    print("3. Borrowing")

def main():
    connection_string = "mongodb+srv://bkostecki:xy3mRddh6EPkgk5@cluster0.znagh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    database_name = "LibraryDB"
    db_manager = DatabaseManager(connection_string, database_name)

    while True:
        show_main_menu()

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            show_display_data_menu()
            try:
                display_choice = int(input("Choose a data type to display: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if display_choice == 1:
                db_manager.display_books()
            elif display_choice == 2:
                db_manager.display_readers()
            elif display_choice == 3:
                db_manager.display_borrowings()
            elif display_choice == 4:
                db_manager.display_last_10_books()
            elif display_choice == 5:
                db_manager.display_last_10_readers()
            elif display_choice == 6:
                db_manager.display_last_10_borrowings()
            else:
                print("Invalid option. Try again.")

        elif choice == 2:
            show_enter_data_menu()
            try:
                data_choice = int(input("Choose a data type to enter: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if data_choice == 1:
                title = input("Enter book title: ")
                authors = input("Enter authors (comma-separated if more than one): ")
                categories = input("Enter categories (comma-separated): ")
                try:
                    published_year = int(input("Enter published_year (YYYY): "))
                    average_rating = float(input("Enter average_rating: "))
                    num_pages = int(input("Enter num_pages: "))
                except ValueError:
                    print("Invalid numeric input. Aborting adding a book.")
                    continue

                db_manager.add_book(
                    title=title,
                    authors=authors,
                    categories=categories,
                    published_year=published_year,
                    average_rating=average_rating,
                    num_pages=num_pages
                )

            elif data_choice == 2:
                first_name = input("Enter reader first_name: ")
                last_name = input("Enter reader last_name: ")
                email = input("Enter reader email: ")
                gender = input("Enter reader gender: ")
                try:
                    birth_year = int(input("Enter reader birth_year (YYYY): "))
                except ValueError:
                    print("Invalid birth_year. Aborting adding a reader.")
                    continue

                db_manager.add_reader(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    gender=gender,
                    birth_year=birth_year
                )

            elif data_choice == 3:
                try:
                    library_card_id = int(input("Enter library card ID: "))
                    book_id = int(input("Enter book ID: "))
                except ValueError:
                    print("Invalid numeric input. Aborting adding a borrowing.")
                    continue

                borrowing_date_str = input("Enter borrowing date (YYYY-MM-DD): ")
                try:
                    borrowing_date = datetime.strptime(borrowing_date_str, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    continue

                db_manager.add_borrowing(library_card_id, book_id, borrowing_date)

            else:
                print("Invalid option. Try again.")

        elif choice == 3:
            show_modify_data_menu()
            try:
                modify_choice = int(input("Choose a data type to modify: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if modify_choice == 1:
                try:
                    book_id = int(input("Enter book ID to update: "))
                except ValueError:
                    print("Invalid book ID.")
                    continue

                new_title = input("Enter new title (leave blank to skip): ") or None
                new_authors = input("Enter new authors (leave blank to skip): ") or None
                new_categories = input("Enter new categories (leave blank to skip): ") or None

                new_published_year_str = input("Enter new published_year (leave blank to skip): ") or None
                new_average_rating_str = input("Enter new average_rating (leave blank to skip): ") or None
                new_num_pages_str = input("Enter new num_pages (leave blank to skip): ") or None

                if new_published_year_str is not None:
                    try:
                        new_published_year = int(new_published_year_str)
                    except ValueError:
                        print("Invalid published_year. Skipping update for that field.")
                        new_published_year = None
                else:
                    new_published_year = None

                if new_average_rating_str is not None:
                    try:
                        new_average_rating = float(new_average_rating_str)
                    except ValueError:
                        print("Invalid average_rating. Skipping update for that field.")
                        new_average_rating = None
                else:
                    new_average_rating = None

                if new_num_pages_str is not None:
                    try:
                        new_num_pages = int(new_num_pages_str)
                    except ValueError:
                        print("Invalid num_pages. Skipping update for that field.")
                        new_num_pages = None
                else:
                    new_num_pages = None

                db_manager.update_book(
                    book_id=book_id,
                    new_title=new_title,
                    new_authors=new_authors,
                    new_categories=new_categories,
                    new_published_year=new_published_year,
                    new_average_rating=new_average_rating,
                    new_num_pages=new_num_pages
                )

            elif modify_choice == 2:
                try:
                    library_card_id = int(input("Enter library_card_id to update: "))
                except ValueError:
                    print("Invalid library_card_id.")
                    continue

                new_first_name = input("Enter new first_name (leave blank to skip): ") or None
                new_last_name = input("Enter new last_name (leave blank to skip): ") or None
                new_email = input("Enter new email (leave blank to skip): ") or None
                new_gender = input("Enter new gender (leave blank to skip): ") or None
                new_birth_year_str = input("Enter new birth_year (leave blank to skip): ") or None

                if new_birth_year_str is not None:
                    try:
                        new_birth_year = int(new_birth_year_str)
                    except ValueError:
                        print("Invalid birth_year. Skipping update for that field.")
                        new_birth_year = None
                else:
                    new_birth_year = None

                db_manager.update_reader(
                    library_card_id=library_card_id,
                    new_first_name=new_first_name,
                    new_last_name=new_last_name,
                    new_email=new_email,
                    new_gender=new_gender,
                    new_birth_year=new_birth_year
                )

            elif modify_choice == 3:
                try:
                    library_card_id = int(input("Enter library card ID: "))
                    book_id = int(input("Enter book ID: "))
                except ValueError:
                    print("Invalid input.")
                    continue

                new_borrowing_date_str = input("Enter new borrowing date (YYYY-MM-DD, leave blank to skip): ") or None
                new_return_date_str = input("Enter new return date (YYYY-MM-DD, leave blank to skip): ") or None

                if new_borrowing_date_str:
                    try:
                        new_borrowing_date = datetime.strptime(new_borrowing_date_str, "%Y-%m-%d")
                    except ValueError:
                        print("Invalid date format. Skipping update for that field.")
                        new_borrowing_date = None
                else:
                    new_borrowing_date = None

                if new_return_date_str:
                    try:
                        new_return_date = datetime.strptime(new_return_date_str, "%Y-%m-%d")
                    except ValueError:
                        print("Invalid date format. Skipping update for that field.")
                        new_return_date = None
                else:
                    new_return_date = None

                db_manager.update_borrowing(
                    library_card_id,
                    book_id,
                    new_borrowing_date=new_borrowing_date,
                    new_return_date=new_return_date
                )

            else:
                print("Invalid option. Try again.")

        elif choice == 4:
            db_manager.export_to_json()


        elif choice == 5:
            db_manager.import_from_json()

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()