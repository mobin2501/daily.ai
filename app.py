from flask import Flask
from models import db
from views import bp
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SECRET_KEY'] = config.SECRET_KEY

db.init_app(app)

app.register_blueprint(bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)