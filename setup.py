from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='instapy',
      version=version,
      description="Python Library for the instapaper.com Simple API",
      long_description="""\
This is a python library to give access to instapaper's simple API but in the future I would like to include the more avanced API too.
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='instapaper',
      author='Adam Glenn',
      author_email='gekitsuu@gmail.com',
      url='https://github.com/gekitsuu/instapy',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
