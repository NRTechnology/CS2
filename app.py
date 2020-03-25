from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# ini adalah pertemuan 3
@app.route('/')
def hello_world():
    return 'Selamat datang'


@app.route('/admin/')
def admin_page():
    return 'Ini adalah halaman admin'


# materi pertemuan 3 berakhir di sini


# ini adalah materi pertemuan 4
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/helloworld')

# materi pertemuan 4 berakhir di sini

if __name__ == '__main__':
    app.run()
