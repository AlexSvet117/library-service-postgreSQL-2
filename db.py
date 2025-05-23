from models.book_model import Book
import psycopg2
from flask import g, current_app

book1 = Book(
        book_id = "001",
        title = "Oi Cat",
        author = "Some Author",
        publication_year = 2000,
        genre = "Kids books",
        read_status = "to-read",
        rating = 4.6,
        notes = "Quite a book to read for 7 year-olds"
    )

book2 = Book(
        book_id = "002",
        title = "Oi Frog",
        author = "Some Author",
        publication_year = 2002,
        genre = "Kids books",
        read_status = "to-read",
        rating = 4.8,
        notes = "Quite a book to read for 7 year-olds too"
    )

book_data = [book1, book2]


def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            dbname ="flask_postgres_db", 
            user ="postgres",
            password ="postgres",
            host="localhost",
            port="5432"
        )
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()