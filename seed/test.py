

from tz import TZ , Article
#import MySQLdb
import urlparse
import psycopg2
import os

#Con = MySQLdb.Connect(host="localhost", port=3306, user="root", passwd="", db="tz")
Con = result = urlparse.urlparse(os.environ['DATABASE_URL'])
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
Con = psycopg2.connect(database = database,user = username,password = password,host = hostname)
Cursor = Con.cursor()

def store_contact(author_id ,contact):
	try:
		sql = "INSERT INTO Contact(author_id,email,facebook,twitter,link) VALUES('%s','%s','%s','%s','%s')"%(author_id,contact.email,contact.facebook,contact.twitter,contact.link)
		Cursor.execute(sql)
	except Exception as e:
		print e
		pass
	finally:
		print '{0} contact added '.format(author_id)
			

def store_author(author):
	try:
		sql = "INSERT INTO Author(id,name,image_url) VALUES('%s','%s','%s')"%(author.id,author.name,author.image)
		Cursor.execute(sql)
	except Exception as e:
		print e
		pass
	finally:
		print '{0} author added '.format(author.name)
		store_contact(author.id,author.contact)
		

def store_article(article):
	sql = "INSERT INTO Article(id,title,tagline,body,issue,link,author_id) VALUES('{0}','{1}','{2}','{3}',{4},'{5}','{6}')"
	#escape_body = MySQLdb.escape_string(str(article.body))
	escape_body = article.body
	try:
		Cursor.execute(sql.format(article.id,article.title,article.tagline,escape_body,article.issue,article.link,article.author.id))
	except Exception as e:
		pass
	finally:
		print e
		print '{0} article added '.format(article.id)
		store_author(article.author)

for i in range(1,5):		
	articles  = TZ().get_articles(i)
	for article in articles:
		print 'fetching link %s'%article['link']
		article  = Article.fromLink(article['link'])
		store_article(article)
# sql = "SELECT * FROM Article"
# print Cursor.execute(sql)

Cursor.close()
Con.commit()
Con.close()