instapy
=============

This is a python library to give access to instapaper's simple API but in the future I would like to include the more avanced API too.

Example
-------

from instapy.simple import SimpleAPI

a = SimpleAPI()
a.auth('username', 'password')
a.create_article('http://example.com')
