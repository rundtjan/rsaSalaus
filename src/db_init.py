from app import app, db
from models.user import User

db.create_all(app=app)
db.session.commit()
