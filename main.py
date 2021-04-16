from flask import Flask, render_template, redirect
from data import db_session
import datetime
from data.users import User
from data.login_form import LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user
from User_register import User_register
from боты.email_sendler import send_message
from bisect import bisect
import sqlite3

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


signs = [(1,20,"Козерог"), (2,18,"Водолей"), (3,20,"Рыбы"), (4,20,"Овен"),
         (5,21,"Телец"), (6,21,"Близнецы"), (7,22,"Рак"), (8,23,"Лев"),
         (9,23,"Дева"), (10,23,"Весы"), (11,22,"Скорпион"), (12,22,"Стрелец"),
         (12,31,"Козерог")]


def zodiac_sign(m, d):
    zn = signs[bisect(signs, (m, d))][2]
    return zn

def z_s(zn):
    con = sqlite3.connect('db/inform.db')
    cur = con.cursor()
    if zn == "Близнецы":
        zn['a'] = cur.execute("SELECT zz FROM BLIZNEZI")
        zn['b'] = cur.execute("SELECT asz FROM BLIZNEZI")
        zn['c'] = cur.execute("SELECT otl FROM BLIZNEZI")
        zn['d'] = cur.execute("SELECT pred FROM BLIZNEZI")
        zn['e'] = cur.execute("SELECT plus FROM BLIZNEZI")
        zn['f'] = cur.execute("SELECT minus FROM BLIZNEZI")
        zn['g'] = cur.execute("SELECT sov FROM BLIZNEZI")
        zn['h'] = cur.execute("SELECT nesov FROM BLIZNEZI")
        zn['i'] = cur.execute("SELECT delo FROM BLIZNEZI")
        zn['j'] = cur.execute("SELECT chislo FROM BLIZNEZI")
        zn['k'] = cur.execute("SELECT prognos FROM BLIZNEZI")
    elif zn == "Овен":
        zn['a'] = cur.execute("SELECT zz FROM OVEN")
        zn['b'] = cur.execute("SELECT asz FROM OVEN")
        zn['c'] = cur.execute("SELECT otl FROM OVEN")
        zn['d'] = cur.execute("SELECT pred FROM OVEN")
        zn['e'] = cur.execute("SELECT plus FROM OVEN")
        zn['f'] = cur.execute("SELECT minus FROM OVEN")
        zn['g'] = cur.execute("SELECT sov FROM OVEN")
        zn['h'] = cur.execute("SELECT nesov FROM OVEN")
        zn['i'] = cur.execute("SELECT delo FROM OVEN")
        zn['j'] = cur.execute("SELECT chislo FROM OVEN")
        zn['k'] = cur.execute("SELECT prognos FROM OVEN")
    elif zn == "Телец":
        zn['a'] = cur.execute("SELECT zz FROM TELEZ")
        zn['b'] = cur.execute("SELECT asz FROM TELEZ")
        zn['c'] = cur.execute("SELECT otl FROM TELEZ")
        zn['d'] = cur.execute("SELECT pred FROM TELEZ")
        zn['e'] = cur.execute("SELECT plus FROM TELEZ")
        zn['f'] = cur.execute("SELECT minus FROM TELEZ")
        zn['g'] = cur.execute("SELECT sov FROM TELEZ")
        zn['h'] = cur.execute("SELECT nesov FROM TELEZ")
        zn['i'] = cur.execute("SELECT delo FROM TELEZ")
        zn['j'] = cur.execute("SELECT chislo FROM TELEZ")
        zn['k'] = cur.execute("SELECT prognos FROM TELEZ")
    elif zn == "Рак":
        zn['a'] = cur.execute("SELECT zz FROM RAK")
        zn['b'] = cur.execute("SELECT asz FROM RAK")
        zn['c'] = cur.execute("SELECT otl FROM RAK")
        zn['d'] = cur.execute("SELECT pred FROM RAK")
        zn['e'] = cur.execute("SELECT plus FROM RAK")
        zn['f'] = cur.execute("SELECT minus FROM RAK")
        zn['g'] = cur.execute("SELECT sov FROM RAK")
        zn['h'] = cur.execute("SELECT nesov FROM RAK")
        zn['i'] = cur.execute("SELECT delo FROM RAK")
        zn['j'] = cur.execute("SELECT chislo FROM RAK")
        zn['k'] = cur.execute("SELECT prognos FROM RAK")
    elif zn == "Лев":
        zn['a'] = cur.execute("SELECT zz FROM LEB")
        zn['b'] = cur.execute("SELECT asz FROM LEB")
        zn['c'] = cur.execute("SELECT otl FROM LEB")
        zn['d'] = cur.execute("SELECT pred FROM LEB")
        zn['e'] = cur.execute("SELECT plus FROM LEB")
        zn['f'] = cur.execute("SELECT minus FROM LEB")
        zn['g'] = cur.execute("SELECT sov FROM LEB")
        zn['h'] = cur.execute("SELECT nesov FROM LEB")
        zn['i'] = cur.execute("SELECT delo FROM LEB")
        zn['j'] = cur.execute("SELECT chislo FROM LEB")
        zn['k'] = cur.execute("SELECT prognos FROM LEB")
    elif zn == "Дева":
        zn['a'] = cur.execute("SELECT zz FROM DEVA")
        zn['b'] = cur.execute("SELECT asz FROM DEVA")
        zn['c'] = cur.execute("SELECT otl FROM DEVA")
        zn['d'] = cur.execute("SELECT pred FROM DEVA")
        zn['e'] = cur.execute("SELECT plus FROM DEVA")
        zn['f'] = cur.execute("SELECT minus FROM DEVA")
        zn['g'] = cur.execute("SELECT sov FROM DEVA")
        zn['h'] = cur.execute("SELECT nesov FROM DEVA")
        zn['i'] = cur.execute("SELECT delo FROM DEVA")
        zn['j'] = cur.execute("SELECT chislo FROM DEVA")
        zn['k'] = cur.execute("SELECT prognos FROM DEVA")
    elif zn == "Весы":
        zn['a'] = cur.execute("SELECT zz FROM VECI")
        zn['b'] = cur.execute("SELECT asz FROM VECI")
        zn['c'] = cur.execute("SELECT otl FROM VECI")
        zn['d'] = cur.execute("SELECT pred FROM VECI")
        zn['e'] = cur.execute("SELECT plus FROM VECI")
        zn['f'] = cur.execute("SELECT minus FROM VECI")
        zn['g'] = cur.execute("SELECT sov FROM VECI")
        zn['h'] = cur.execute("SELECT nesov FROM VECI")
        zn['i'] = cur.execute("SELECT delo FROM VECI")
        zn['j'] = cur.execute("SELECT chislo FROM VECI")
        zn['k'] = cur.execute("SELECT prognos FROM VECI")
    elif zn == "Скорпион":
        zn['a'] = cur.execute("SELECT zz FROM SKORPION")
        zn['b'] = cur.execute("SELECT asz FROM SKORPION")
        zn['c'] = cur.execute("SELECT otl FROM SKORPION")
        zn['d'] = cur.execute("SELECT pred FROM SKORPION")
        zn['e'] = cur.execute("SELECT plus FROM SKORPION")
        zn['f'] = cur.execute("SELECT minus FROM SKORPION")
        zn['g'] = cur.execute("SELECT sov FROM SKORPION")
        zn['h'] = cur.execute("SELECT nesov FROM SKORPION")
        zn['i'] = cur.execute("SELECT delo FROM SKORPION")
        zn['j'] = cur.execute("SELECT chislo FROM SKORPION")
        zn['k'] = cur.execute("SELECT prognos FROM SKORPION")
    elif zn == "Стрелец":
        zn['a'] = cur.execute("SELECT zz FROM CTRELEZ")
        zn['b'] = cur.execute("SELECT asz FROM CTRELEZ")
        zn['c'] = cur.execute("SELECT otl FROM CTRELEZ")
        zn['d'] = cur.execute("SELECT pred FROM CTRELEZ")
        zn['e'] = cur.execute("SELECT plus FROM CTRELEZ")
        zn['f'] = cur.execute("SELECT minus FROM CTRELEZ")
        zn['g'] = cur.execute("SELECT sov FROM CTRELEZ")
        zn['h'] = cur.execute("SELECT nesov FROM CTRELEZ")
        zn['i'] = cur.execute("SELECT delo FROM CTRELEZ")
        zn['j'] = cur.execute("SELECT chislo FROM CTRELEZ")
        zn['k'] = cur.execute("SELECT prognos FROM CTRELEZ")
    elif zn == "Рак":
        zn['a'] = cur.execute("SELECT zz FROM RAK")
        zn['b'] = cur.execute("SELECT asz FROM RAK")
        zn['c'] = cur.execute("SELECT otl FROM RAK")
        zn['d'] = cur.execute("SELECT pred FROM RAK")
        zn['e'] = cur.execute("SELECT plus FROM RAK")
        zn['f'] = cur.execute("SELECT minus FROM RAK")
        zn['g'] = cur.execute("SELECT sov FROM RAK")
        zn['h'] = cur.execute("SELECT nesov FROM RAK")
        zn['i'] = cur.execute("SELECT delo FROM RAK")
        zn['j'] = cur.execute("SELECT chislo FROM RAK")
        zn['k'] = cur.execute("SELECT prognos FROM RAK")
    elif zn == "Козерог":
        zn['a'] = cur.execute("SELECT zz FROM KOZA")
        zn['b'] = cur.execute("SELECT asz FROM KOZA")
        zn['c'] = cur.execute("SELECT otl FROM KOZA")
        zn['d'] = cur.execute("SELECT pred FROM KOZA")
        zn['e'] = cur.execute("SELECT plus FROM KOZA")
        zn['f'] = cur.execute("SELECT minus FROM KOZA")
        zn['g'] = cur.execute("SELECT sov FROM KOZA")
        zn['h'] = cur.execute("SELECT nesov FROM KOZA")
        zn['i'] = cur.execute("SELECT delo FROM KOZA")
        zn['j'] = cur.execute("SELECT chislo FROM KOZA")
        zn['k'] = cur.execute("SELECT prognos FROM KOZA")
    elif zn == "Водолей":
        zn['a'] = cur.execute("SELECT zz FROM VODOLEI")
        zn['b'] = cur.execute("SELECT asz FROM VODOLEI")
        zn['c'] = cur.execute("SELECT otl FROM VODOLEI")
        zn['d'] = cur.execute("SELECT pred FROM VODOLEI")
        zn['e'] = cur.execute("SELECT plus FROM VODOLEI")
        zn['f'] = cur.execute("SELECT minus FROM VODOLEI")
        zn['g'] = cur.execute("SELECT sov FROM VODOLEI")
        zn['h'] = cur.execute("SELECT nesov FROM VODOLEI")
        zn['i'] = cur.execute("SELECT delo FROM VODOLEI")
        zn['j'] = cur.execute("SELECT chislo FROM VODOLEI")
        zn['k'] = cur.execute("SELECT prognos FROM VODOLEI")
    elif zn == "Рыбы":
        zn['a'] = cur.execute("SELECT zz FROM RIBA")
        zn['b'] = cur.execute("SELECT asz FROM RIBA")
        zn['c'] = cur.execute("SELECT otl FROM RIBA")
        zn['d'] = cur.execute("SELECT pred FROM RIBA")
        zn['e'] = cur.execute("SELECT plus FROM RIBA")
        zn['f'] = cur.execute("SELECT minus FROM RIBA")
        zn['g'] = cur.execute("SELECT sov FROM RIBA")
        zn['h'] = cur.execute("SELECT nesov FROM RIBA")
        zn['i'] = cur.execute("SELECT delo FROM RIBA")
        zn['j'] = cur.execute("SELECT chislo FROM RIBA")
        zn['k'] = cur.execute("SELECT prognos FROM RIBA")
 


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


@app.route('/register', methods=['GET', 'POST'])
def register():
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

        try:
            date = str(form.birth_date.data) + ' ' + '00:00'
            user.birth_date = datetime.datetime.strptime(date, "%d.%m.%y %H:%M")
        except ValueError:
            return render_template('register.html', message="Дата должна быть в формате dd.mm.yy", form=form)
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
        print(user.check_password(form.password.data))
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)

        return redirect("/")
    else:
        return render_template('register.html', message="Упс, что то ввели неправильно", form=form)
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    print('http://127.0.0.1:8080/')
    db_session.global_init("db/users.db")  # сюда подставим бд
    app.run(port=8080, host='127.0.0.1')
