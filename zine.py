import os

from flask import Flask
from flask.ext.restful import Resource,Api,abort
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL'] if os.environ['DATABASE_URL'] else ''
db = SQLAlchemy(app)

# Defining SQLAlchemy Models

class Author(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))
    image_url = db.Column(db.String(255))

    def __init__(self, id, name,image_url):
        self.id = id
        self.name = name
        self.image_url = image_url

    def get_articles(self):
        article_list = []
        articles = Article.query.filter_by(author_id=self.id).all()
        for article in articles:
            article_dict = article.serialize()
            article_list.append({'id':article_dict['id'],'title':article_dict['title']})
        return article_list

    def get_contacts(self):
        contact_list = []
        contacts = Contact.query.filter_by(author_id=self.id).all()
        for contact in contacts:
            contact_dict = contact.serialize()
            contact_list.append(contact_dict)
        return contact_list

    def serialize(self):
        """
            Converts object to dict
        """
        author_dict = {
            'id' : self.id,
            'name' :self.name,
            'image_url' : self.image_url,
            'no_of_articles':len(self.get_articles()),
            'articles':self.get_articles(),
            'contacts':self.get_contacts()
        }
        return author_dict

    def __repr__(self):
        return '<Author %r>' % self.id

class Article(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    title = db.Column(db.String(255))
    tagline = db.Column(db.String(255))
    body = db.Column(db.Text)
    issue = db.Column(db.SmallInteger)
    link = db.Column(db.String(255))
    author_id = db.Column(db.String(255))

    def __init__(self, id, title,tagline,body,issue,link ,author_id):
        self.id = id
        self.title = title
        self.tagline = tagline
        self.body = body
        self.issue = issue
        self.link = link
        self.author_id = author_id

    def serialize(self):
        """
            Object to dict
        """
        article_dict = {
            'id':self.id,
            'title':self.title,
            'tagline':self.tagline,
            'body':self.body,
            'issue':self.issue,
            'link':self.link,
            'author_id':self.author_id
        }
        return article_dict

    def __repr__(self):
        return '<Article %r>' % self.title

class Contact(db.Model):
    author_id = db.Column(db.String(255),primary_key=True)
    email = db.Column(db.String(255))
    facebook = db.Column(db.String(255))
    twitter = db.Column(db.String(255))
    link = db.Column(db.String(255))

    def __init__(self, author_id, email,facebook,twitter,link):
        self.author_id = author_id
        self.email = email
        self.facebook= facebook
        self.twitter = twitter
        self.link = link

    def serialize(self):
        contact_dict={
            'email':self.email,
            'facebook':self.facebook,
            'twitter':self.twitter,
            'link':self.link
        }
        return contact_dict

    def __repr__(self):
        return '<Contact %r>' % self.author_id

# Defining resources for restful

def abort_if_article_doesnt_exist(article_id):
    article_list = []
    for article in Article.query.all():
        article_dict = article.serialize()
        article_list.append(article_dict['id'])
    if article_id not in article_list :
        abort(404,meta={'code':404,'is_successful':False},message="Article with id {} doesn't exist".format(article_id))

def abort_if_author_doesnt_exist(author_id):
    author_list = []
    for author in Author.query.all():
        author_dict = author.serialize()
        author_list.append(author_dict['id'])

    if author_id not in author_list:
        abort(404,meta={'code':404,'is_successful':False},message="Author with id {} doesn't exist".format(author_id))

class AuthorResource(Resource):
    def get(self,author_id):
        abort_if_author_doesnt_exist(author_id)
        return {
            "message":"Author with this id exist",
            "meta":{
                'is_successful':True,
                'code':200
            },
           "data": Author.query.filter_by(id=author_id).first().serialize()
        }

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

class Index(Resource):
    def get(self):
        return {'message': 'unofficial api of the blog http://thezine.biz'}


# Defining routes

api.add_resource(Index,'/')
api.add_resource(AuthorResource,'/v1/author/<string:author_id>')
api.add_resource(ArticleResource,'/v1/article/<string:article_id>')



if __name__ == '__main__':
    app.run(debug=True)
