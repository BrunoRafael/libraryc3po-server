# coding: utf-8
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os

import webapp2
import jinja2

import database
import datetime
import utils

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    variable_start_string='[[',
    variable_end_string=']]',
    autoescape=True)


class DocApiRequest(webapp2.RequestHandler):
    def get(self):
      self.response.headers.add_header('Access-Control-Allow-Origin', '*')
      self.response.headers['Content-Type'] = 'application/json'
      values = {'title': 'Documentation'}
      template = JINJA_ENVIRONMENT.get_template('doc.html')
      self.response.write(template.render(values))
 
class BookLibraryRequest(webapp2.RequestHandler):
   def get(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    response = []
    URLBASE = self.request.host_url
    books = database.getLibrary()
    for b in books:
      bookDict = b.to_dict(URLBASE)
      response.append(bookDict)
    self.response.write(utils.dataToJsonString(response))

class BookRequest(webapp2.RequestHandler):
    def get(self, bookId):
      self.response.headers.add_header('Access-Control-Allow-Origin', '*')
      self.response.headers['Content-Type'] = 'application/json'
      book = database.getBook(bookId);
      if book is None:
        self.response.set_status(400)
        self.response.write('{"msg":"Livro \'%s\' não encontrado", "error":404, "datetime":"%s"}' % (bookid, datetime.datetime.now().isoformat()))
        return

      URLBASE = self.request.host_url
      bookDict = book.to_dict(URLBASE);
      self.response.write(utils.dataToJsonString(bookDict).encode('utf-8'))

class BookRemoveRequest(webapp2.RequestHandler):
  def options(self, bookId):
    self.response.headers['Access-Control-Allow-Origin'] = '*'
    self.response.headers['Access-Control-Allow-Headers'] = '*'
    self.response.headers['Content-Type'] = 'application/json'
    self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
    self.response.write("options do removeBook funcionou!");
  
  def delete(self, bookId):
    database.remove(bookId);
    self.response.write(bookId);

class BookUpdateRequest(webapp2.RequestHandler):
    def put(self):
    	print("Aqui4")
    	pass

class BookAddRequest(webapp2.RequestHandler):
    def post(self):
      self.response.headers.add_header('Access-Control-Allow-Origin', '*')
      self.response.headers['Content-Type'] = 'application/json'
      print("Aqui5")
      pass

class BookSearchRequest(webapp2.RequestHandler):
  def get(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    print("Aqui6")
    pass

class BookAddCommentRequest(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    print("Aqui7")
    pass

class BookAddCommentRequest(webapp2.RequestHandler):
  def post(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    print("Aqui8")
    pass

class DeleteDatabaseRequest(webapp2.RequestHandler):
  def options(self):
    self.response.headers['Access-Control-Allow-Origin'] = '*'
    self.response.headers['Access-Control-Allow-Headers'] = '*'
    self.response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
    self.response.write("options funcionou!");

  def delete(self):
    database.removeAll('Bo');
    self.response.write("Livros removidos com sucesso!");

class BookLogListRequest(webapp2.RequestHandler):
  def get(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    database.listAllBooks()

class CleanDatabaseRequest(webapp2.RequestHandler):
  def get(self):
    self.response.headers.add_header('Access-Control-Allow-Origin', '*')
    self.response.headers['Content-Type'] = 'application/json'
    print("clean")
    utils.generateDatabase();
    self.response.write("Tudo salvo!");

app = webapp2.WSGIApplication([
    ('/', DocApiRequest),
    ('/books', BookLibraryRequest),
    ('/books/add/book', BookAddRequest),
    ('/books/list/book', BookLogListRequest),
    ('/books/update/book', BookUpdateRequest),
    ('/books/remove/(.*)', BookRemoveRequest),
    ('/books/search/book', BookSearchRequest),
    ('/books/add/comment', BookAddCommentRequest),
  	('/books/delete/database', DeleteDatabaseRequest),
  	('/books/clean/database', CleanDatabaseRequest),
  	('/books/(.*)', BookRequest),
], debug=True)