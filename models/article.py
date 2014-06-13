__author__ = 'ABHIJEET'

def get_article_model(db):

    class Article(db.Model):
        __tablename__ = 'Article'
        __table_args__ = {"useexisting": True}
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

    return Article
