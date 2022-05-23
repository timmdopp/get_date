# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("NAME")
DATABASE_PASSWORD = os.environ.get("PWORD")
print(SECRET_KEY)
print(DATABASE_PASSWORD)