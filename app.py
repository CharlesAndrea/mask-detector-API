from flask import Flask
from flask_restful import Resource, Api
from flask_migrate import Migrate
from models.models import db, marsh
from flask_cors import CORS


from routes.empleado_routes import empleado_bp
from routes.historial_routes import historial_bp
from routes.departamento_routes import departamento_bp
from routes.auth_routes import auth_bp

app = Flask(__name__)
api = Api(app)
cors = CORS()
#cors = CORS(
#    app,
#    resources={r"*": {"origins": "http://localhost:4200/"}},
#    allow_headers=["x-access-token", "Authorization"],
#    expose_headers=["Authorization", "x-access-token", "Content-Type"],
#    methods=["GET", "POST", "PUT", 'DELETE'],
#    supports_credentials=True,)


app.config.from_object('config')

db.init_app(app)
cors.init_app(app)
marsh.init_app(app)
migrate = Migrate(app, db)


app.register_blueprint(empleado_bp, url_prefix='/empleados')
app.register_blueprint(historial_bp, url_prefix='/historiales')
app.register_blueprint(departamento_bp, url_prefix='/departamentos')
app.register_blueprint(auth_bp, url_prefix='/auth')



class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)