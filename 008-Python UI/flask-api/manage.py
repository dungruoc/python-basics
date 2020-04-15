# https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/

# pip install flask-bcrypt
# pip install flask-restplus
# pip install Flask-Script
# pip install flask_testing
# pip install Werkzeug==0.16.1


from flask import Flask
from flask_bcrypt import Bcrypt

from flask_restplus import Api
from flask import Blueprint

from controllers import user_api as user_api

config = {
}

def create_app():
  app = Flask(__name__)
  app.config.from_object(config)
  flask_bcrypt = Bcrypt()
  flask_bcrypt.init_app(app)
  blueprint = Blueprint('api', __name__)
  api = Api(blueprint,
            title='FLASK RESTPLUS API',
            version='1.0',
            description='a flask restplus web service'
            )
  
  api.add_namespace(user_api, path='/user')
  
  app.register_blueprint(blueprint)
  app.app_context().push()
  return app

app = create_app()

def run():
  app.run() # ng serve

if __name__ == "__main__":
  run()
  # gunicorn http-server angular-http-server