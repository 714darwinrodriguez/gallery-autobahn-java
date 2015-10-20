# -*- coding: utf-8 -*-
#
# AutobahnAndroid documentation build configuration file, created by
# sphinx-quickstart on Thu Mar 20 14:07:35 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import sphinx_bootstrap_theme


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'javasphinx',
    'sphinx.ext.ifconfig',
    'sphinxcontrib.spelling'
]

spelling_lang = 'en_US'
spelling_show_suggestions = False
spelling_word_list_filename = 'spelling_wordlist.txt'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'AutobahnAndroid'
copyright = None
# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.5.2'
# The full version, including alpha/beta/rc tags.
release = '0.5.2'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'work']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
# pygments_style = 'flask_theme_support.FlaskyStyle'
# pygments_style = 'pastie'
# pygments_style = 'monokai'
# pygments_style = 'colorful'
# pygments_style = 'trac'


# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#html_theme = 'default'
# sys.path.append(os.path.abspath('_themes'))
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

## Sphinx-Bootstrap Theme
##
## http://sphinx-bootstrap-theme.readthedocs.org/en/latest/README.html
##
if sphinx_bootstrap_theme:

   html_theme = 'bootstrap'
   html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
   # (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
   # Path should be relative to the ``_static`` files directory.

   html_theme_options = {
       # Navigation bar title. (Default: ``project`` value)
       'navbar_title': " ",

       # Tab name for entire site. (Default: "Site")
       'navbar_site_name': "Site",

       # A list of tuples containing pages or urls to link to.
       # Valid tuples should be in the following forms:
       #    (name, page)                 # a link to a page
       #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
       #    (name, "http://example.com", True) # arbitrary absolute url
       # Note the "1" or "True" value above as the third argument to indicate
       # an arbitrary url.
       'navbar_links': [
           #("Examples", "examples"),
           #("Link", "http://example.com", True),
       ],

       # Render the next and previous page links in navbar. (Default: true)
       'navbar_sidebarrel': True,

       # Render the current pages TOC in the navbar. (Default: true)
       'navbar_pagenav': True,

       # Tab name for the current pages TOC. (Default: "Page")
       #'navbar_pagenav_name': "Page",

       # Global TOC depth for "site" navbar tab. (Default: 1)
       # Switching to -1 shows all levels.
       'globaltoc_depth': 1,

       # Include hidden TOCs in Site navbar?
       #
       # Note: If this is "false", you cannot have mixed ``:hidden:`` and
       # non-hidden ``toctree`` directives in the same page, or else the build
       # will break.
       #
       # Values: "true" (default) or "false"
       'globaltoc_includehidden': "true",

       # HTML navbar class (Default: "navbar") to attach to <div> element.
       # For black navbar, do "navbar navbar-inverse"
       #'navbar_class': "navbar navbar-inverse",
       'navbar_class': "navbar",

       # Fix navigation bar to top of page?
       # Values: "true" (default) or "false"
       'navbar_fixed_top': "true",

       # Location of link to source.
       # Options are "nav" (default), "footer" or anything else to exclude.
       'source_link_position': "nav",

       # Bootswatch (http://bootswatch.com/) theme.
       #
       # Options are nothing with "" (default) or the name of a valid theme
       # such as "amelia" or "cosmo".
       'bootswatch_theme': "",

       # Choose Bootstrap version.
       # Values: "3" (default) or "2" (in quotes)
       'bootstrap_version': "3",
   }

# if sphinx_rtd_theme:
#    html_theme = "sphinx_rtd_theme"
#    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# additional variables which become accessible in the template engine's context for
# all pages
# html_context = {'widgeturl': 'http://192.168.1.147:8090/widget'}
html_context = {
   #'widgeturl': 'https://demo.crossbar.io/clandeckwidget'
   #'widgeturl': 'http://127.0.0.1:8090/widget'
   'widgeturl': None,
   'no_network': False,
   #'cstatic': 'http://127.0.0.1:8888',
   'cstatic': '//tavendo-common-static.s3-eu-west-1.amazonaws.com',
}


# (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
# Path should be relative to the ``_static`` files directory.
html_logo = None

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

html_sidebars = {
   '**':       ['side-primary.html']
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'AutobahnAndroid'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'AutobahnAndroid.tex', u'AutobahnAndroid Documentation',
   u'Tavendo GmbH', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'autobahnandroid', u'AutobahnAndroid Documentation',
     [u'Tavendo GmbH'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'AutobahnAndroid', u'AutobahnAndroid Documentation',
   u'Tavendo GmbH', 'AutobahnAndroid', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}

javadoc_url_map = {
    'com.netflix.curator' : ('http://netflix.github.com/curator/doc', 'javadoc'),
    'org.springframework' : ('http://static.springsource.org/spring/docs/3.1.x/javadoc-api/', 'javadoc'),
    'org.springframework.data.redis' : ('http://static.springsource.org/spring-data/data-redis/docs/current/api/', 'javadoc')
}



rst_epilog = """
.. |ab| replace:: Autobahn\|Android
.. |Ab| replace:: **Autobahn**\|Android
.. _Autobahn: http://autobahn.ws
.. _AutobahnPython: **Autobahn**\|Python
.. _AutobahnJS: **Autobahn**\|JS
.. _WebSocket: http://tools.ietf.org/html/rfc6455
.. _RFC6455: http://tools.ietf.org/html/rfc6455
.. _WAMP: http://wamp.ws/
.. _WAMPv1: http://wamp.ws/spec/wamp1/
.. _WAMPv2: https://wamp-proto.org/spec/
.. _AutobahnTestsuite: http://autobahn.ws/testsuite
"""

# rst_prolog = """
# .. container:: topnav

#    :doc:`Overview </index>` :doc:`Getting Started </gettingstarted>`  :doc:`/examples` :doc:`API Reference </_gen/packages>` :doc:`/table_of_contents`

# """


# http://stackoverflow.com/questions/5599254/how-to-use-sphinxs-autodoc-to-document-a-classs-init-self-method
autoclass_content = 'both'

autodoc_member_order = 'bysource'
