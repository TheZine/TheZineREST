__author__ = 'ABHIJEET'

def get_author_model(db):

    class Author(db.Model):
        __tablename__ = 'Author'
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

        def serialize_profile(self):
            """
                Converts object to dict
            """
            author_profile_dict = {
                'id' : self.id,
                'name' :self.name,
                'image_url' : self.image_url
            }
            return author_profile_dict

        def serialize_articles(self):
            """
                Converts object to dict
            """
            author_articles_dict = {
                'no_of_articles':len(self.get_articles()),
                'articles':self.get_articles()
            }
            return author_articles_dict


        def serialize_contacts(self):
            """
                Converts object to dict
            """
            author_contacts_dict = {
                'contacts':self.get_contacts()
            }

            return author_contacts_dict

        def __repr__(self):
            return '<Author %r>' % self.id

    return Author
