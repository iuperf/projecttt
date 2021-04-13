from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.login_form import LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key_x'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def main_page():
    return render_template('main_page.html')

"""Заход на главную страницу"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        print(user.check_password(form.password.data))
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        else:
            return render_template('login.html', message="Wrong login or password", form=form)
    return render_template('login.html', title='Authorization', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    print('http://127.0.0.1:8080/')
    db_session.global_init("db/users.db") # сюда подставим бд
    app.run(port=8080, host='127.0.0.1')
