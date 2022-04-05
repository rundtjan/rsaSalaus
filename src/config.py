import os
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv("APP_SECRET")
DB_URI = os.getenv("DATABASE_URL")
