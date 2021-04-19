from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.login_form import LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from User_register import User_register
from боты.email_sendler import send_message
import goroskop
import get_zapross

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
    global current_user
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        else:
            return render_template('login.html', message="Wrong login or password", form=form)
    return render_template('login.html', title='Authorization', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    global current_user
    form = User_register()
    if form.validate_on_submit():
        user = User()
        user.name = form.name.data
        user.surname = form.surname.data
        user.age = form.age.data
        db_sess = db_session.create_session()
        a = db_sess.query(User).filter(User.email == form.email.data).first()
        if not a:
            user.email = form.email.data
        else:
            return render_template('register.html', message="Такой E-mail уже зарегестрирован", form=form)
        if form.birth_date.data.count('.') == 2 or len(form.birth_date.data) != 10:
            user.birth_date = form.birth_date.data
        else:
            return render_template('register.html', message="пишите дату в формате 00(день).00(месяц).0000(год)",
                                   form=form)
        user.set_password(str(form.password.data))
        stroka = [f'Поздравляем с регистрацией {user.name} {user.surname}!', f'Вы зарегестрировались на нашем сайте',
                  f'Вы указали что вам {user.age} лет и ваш день рождения {user.birth_date}!']
        stroka = '\n'.join(stroka)
        send_message(form.email.data, stroka)
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)

        return redirect("/")
    else:
        return render_template('register.html', message="Упс, что то ввели неправильно", form=form)
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/show')
@login_required
def show_gor():
    date = current_user.birth_date
    m, d = int(date.split('.')[1]), int(date.split('.')[0])
    print(date)
    message = goroskop.z_s(goroskop.zodiac_sign(m, d))
    return render_template('show.html', message=message)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    app.register_blueprint(get_zapross.blueprint)
    print('http://127.0.0.1:8080/')
    db_session.global_init("db/users.db")  # сюда подставим бд
    app.run(port=8080, host='127.0.0.1')
