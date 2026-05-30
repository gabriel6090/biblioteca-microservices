from flask import Flask
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Starting book service")

app = Flask(__name__)

@app.route('/books')
def books():
    logging.info("Fetching books")
    return [
        {
            "id": 1,
            "titulo": "A Morte de Ivan Ilitch"
        },
        {
            "id": 2,
            "titulo": "Call of Cthulhu"
        },
        {
            "id": 3,
            "titulo": "O Apanhador no Campo de Centeio"
        },
        {
            "id": 4,
            "titulo": "Metamorfose"
        },
        {
            "id": 5,
            "titulo": "1984"
        },
        {
            "id": 6,
            "titulo": "Weiss, a Mente é o Limite"
        }
    ]

@app.route('/health')
def health():
    logging.info("Checking health")
    return {"status":"ok"}

app.run(host='0.0.0.0', port=5002)