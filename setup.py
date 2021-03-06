#! /usr/bin/env python
#
from distutils.core import setup
from ginga.version import version

setup(
    name = "Ginga",
    version = version,
    author = "Eric Jeschke",
    author_email = "eric@naoj.org",
    description = ("An astronomical (FITS) image viewer."),
    license = "BSD",
    keywords = "FITS image viewer astronomy",
    url = "http://ejeschke.github.com/ginga",
    packages = ['ginga', 'ginga.gtkw', 'ginga.gtkw.plugins', 'ginga.gtkw.tests',
                'ginga.qtw', 'ginga.qtw.plugins', 'ginga.qtw.tests',
                'ginga.misc', 'ginga.misc.plugins',
                'ginga.icons', 'ginga.util',
                'ginga.doc'],
    package_data = { 'ginga.icons': ['*.ppm', '*.png'],
                     'ginga.doc': ['manual/*.html'],
                     'ginga.gtkw': ['gtk_rc']
                     },
    scripts = ['scripts/ginga'],
    classifiers = [
        "Development Status :: 5 - Stable",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
)

