# coding: utf-8

from google.appengine.ext import ndb
import datetime
import logging

class Comment(ndb.Model):
	authorId= ndb.StringProperty()
	text= ndb.StringProperty()

#class User(ndb.Model):

class Book(ndb.Model):
	bookId= ndb.StringProperty()
	title = ndb.StringProperty(default="sem titulo")
	authors = ndb.StringProperty(repeated=True)
	description = ndb.StringProperty()
	imgUrl = ndb.StringProperty()
	create_datetime = ndb.DateTimeProperty(auto_now_add=True)
	comments = ndb.StructuredProperty(Comment, repeated=True)

	def to_dict(self, URLBASE=""):
		data = super(Book, self).to_dict()
		data["url"] = "%s/books/%s" % (URLBASE, self.bookId)
		return data

def saveBook(bookId, title, authors, description, imgUrl):
	book = Book(id=bookId)
	book.title = title
	book.authors = authors
	book.description = description
	book.bookId= bookId
	book.imgUrl = imgUrl
	book.create_datetime = datetime.datetime.now()
	logging.debug(book)
	book.put();

def saveLibrary(library):
	ndb.put_multi(library);

def saveComment(bookId, authorId, text):
	book = Book(id=bookId)
	book.comments.append(Comment(authorId=authorId, text=text))
	book.put();

def getLibrary():
	return Book.query().fetch();

def getBook(bookId):
	return Book.get_by_id(bookId)

def removeAll(type):
	if(type == 'Book'):
		ndb.delete_multi(
	    	Book.query().fetch(keys_only=True)
		)
def listAllBooks():
	result = Book.query();
	for book in result:
		logging.info(book)
   	