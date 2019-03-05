# cef_parser
Parses .cef (Category-Entry-Fields) files

How to use:

    import cefparser
    info = cefparser.parse_filename("myfile.cef")

.cef files are a human-friendly format for storing information. They look like this:

Category
======

Entry1
------
- field1: value
- field2: value

    Sub-Category
    =======
    Entry2
    -----
    - field1: value
    - field2: value
    - field3:

       Nested Entry
       -----------
       - field1: value
       - field2: value

    - field4: value


Entry3
----
- field1: value
- field2: value


New Category
======

Entry4
----
- field1:

    Nested Entry
    -----
    - field1: value
    - field2: value

- field2: value



And cefparser will turn the above into this:

    {'Category': {'Entry1': {'field1': 'value', 'field2': 'value'},
                  'Entry3': {'field1': 'value', 'field2': 'value'},
                  'Sub-Category': {'Entry2': {'field1': 'value',
                                              'field2': 'value',
                                              'field3': {'Nested Entry': {'field1':     'value',
                                                                          'field2':     'value'}},
                                              'field4': 'value'}}},
    'New Category': {'Entry4': {'field1': {'Nested Entry': {'field1': 'value',
                                                            'field2': 'value'}},
                                'field2': 'value'}}}

# Dependencies

None - `cefparser` does not even import any modules from the python standard library

# Installation

Download [the .zip from github](https://github.com/erose1337/cef_parser/archive/master.zip) and run `sudo python setup.py install` (`sudo` not applicable on Windows)

Installation via `pip` currently unavailable
