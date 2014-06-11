

from tz import TZ , Article
import MySQLdb
import psycopg2

#Con = MySQLdb.Connect(host="localhost", port=3306, user="root", passwd="", db="tz")
Con = psycopg2.connect(host="ec2-54-243-49-82.compute-1.amazonaws.com" , port=5432 ,database='d1nrqcben47t9e', user='nhhixxyvtfnfhz',passwd="ZFVEs0WFj_ezDqWqtMI5OZsDV8")
Cursor = Con.cursor()

def store_contact(author_id ,contact):
	try:
		sql = "INSERT INTO Contact(author_id,email,facebook,twitter,link) VALUES('%s','%s','%s','%s','%s')"%(author_id,contact.email,contact.facebook,contact.twitter,contact.link)
		Cursor.execute(sql)
	except Exception as e:
		pass
	finally:
		print '{0} contact added '.format(author_id)
			

def store_author(author):
	try:
		sql = "INSERT INTO Author(id,name,image_url) VALUES('%s','%s','%s')"%(author.id,author.name,author.image)
		Cursor.execute(sql)
	except:
		pass
	finally:
		print '{0} author added '.format(author.name)
		store_contact(author.id,author.contact)
		

def store_article(article):
	sql = "INSERT INTO Article(id,title,tagline,body,issue,link,author_id) VALUES('{0}','{1}','{2}','{3}',{4},'{5}','{6}')"
	escape_body = MySQLdb.escape_string(str(article.body))
	try:
		Cursor.execute(sql.format(article.id,article.title,article.tagline,escape_body,article.issue,article.link,article.author.id))
	except Exception as e:
		pass
	finally:
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