__author__ = 'ABHIJEET'

from flask_restful import Resource,abort
from models.author import get_author_model
from models.article import get_article_model


def get_author_resource(db):

    Author = get_author_model(db)

    class AuthorResource(Resource):
        def get(self,author_id):
            abort_if_author_doesnt_exist(author_id)
            return {
                "message":"Author with this id exist",
                "meta":{
                    'is_successful':True,
                    'code':200
                },
               "data": Author.query.filter_by(id=author_id).first().serialize_profile()
            }

    def abort_if_author_doesnt_exist(author_id):
        author_list = []
        for author in Author.query.all():
            author_dict = author.serialize_profile()
            author_list.append(author_dict['id'])

        if author_id not in author_list:
            abort(404,meta={'code':404,'is_successful':False},message="Author with id {} doesn't exist".format(author_id))

    return AuthorResource

def get_author_article_resource(db):

    Article = get_article_model(db)

    class AuthorArticleResource(Resource):
        def get(self,author_id):
            author_articles = []
            for article in Article.query.filter_by(author_id=author_id):
                author_articles.append(article.serialize())

            return {
                "message":"Author with this id exist",
                "meta":{
                    'is_successful':True,
                    'code':200
                },
               "data":{
                   "no_of_articles":len(author_articles),
                   "articles":author_articles
               }
            }

    return AuthorArticleResource