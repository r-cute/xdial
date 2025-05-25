# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'xDial User Manual'
copyright = '2024, hyan'
author = 'hyan'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import sys, os
sys.path.append(os.path.abspath('../exts')) # relative to [lang]/conf.py

extensions = ['sphinx.ext.githubpages', 'sphinx.ext.autosectionlabel', 'xref']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_css_files = ['custom.css']
html_js_files = ['custom.js']

html_theme_options = {
    'collapse_navigation': False
}

html_context = {
    'display_github': False
}

html_show_sourcelink = False
