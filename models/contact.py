__author__ = 'ABHIJEET'

def get_contact_model(db):

    class Contact(db.Model):
        __tablename__ = 'Contact'
        __table_args__ = {"useexisting": True}
        author_id = db.Column(db.String(255),primary_key=True)
        email = db.Column(db.String(255))
        facebook = db.Column(db.String(255))
        twitter = db.Column(db.String(255))
        link = db.Column(db.String(255))

        def __init__(self, author_id,email,facebook,twitter,link):
            self.author_id = author_id
            self.email = email
            self.facebook = facebook
            self.twitter = twitter
            self.link = link

        def serialize(self):
            """
                Converts object to dict
            """
            contact_dict = {
                'email' : self.email,
                'facebook' :self.facebook,
                'twitter' : self.twitter,
                'link':self.link
            }
            return contact_dict

        def __repr__(self):
            return '<Author %r>' % self.email

    return Contact
