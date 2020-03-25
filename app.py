from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Selamat datang'


@app.route('/admin/')
def admin_page():
    return 'Ini adalah halaman admin'


if __name__ == '__main__':
    app.run()
