````markdown
# 📝 Note App

A simple Flask + PostgreSQL note-taking app.  
Built with **Python**, **Flask**, **PostgreSQL**, **HTML/CSS**.

---

## 🚀 Features
- Add and delete notes
- Stores notes in PostgreSQL
- Simple HTML/CSS frontend
- Lightweight Flask backend

---

## ⚙️ Requirements
- Python 3.10+
- PostgreSQL 13+
- Virtualenv (recommended)

---

## 📦 Setup & Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/G1DO/note-app.git
   cd note-app
````

2. **Create virtual environment & install dependencies**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # On Windows PowerShell: .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

3. **Setup PostgreSQL**

   * Create a database `notesdb`
   * Run the schema:

     ```sql
     CREATE TABLE IF NOT EXISTS notes (
         id SERIAL PRIMARY KEY,
         title VARCHAR(100) NOT NULL,
         content TEXT NOT NULL,
         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
     );
     ```

4. **Environment variables**
   Create a `.env` file in the project root:

   ```ini
   FLASK_ENV=development
   DATABASE_URL=postgresql://<USER>:<PASSWORD>@<HOST>:5432/notesdb
   ```

   Example (if Postgres is running on Windows and Flask runs in WSL):

   ```ini
   DATABASE_URL=postgresql://postgres:1965@172.29.64.1:5432/notesdb
   ```

5. **Run the app**

   ```bash
   python3 app.py
   ```

6. Open in browser:

   ```
   http://127.0.0.1:5000
   ```

---

## 📂 Project Structure

```
note-app/
│── app.py             # Flask backend
│── requirements.txt   # Python dependencies
│── templates/         # HTML templates
│   └── index.html
│── static/            # CSS styles
│   └── style.css
└── .env.example       # Example env file
```


Would you like me to also generate a **`.env.example` file** (instead of exposing your real password) so you can commit that safely to GitHub?
```
