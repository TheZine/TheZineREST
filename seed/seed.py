

from tz import TZ , Article as ArticleClass
from zine import db,Author,Article,Contact

session = db.session()

def store_contact(author_id ,contact):
	try:
		contact = Contact(author_id,contact.email,contact.facebook,contact.twitter,contact.link)
		session.add(contact)
	except Exception as e:
		print e
		pass
	finally:
		print '{0} contact added '.format(author_id)
			

def store_author(author):
	try:
		author = Author(author.id,author.name,author.image)
		session.add(author)
	except Exception as e:
		print e
		pass
	finally:
		print '{0} author added '.format(author.name)
		store_contact(author.id,author.contact)
		

def store_article(article):
	escape_body = 'dummy body'
	try:
		article = Article(article.id,article.title,article.tagline,escape_body,article.issue,article.link,article.author.id)
		session.add(article)
	except Exception as e:
		print e
		pass
	finally:
		print '{0} article added '.format(article.id)
		store_author(article.author)

for i in range(1,5):		
	articles  = TZ().get_articles(i)
	for article in articles:
		print 'fetching link %s'%article['link']
		article  = ArticleClass.fromLink(article['link'])
		store_article(article)

session.commit()