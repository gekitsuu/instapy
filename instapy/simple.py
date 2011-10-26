"""Provide an interface to the SimpleAPI"""

import urllib, urllib2

class AuthError(Exception):
	def __init__(self, error_message):
		self.parameter = error_message
	
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

		if response.getcode() == 200:
			self.auth_status = "Authenticated"
		elif response.getcode() == 403:
			self.auth_status = "Invalide username or password"
		elif response.getcode() == 500:
			self.auth_status = "The service encountered an error. Please try again later"

	def create_article(self, url, title=None, selection=None, redirect=None, jsonp=None):
		if self.auth_status != "Authenticated":
			raise AuthError("Not currently authenticated")
			return
		
		
