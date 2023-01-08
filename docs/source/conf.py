# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'bt3m-multimodal'
copyright = '2023, Zhixin Li (DFCI)'
author = 'Zhixin Li'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'alabaster'

html_theme_options = {
    'analytics_id': 'UA-253317179-1',  #  Provided by Google in your dashboard, G-B2C3KPTYYZ
    'logo': 'logo.png',
    'github_banner' : 'true',
    'github_button' : 'true',
    'github_user': 'leezx',
    'github_repo': 'bt3m-multimodal',
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
