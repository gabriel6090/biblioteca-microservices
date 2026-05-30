from flask import Flask
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Starting user service")

app = Flask(__name__)

@app.route('/users')
def users():
    logging.info("Fetching users")
    return [
        {
            "id": 1,
            "nome": "Gabriel"
        },

        {
            "id": 2,
            "nome": "Maria"
        },
        {
            "id": 3,
            "nome": "João"
        },
        {
            "id": 4,
            "nome": "Ana"
        },
        {
            "id": 5,
            "nome": "Carlos"
        },
        {
            "id": 6,
            "nome": "Mariana"
        }

    ]

@app.route('/health')
def health():
    logging.info("Checking health")
    return {"status":"ok"}

app.run(host='0.0.0.0', port=5001)