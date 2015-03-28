from flask import Flask
from flask_restful import Api,Resource,abort
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# localhost database configuration
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/tz'
db = SQLAlchemy(app)

from resources.author import get_author_resource
from resources.author import get_author_article_resource
from resources.author import get_author_contact_resource

from resources.article import get_article_resource
from resources.article import get_article_list_resource
from resources.article import get_article_list_issue_resource

AuthorResource = get_author_resource(db)
AuthorArticleResource = get_author_article_resource(db)
AuthorContactResource = get_author_contact_resource(db)

ArticleResource = get_article_resource(db)
ArticleListResource = get_article_list_resource(db)
ArticleListIssueResource = get_article_list_issue_resource(db)

class HelloResource(Resource):
    def get(self):
        return {
            "message":'Unofficial api for the blog http://thezine.biz'
        }


api.add_resource(AuthorResource,'/v1/author/<string:author_id>')
api.add_resource(AuthorArticleResource,'/v1/author/<string:author_id>/articles')
api.add_resource(AuthorContactResource,'/v1/author/<string:author_id>/contacts')

api.add_resource(ArticleResource,'/v1/article/<string:article_id>')
api.add_resource(ArticleListResource,'/v1/articles')
api.add_resource(ArticleListIssueResource,'/v1/articles/<string:issue_id>')
api.add_resource(HelloResource,'/')


if __name__ == '__main__':
    app.run(debug=True)
