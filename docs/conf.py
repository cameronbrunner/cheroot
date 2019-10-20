#! /usr/bin/env python3
# Requires Python 3.6+
"""Configuration of Sphinx documentation generator."""

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'jaraco.packaging.sphinx',
    'sphinx_tabs.tabs',
    'scm_tag_titles_ext',
]

master_doc = 'index'

scm_version_title_settings = {
    'scm': 'git',
    'date_format': '%d %b %Y',
}

github_url = 'https://github.com'
github_repo_org = 'cherrypy'
github_repo_name = 'cheroot'
github_repo_slug = f'{github_repo_org}/{github_repo_name}'
github_repo_url = f'{github_url}/{github_repo_slug}'
cp_github_repo_url = f'{github_url}/{github_repo_org}/cherrypy'

extlinks = {
    'issue': (f'{github_repo_url}/issues/%s', '#'),
    'pr': (f'{github_repo_url}/pull/%s', 'PR #'),
    'commit': (f'{github_repo_url}/commit/%s', ''),
    'cp-issue': (f'{cp_github_repo_url}/issues/%s', 'CherryPy #'),
    'cp-pr': (f'{cp_github_repo_url}/pull/%s', 'CherryPy PR #'),
    'gh': (f'{github_url}/%s', 'GitHub: '),
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'python2': ('https://docs.python.org/2', None),
    'cherrypy': ('https://docs.cherrypy.org/en/latest/', None),
    'trustme': ('https://trustme.readthedocs.io/en/latest/', None),
    'ddt': ('https://ddt.readthedocs.io/en/latest/', None),
    'pyopenssl': ('https://www.pyopenssl.org/en/latest/', None),
}

nitpicky = True

nitpick_ignore = [
    ('py:attr', 'cheroot.server.HTTPServer.bind_addr'),
    ('py:const', 'socket.SO_PEERCRED'),
    ('py:class', '_io.BufferedWriter'),
    ('py:class', '_io.BufferedReader'),
    ('py:class', 'cheroot.server.DropUnderscoreHeaderReader'),
    ('py:class', 'cheroot.server.HeaderReader'),
    ('py:class', 'cheroot.server.HTTPServer'),
    ('py:class', 'cheroot.test.helper.Controller'),
    ('py:class', 'cheroot.wsgi.Server'),
    ('py:func', 'cheroot._compat.extract_bytes'),
    ('py:meth', 'cheroot.server.HTTPServer.prepare'),
    ('py:meth', 'cheroot.server.HTTPServer.serve'),
    ('py:meth', 'cheroot.ssl.builtin.BuiltinSSLAdapter.wrap'),
    ('py:mod', 'cheroot._compat'),
    ('py:mod', 'cheroot.makefile'),
    ('py:mod', 'cheroot.server'),
    ('py:mod', 'cheroot.ssl.pyopenssl'),
    ('py:mod', 'cheroot.wsgi'),
]
