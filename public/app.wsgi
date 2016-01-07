import os
import sys 

from os.path import dirname, realpath

project_path = dirname(dirname(realpath(__file__)))

activate_this = project_path + '/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, project_path + '/application')

from application import app as application
