# -- General configuration -----------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
]

release = "0.19.2"

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'pyramid_zipkin'
copyright = u'2019, Yelp, Inc'

exclude_patterns = []

pygments_style = 'sphinx'


# -- Options for HTML output ---------------------------------------------

html_theme = 'sphinx_rtd_theme'

htmlhelp_basename = 'zipkin-pydoc'


intersphinx_mapping = {
    'http://docs.python.org/': None
}
