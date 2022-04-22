from flask import Flask
from flask_login import LoginManager
from config import SECRET

app = Flask(__name__)
app.secret_key = SECRET

import routes
