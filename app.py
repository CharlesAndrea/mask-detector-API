from flask import Flask
from flask_restful import Resource, Api
from flask_migrate import Migrate
from models.models import db

from routes.empleado_routes import empleado_bp
from routes.historial_routes import historial_bp

app = Flask(__name__)
api = Api(app)

app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(empleado_bp, url_prefix='/empleados')
app.register_blueprint(historial_bp, url_prefix='/historiales')



class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)