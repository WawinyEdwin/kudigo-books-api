import sqlite3


def connect_to_db():
    conn = sqlite3.connect("books.db")
    return conn


def create_books_table():
    try:
        conn = connect_to_db()
        # conn.execute("""DROP TABLE books""")
        conn.execute(
            """
            CREATE TABLE books (
                book_id INTEGER PRIMARY KEY NOT NULL,
                isbn INT NOT NULL,
                title VARCHAR NOT NULL,
                author VARCHAR NOT NULL,
                publish_year INT NOT NULL
            );
        """
        )

        conn.commit()
        print("Books table created successfully")
    except Exception as e:
        print(e)
        print("Books table creation failed")
    finally:
        conn.close()


def add_book(data):
    print(data)
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO books (isbn, title, author, publish_year) VALUES (?, ?, ?, ? )""",
            (data["isbn"], data["title"], data["author"], data["publish_year"]),
        )
        conn.commit()
        created_book = get_book_by_id(cur.lastrowid)
        print("Books table created successfully")
    except Exception as e:
        conn.rollback()
        print(e)
        print("Books table creation failed")
    finally:
        conn.close()


def get_books():
    books = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM books")
        rows = cur.fetchall()

        # row convertion to dict
        for i in rows:
            book = {}
            book["book_id"] = i["book_id"]
            book["isbn"] = i["isbn"]
            book["title"] = i["title"]
            book["author"] = i["author"]
            book["publish_year"] = i["publish_year"]
            books.append(book)

        print("Got Books")
    except:
        books = []
        print("Failed to get books")

    return books


def get_book_by_id(book_id):
    book = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
        row = cur.fetchone()
        book = dict(row)
        print(book)
    except:
        book = {}
        print("Failed to get books")

    return book


def update_book_by_id(data, book_id):
    updated_book = {}
    print(data)
    try:
        conn = connect_to_db()
        conn.execute(
            "UPDATE books SET isbn = ?, title = ?, author = ?, publish_year = ?  WHERE book_id = ?",
            (
                data["isbn"],
                data["title"],
                data["author"],
                data["publish_year"],
                book_id,
            ),
        )
        conn.commit()
        # the updated user
        updated_book = get_book_by_id(book_id)
    except:
        conn.rollback()
        print("Failed to get books")
    finally:
        conn.close()

    return updated_book


def delete_book_by_id(book_id):
    msg = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from books WHERE book_id = ?", (book_id,))
        conn.commit()
        msg["status"] = "Book Deleted"
    except:
        conn.rollback()
    finally:
        conn.close()

    return msg
