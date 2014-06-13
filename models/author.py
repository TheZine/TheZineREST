__author__ = 'ABHIJEET'

from models.contact import get_contact_model

def get_author_model(db):

    Contact = get_contact_model(db)

    class Author(db.Model):
        __tablename__ = 'Author'
        __table_args__ = {"extend_existing": True}
        id = db.Column(db.String(255), primary_key=True)
        name = db.Column(db.String(255))
        image_url = db.Column(db.String(255))

        def __init__(self, id, name,image_url):
            self.id = id
            self.name = name
            self.image_url = image_url

        def serialize_profile(self):
            """
                Converts object to dict
            """
            author_profile_dict = {
                'id' : self.id,
                'name' :self.name,
                'image_url' : self.image_url,
                'contacts' : Contact.query.filter_by(author_id=self.id).first().serialize()
            }
            return author_profile_dict

        def __repr__(self):
            return '<Author %r>' % self.id

    return Author
