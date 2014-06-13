__author__ = 'ABHIJEET'

from flask_restful import Resource,abort
from models.article import get_article_model


def get_issue_resource(db):

    Article = get_article_model(db)

    class IssueResource(Resource):
        def get(self,issue_id):
            abort_if_issue_doesnt_exist(issue_id)
            articles = []
            for article in Article.query.filter_by(issue=issue_id):
                articles.append(article.serialize())
            return {
                "message":"Article with this id exist",
                "meta":{
                    'is_successful':True,
                    'code':200
                },
                "data":{
                    "articles":articles
                }
            }

    def abort_if_issue_doesnt_exist(issue_id):
        if issue_id in range(0,10):
            abort(404,meta={'code':404,'is_successful':False},message="Issue {} doesn't exist".format(issue_id))

    return IssueResource