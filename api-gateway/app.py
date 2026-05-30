from flask import Flask
import requests
import logging
import os

logging.basicConfig(level=logging.INFO)
logging.info("Starting API gateway")

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Biblioteca Microservices</title>

        <style>
            body{
                font-family: Arial;
                text-align:center;
                margin-top:100px;
                background:#f5f5f5;
            }

            h1{
                color:#333;
            }

            a{
                display:block;
                margin:20px;
                font-size:24px;
                text-decoration:none;
            }
        </style>

    </head>

    <body>

        <h1>📚 Biblioteca Microservices</h1>

        <a href="/users">👤 Usuários</a>
        <a href="/books">📖 Livros</a>

    </body>
    </html>
    """

USER_SERVICE_URL = os.getenv(
    "USER_SERVICE_URL",
    "http://user-service:5001"
)

BOOK_SERVICE_URL = os.getenv(
    "BOOK_SERVICE_URL",
    "http://book-service:5002"
)

@app.route('/books')
def books():

    livros = requests.get("http://book-service:5002/books").json()

    html = """
    <html>
    <head>
        <title>Livros</title>
        <style>
            body { font-family: Arial; background:#f4f4f4; padding:40px; }
            .card { background:white; padding:15px; margin:10px; border-radius:8px; }
        </style>
    </head>
    <body>
        <h1>📚 Livros</h1>
    """

    for livro in livros:
        html += f"""
        <div class="card">
            <b>ID:</b> {livro['id']}<br>
            <b>Título:</b> {livro['titulo']}
        </div>
        """

    html += "</body></html>"
    return html

@app.route('/health')
def health():
    return {"status":"ok"}

app.run(host='0.0.0.0', port=5000)