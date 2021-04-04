from flask import Flask
from data import db_session
import datetime
from flask_login import LoginManager
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key_x'

login_manager = LoginManager()
login_manager.init_app(app)



if __name__ == '__main__':
    db_session.global_init("db/users.db")
    user = User()
    user.name = "имя"
    user.surname = "фамилия"
    user.age = 12
    user.email = "esail@email.ru"
    user.set_password('12345')
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
