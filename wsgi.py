import sys
import os
from flask import Flask

# Add your project directory to the sys.path
project_home = '/home/mustafizfx/mysite'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set the FLASK_APP environment variable if needed
os.environ['FLASK_APP'] = 'app.py'

from app import app as application  # noqa
