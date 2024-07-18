from dotenv import load_dotenv
import os

load_dotenv()

FLASK_ENV = os.getenv('FLASK_ENV', 'development')

PG_HOST = os.getenv('PG_HOST', '127.0.0.1')
PG_DB = os.getenv('PG_DB', 'db')
PG_USER = os.getenv('PG_USER', 'admin')
PG_PASS = os.getenv('PG_PASS', 'admin')
PG_PORT = os.getenv('PG_PORT', '5432')

if FLASK_ENV == 'production':
    DB_URL = f'postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}'
else:
    DB_URL = f'postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}'