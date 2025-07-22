from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

# Azure SQL Database connection variables
server = 'flask-sql-server1.database.windows.net'
database = 'flaskdb'
username = 'sqladmin'  # 🔁 Replace with your actual username
password = 'YourSecurePassword123!'  # 🔁 Replace with your actual password

# Connection string
connection_string = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=no;"
    f"Connection Timeout=30;"
)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ''
    all_messages = []

    try:
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Handle form submission
        if request.method == 'POST':
            message = request.form['message']
            cursor.execute("INSERT INTO messages (message) VALUES (?)", message)
            conn.commit()

        # Retrieve all messages
        cursor.execute("SELECT message FROM messages ORDER BY id DESC")
        all_messages = [row[0] for row in cursor.fetchall()]

    except Exception as e:
        return f"<h2>Database error:</h2><pre>{e}</pre>"

    finally:
        if 'conn' in locals():
            conn.close()

    return render_template('index.html', message=message, all_messages=all_messages)

if __name__ == '__main__':
    app.run(debug=True)
