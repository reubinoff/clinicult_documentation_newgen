# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Clinicult"
copyright = "2021, Clinicult"
author = "Moshe Reubinoff"

release = "0.2"
version = "1.0.1"

# -- General configuration
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"
html_static_path = ["html/_static"]
html_logo = "html/_static/clinicult.svg"
html_theme_options = {
    "logo_only": True,
}

pygments_style = "sphinx"

# -- Options for EPUB output
epub_show_urls = "footnote"

autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}
