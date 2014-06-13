from flask import Flask
from flask_restful import Api,Resource
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/tz'
db = SQLAlchemy(app)

from resources.author import get_author_resource
from resources.article import get_article_resource
from resources.author import get_author_article_resource

AuthorResource = get_author_resource(db)
ArticleResource = get_article_resource(db)
AuthorArticleResource = get_author_article_resource(db)

class HelloResource(Resource):
    def get(self):
        return {
            "message":'hey'
        }

api.add_resource(AuthorResource,'/v1/author/<string:author_id>')
api.add_resource(AuthorArticleResource,'/v1/author/<string:author_id>/articles')
api.add_resource(ArticleResource,'/v1/article/<string:article_id>')
api.add_resource(HelloResource,'/')


if __name__ == '__main__':
    app.run(debug=True)
