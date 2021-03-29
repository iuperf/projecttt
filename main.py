from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           text=user)


if __name__ == '__main__':
    print('http://127.0.0.1:8080/index')
    app.run(port=8080, host='127.0.0.1')
