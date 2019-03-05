from setuptools import setup

import api

options = {"name" : "cefparser",
           "version" : api.VERSION,
           "description" : "Parser for .cef (Category Entry Fields) files",
           "author" : "Ella Rose",
           "author_email" : "python_pride@protonmail.com",
           "packages" : ["cefparser"],
           "classifiers" : ["Development Status :: 4 - Beta",
                            "Intended Audience :: Developers",
                            "License :: OSI Approved :: MIT License",
                            "Programming Language :: Python :: 2.7",
                            "Topic :: Software Development :: Libraries :: Python Modules"]
                            }

if __name__ == "__main__":
    setup(**options)
