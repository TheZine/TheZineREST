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

def get_article_list_resource(db):

    Article = get_article_model(db)

    class ArticleListResource(Resource):
        def get(self):
            articles = []
            keys = ['id','title','author','tagline']
            for article in Article.query.all():
                article_dict = article.serialize()
                articles.append({key:article_dict[key] for key in keys})
            return {
                "meta":{
                    'is_successful':True,
                    'code':200
                },
                "data":{
                    "articles":articles,
                    "no_of_articles":len(articles)
                }
            }

    return ArticleListResource

def get_article_list_issue_resource(db):

    Article = get_article_model(db)

    class ArticleListIssueResource(Resource):
        def get(self,issue_id):
            abort_if_issue_doesnt_exist(issue_id)
            articles = []
            keys = ['id','title','author','tagline']
            for article in Article.query.all():
                article_dict = article.serialize()
                articles.append({key:article_dict[key] for key in keys})
            return {
                "meta":{
                    'is_successful':True,
                    'code':200
                },
                "data":{
                    "articles":articles,
                    "no_of_articles":len(articles)
                }
            }

    def abort_if_issue_doesnt_exist(issue_id):
        if issue_id in range(0,10):
            abort(404,meta={'code':404,'is_successful':False},message="Issue {} doesn't exist".format(issue_id))

    return ArticleListIssueResource