# Configuration file for the Sphinx documentation builder.
# -- Project information
# import furo

project = 'CRChub'
copyright = '2023, Zhixin Li (DFCI)'
author = 'Zhixin Li'

version = '0.4.9'
release = version

# -- General configuration
master_doc = 'index'

extensions = [
    #"myst_nb", # pip install myst_nb
    "nbsphinx", # pip install nbsphinx
    "myst_parser", # pip install myst-parser
    "sphinx_gallery.load_style",
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_copybutton',
    'sphinx_panels',
    'sphinx.ext.viewcode',
    # theme
    'sphinx_rtd_size',
    'ipykernel', # for kernels
]

nbsphinx_kernel_name = 'python'
nbsphinx_execute = 'never' # don't check R code

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'pydata_sphinx_theme' # alabaster, furo, sphinx_rtd_theme, insipid
html_logo = "CRChub.png"
html_static_path = ['_static'] 
sphinx_rtd_size_width = "120%"

html_css_files = ["custom.css"]
# html_style = 'custom.css' # not good

# # for sphinx_gallery
# sphinx_gallery_conf = {
#     'thumbnail_size': (150, 150),
#     'line_numbers': True,
#     'default_thumb_file': 'CRChub.png',
#     'nested_sections' : False,
# }

logo_only = True
display_version = False
analytics_id = 'G-K4WP6HMMF7'
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True

# html_theme_options = {
#    'analytics_id': 'G-K4WP6HMMF7',  #  Provided by Google in your dashboard, UA-253317179-2
    # 'github_banner' : 'false',
    # 'github_button' : 'false',
    # 'github_user': 'leezx',
    # 'github_repo': 'bt3m-multimodal',
# }

# -- Options for EPUB output
epub_show_urls = 'footnote'

# advanced skills
# https://nbsphinx.readthedocs.io/en/latest/gallery/gallery-with-nested-documents.html
