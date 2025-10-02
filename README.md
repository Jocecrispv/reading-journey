# ReadingJourney

**ReadingJourney** is a Python console-based application for managing a personal library.  
It connects to an SQLite database (`MyReadingJourney.db`) and provides the following features:

- Automatic creation of the database and table if not present  
- Insertion of new books (title, author, and status)  
- Update of the reading status of existing books  
- Deletion of books by their ID  
- Display of all registered books in a formatted list  

This project was developed as a practice activity to apply Python and database management concepts.


## Features

- **Database connection** using SQLite (`sqlite3`)  
- **CRUD operations**: Create, Read, Update, Delete  
- **Console-based menu** for user interaction  


## Requirements

- Python 3.x  
- Uses the Python standard library (`sqlite3` module for database management)  
- *Optional:* [DB Browser for SQLite](https://sqlitebrowser.org/) – useful for inspecting the database manually


## How to Run

1. Clone the repository
2. Execute the script:

```bash
python ReadingJourney.py
```
3. The database file MyReadingJourney.db will be created automatically in the working directory.
