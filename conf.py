import os
import sys
import django

# Add the Django project root directory to the Python path
sys.path.insert(0, os.path.abspath('..'))  # Parent directory of conf.py
sys.path.insert(0, os.path.abspath('../candidate_site'))  # Django project package

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'candidate_site.settings'

# Initialize Django
django.setup()

# Project information
project = 'candidate_site'
copyright = '2025, Hlomelang Lipholo'
author = 'Hlomelang Lipholo'
release = '00.00.01'

# General configuration
extensions = []
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Options for HTML output
html_theme = 'alabaster'
html_static_path = ['_static']