"""Provide an interface to the SimpleAPI"""

import urllib, urllib2

class AuthError(Exception):
	def __init__(self, error_message):
		self.parameter = error_message
	
	def __repr__(self):
		return self.parameter

	def __str__(self):
		return repr(self.paramtere)

class SimpleAPI():
	def __init__(self):
		self.auth_status = "Unauthenticated"

	def auth(self, username, password, jsonp=None):
		self.username = username
		self.password = password

		data = urllib.urlencode({ 'username': self.username, 'password': self.password})
		
		response = urllib2.urlopen('https://www.instapaper.com/api/authenticate', data)

		status = response.getcode()

		if status == 200:
			self.auth_status = "Authenticated"
		elif status == 403:
			self.auth_status = "Invalide username or password"
		elif status == 500:
			self.auth_status = "The service encountered an error. Please try again later"

	def create_article(self, url, title=None, selection=None, redirect=None, jsonp=None):
		if self.auth_status != "Authenticated":
			raise AuthError("Not currently authenticated")
		
		datadict = {
				'username': self.username,
				'password': self.password,
				'url': url
			}

		if title is not None: data['title'] = title
		if selection is not None: data['selection'] = selection
		if redirect is not None: data['redirect'] = redirect
		if jsonp is not None: data['jsonp'] = jsonp

		data = urllib.urlencode(datadict)
		response = urllib2.urlopen("https://www.instapaper.com/api/add", data)

		status = response.getcode()

		if status == 201:
			pass
		elif status == 400:
			pass
		elif status == 403:
			raise AuthError("Invalid username or password.")
		elif status == 500:
			pass	
		

