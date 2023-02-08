import os
# Configuration file for the Sphinx documentation builder.

# -- Project information

# import furo

project = 'CRChub'
copyright = '2023, Zhixin Li (DFCI)'
author = 'Zhixin Li'

release = '1.0'
version = '1.0.0'

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

# List of arguments to be passed to the kernel that executes the notebooks:
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
]

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'pydata_sphinx_theme' # alabaster, furo, sphinx_rtd_theme, insipid
html_logo = "CRChub.png"
html_static_path = ['_static'] 
sphinx_rtd_size_width = "120%"

# html_css_files = ["custom.css"]
# html_style = 'custom.css'

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

# This is processed by Jinja2 and inserted before each notebook
nbsphinx_prolog = r"""
{% set docname = 'doc/' + env.doc2path(env.docname, base=None) %}
.. raw:: html
    <div class="admonition note">
      This page was generated from
      <a class="reference external" href="https://github.com/spatialaudio/nbsphinx/blob/{{ env.config.release|e }}/{{ docname|e }}">{{ docname|e }}</a>.
      Interactive online version:
      <span style="white-space: nowrap;"><a href="https://mybinder.org/v2/gh/spatialaudio/nbsphinx/{{ env.config.release|e }}?filepath={{ docname|e }}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="vertical-align:text-bottom"></a>.</span>
      <script>
        if (document.location.host) {
          let nbviewer_link = document.createElement('a');
          nbviewer_link.setAttribute('href',
            'https://nbviewer.org/url' +
            (window.location.protocol == 'https:' ? 's/' : '/') +
            window.location.host +
            window.location.pathname.slice(0, -4) +
            'ipynb');
          nbviewer_link.innerHTML = 'View in <em>nbviewer</em>';
          nbviewer_link.classList.add('reference');
          nbviewer_link.classList.add('external');
          document.currentScript.replaceWith(nbviewer_link, '.');
        }
      </script>
    </div>
.. raw:: latex
    \nbsphinxstartnotebook{\scriptsize\noindent\strut
    \textcolor{gray}{The following section was generated from
    \sphinxcode{\sphinxupquote{\strut {{ docname | escape_latex }}}} \dotfill}}
"""

# This is processed by Jinja2 and inserted after each notebook
nbsphinx_epilog = r"""
{% set docname = 'doc/' + env.doc2path(env.docname, base=None) %}
.. raw:: latex
    \nbsphinxstopnotebook{\scriptsize\noindent\strut
    \textcolor{gray}{\dotfill\ \sphinxcode{\sphinxupquote{\strut
    {{ docname | escape_latex }}}} ends here.}}
"""

mathjax3_config = {
    'tex': {'tags': 'ams', 'useLabelIds': True},
}

bibtex_bibfiles = ['references.bib']


