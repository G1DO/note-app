from flask import Flask, render_template, request, redirect, url_for
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DATABASE_URL")

def get_conn():
    return psycopg2.connect(DB_URL, cursor_factory=RealDictCursor)

app = Flask(__name__)

@app.get("/")
def index():
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, title, content, created_at FROM notes ORDER BY created_at DESC;")
        notes = cur.fetchall()
    return render_template("index.html", notes=notes)

@app.post("/add")
def add_note():
    title = request.form["title"].strip()
    content = request.form["content"].strip()
    if title and content:
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute("INSERT INTO notes (title, content) VALUES (%s, %s);", (title, content))
    return redirect(url_for("index"))

@app.get("/delete/<int:note_id>")
def delete_note(note_id):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM notes WHERE id=%s;", (note_id,))
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
