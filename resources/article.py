__author__ = 'ABHIJEET'

from flask_restful import Resource,abort
from models.article import get_article_model


def get_article_resource(db):

    Article = get_article_model(db)

    class ArticleResource(Resource):
        def get(self,article_id):
            abort_if_article_doesnt_exist(article_id)
            return {
                "message":"Article with this id exist",
                "meta":{
                    'is_successful':True,
                    'code':200
                },
                "data":Article.query.filter_by(id=article_id).first().serialize()
            }

    def abort_if_article_doesnt_exist(article_id):
        article_list = []
        for article in Article.query.all():
            article_dict = article.serialize()
            article_list.append(article_dict['id'])
        if article_id not in article_list :
            abort(404,meta={'code':404,'is_successful':False},message="Article with id {} doesn't exist".format(article_id))

    return ArticleResource