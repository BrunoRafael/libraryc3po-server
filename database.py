# coding: utf-8

from google.appengine.ext import ndb

class Comment(ndb.Model):
	commentId: ndb.StringProperty()
	text: ndb.StringProperty()


#class User(ndb.Model):

class Book(ndb.Model):
    bookId = ndb.StringProperty()
    title = ndb.StringProperty(default="sem texto")
    authors = ndb.StructuredProperty(ndb.StringProperty(), repeated=True)
    description = ndb.StringProperty()
    imgUrl = ndb.StringProperty()
    create_datetime = ndb.DateTimeProperty(auto_now_add=True)
    comments = ndb.StructuredProperty(Comment, repeated=True)

def saveBook(bookId, title, authors, description, imgUrl):
	book = Book(id=bookId)
	book.title = title
	book.authors = authors
	book.description = description
	book.bookId= bookId
	book.imgUrl = imgUrl
	#message.create_datetime = dateTime.dateTime.now()
	book.put()

def saveComment(bookId, text):
	book = Book(id=bookId)

def getLibrary(hostUrl):
	books = Book.query()
    data = []
    for book in books:
        data.append({"url": "%s/books/%s" % (hostUrl, book.msgid)})
	
	return books

def getBook(bookId):
	book = Book()
   