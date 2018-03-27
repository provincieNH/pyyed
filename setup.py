import os
from distutils.core import setup
from distutils.command.install import install as _install


setup(name='pyyed',
      version='1.0.1',
      description='A simple Python library to export graphs to the yEd graph editor, with some extra options',

      author='James Scott-Brown',

      author_email='james@jamesscottbrown.com',

      url='https://github.com/jamesscottbrown/pyyed',

      packages=['pyyed'],
      
      requires=[]
      )
