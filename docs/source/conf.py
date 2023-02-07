# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Computational Biochemistry'
copyright = '2023, Folorunsho Bright Omage n\ Departamento de Bioquímica e Biologia Molecular (UFSM) Programas de Pós-Graduação em Ciências Biológicas: Bioquímica Toxicológica - PPGBTox Programa de Pós-Graduação em Educação em Ciências: Química da Vida e Saúde - PPGECQVS Centro de Ciências Naturais e Exatas - CCNE 97105-900 Santa Maria RS Brasil'
author = 'Folorunsho Bright Omage, n\ Prof Laura Orian, Prof João Batista Teixeira da Rocha '

release = '0.1'
version = '0.1.0'

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

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
