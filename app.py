from flask import Flask
from flask_restful import Resource, Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)

app.config.from_object('config')


db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)