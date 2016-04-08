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
import datetime
import json

import webapp2
import jinja2

import database
import utils

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    variable_start_string='[[',
	variable_end_string=']]',
    autoescape=True)


class DocApiRequest(webapp2.RequestHandler):
    def get(self):
		values = {
			'title': 'Documentation'
		}
		template = JINJA_ENVIRONMENT.get_template('doc.html')
		self.response.write(template.render(values));
 
class BookLibraryRequest(webapp2.RequestHandler):
   def get(self):
   		messages = database.getLibrary()
        self.response.write(utils.dataTojson(data).encode('utf-8'))
        self.response.write();

class BookRequest(webapp2.RequestHandler):
    def get(self):
    	pass

class BookRemoveRequest(webapp2.RequestHandler):
    def delete(self):
    	pass

class BookUpdateRequest(webapp2.RequestHandler):
    def put(self):
    	pass

class BookAddRequest(webapp2.RequestHandler):
    def post(self):
    	pass
class BookSearchRequest(webapp2.RequestHandler):
	def get(self):
		pass

class BookAddCommentRequest(webapp2.RequestHandler):
	def post(self):
		pass

class BookAddCommentRequest(webapp2.RequestHandler):
	def post(self):
		pass

class DeleteDatabaseRequest(webapp2.RequestHandler):
	def post(self):
		pass

class CleanDatabaseRequest(webapp2.RequestHandler):
	def post(self):
		pass

app = webapp2.WSGIApplication([
    ('/', DocApiRequest),
    ('/books', BookLibraryRequest),
    ('/books/.*', BookRequest),
    ('/books/addBook', BookAddRequest),
    ('/books/updateBook', BookUpdateRequest),
    ('/books/removeBook', BookRemoveRequest),
    ('/books/searchBooks', BookSearchRequest),
    ('/books/addComment', BookAddCommentRequest),
	('/books/delete/database', DeleteDatabaseRequest),
	('/books/clean/database', CleanDatabaseRequest)
], debug=True)

utils.generateDatabase();