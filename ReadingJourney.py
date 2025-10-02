# -*- coding: utf-8 -*-
"""
ReadingJourney.py

Console-based Python application for managing a personal reading journey.
Connects to an SQLite database (MyReadingJourney.db) and allows:
- Creation of the database and table
- Insertion of new books
- Updating the status of books
- Deleting books
- Displaying all registered books
"""

import sqlite3

# Global connection variable
conn = None

def create_db_and_table():
    """Create the database and the 'libros' table if they do not exist."""
    global conn
    try:
        conn = sqlite3.connect('MyReadingJourney.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                estado TEXT CHECK(estado IN ('Pendiente', 'En progreso', 'Terminado')))
        ''')
        
        # Insert sample data if table is empty
        cursor.execute('SELECT COUNT(*) FROM libros')
        if cursor.fetchone()[0] == 0:
            sample_books = [
                ("Choose Wonder Over Worry", "Amber Rae", "Terminado"),
                ("El poder del Ahora", "Eckhart Tolle", "En progreso"),
                ("The light we carry", "Michelle Obama", "Pendiente"),
                ("Una nueva tierra", "Eckhart Tolle", "Terminado"),
                ("Toxic positivity", "Whitney Goodman", "Pendiente")
            ]
            cursor.executemany('''
                INSERT INTO libros (titulo, autor, estado)
                VALUES (?, ?, ?)
            ''', sample_books)
            print("\nSample books inserted successfully.")

        conn.commit()
        print("\nDatabase and table 'libros' created successfully.")
    except sqlite3.Error as e:
        print("\nError while creating database or table: {}".format(e))

def insert_book():
    """Insert a new book into the 'libros' table."""
    global conn
    print("\n--- Insert a New Book ---")
    titulo = input("Book title: ")
    autor = input("Author: ")
    estado = input("Status (Pendiente/In progreso/Terminado): ").capitalize()
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO libros (titulo, autor, estado)
            VALUES (?, ?, ?)
        ''', (titulo, autor, estado))
        conn.commit()
        print("\nBook inserted successfully.")
    except sqlite3.Error as e:
        print("\nError while inserting the book: {}".format(e))

def update_book_status():
    """Update the status of a book identified by its ID."""
    global conn
    print("\n--- Update Book Status ---")
    show_all_books()
    id_libro = input("\nEnter the ID of the book to update: ")
    new_status = input("New status (Pendiente/In progreso/Terminado): ").capitalize()
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE libros
            SET estado = ?
            WHERE id = ?
        ''', (new_status, id_libro))
        conn.commit()
        if cursor.rowcount > 0:
            print("\nBook status updated successfully.")
        else:
            print("\nNo book found with ID {}.".format(id_libro))
    except sqlite3.Error as e:
        print("\nError while updating book status: {}".format(e))

def delete_book():
    """Delete a book from the 'libros' table by its ID."""
    global conn
    print("\n--- Delete a Book ---")
    show_all_books()
    id_libro = input("\nEnter the ID of the book to delete: ")
    
    try:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM libros
            WHERE id = ?
        ''', (id_libro,))
        conn.commit()
        if cursor.rowcount > 0:
            print("\nBook deleted successfully.")
        else:
            print("\nNo book found with ID {}.".format(id_libro))
    except sqlite3.Error as e:
        print("\nError while deleting the book: {}".format(e))

def show_all_books():
    """Display all books stored in the 'libros' table."""
    global conn
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM libros')
        books = cursor.fetchall()
        if books:
            print("\n--- Book List ---")
            print("{:<5} {:<30} {:<25} {:<15}".format("ID", "Title", "Author", "Status"))
            print("-"*75)
            for book in books:
                print("{:<5} {:<30} {:<25} {:<15}".format(book[0], book[1], book[2], book[3]))
        else:
            print("\nNo books found.")
    except sqlite3.Error as e:
        print("\nError while displaying books: {}".format(e))

def show_menu():
    """Display the main menu."""
    print("\nMY READING JOURNEY - Book Management")
    print("1. Show all books")
    print("2. Add a new book")
    print("3. Update book status")
    print("4. Delete a book")
    print("5. Exit")

def main():
    """Main program loop."""
    create_db_and_table()
    
    while True:
        show_menu()
        option = input("\nSelect an option (1-5): ")
        
        if option == "1":
            show_all_books()
        elif option == "2":
            insert_book()
        elif option == "3":
            update_book_status()
        elif option == "4":
            delete_book()
        elif option == "5":
            print("\nApplication terminated. Thank you for using Reading Journey.")
            if conn:
                conn.close()
            break
        else:
            print("\nInvalid option. Please select a number between 1 and 5.")
        
        input("\nPress Enter to continue...")

if __name__ == '__main__':
    main()
