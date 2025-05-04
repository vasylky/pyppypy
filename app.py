import os
from flask import Flask, render_template, request, redirect
import mysql.connector
import time

app = Flask(__name__)

# Повторні спроби з'єднання з MySQL
while True:
    try:
        db = mysql.connector.connect(
            host=os.environ.get("MYSQL_HOST", "db"),
            user=os.environ.get("MYSQL_USER", "root"),
            password=os.environ.get("MYSQL_PASSWORD", ""),
            database=os.environ.get("MYSQL_DATABASE", "")
        )
        break
    except mysql.connector.Error as err:
        print(f"MySQL connection error: {err}")
        time.sleep(2)

cursor = db.cursor()


@app.route('/')
def index():
    print("Connected to database:", db.database)

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return render_template("index.html", books=books)

@app.route('/add', methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form['title']
        author = request.form['author']
        cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
        db.commit()
        return redirect('/')
    return render_template("add_book.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

