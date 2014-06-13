from flask import Flask
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/tz'
db = SQLAlchemy(app)

from resources.author import get_author_resource

AuthorResource = get_author_resource(db)

class HelloResource(Resource):
    def get(self):
        return {
            "message":'hey'
        }

api.add_resource(AuthorResource,'/v1/author/<string:author_id>')
api.add_resource(HelloResource,'/')


if __name__ == '__main__':
    app.run(debug=True)
