""" Provides parsing tools for .cef (Category-Entry-Field) files. """

__all__ = ["parse_filename", "parse", "CategoryError", "EntryError", "FieldError"]

class CategoryError(Exception): pass
class EntryError(Exception): pass
class FieldError(Exception): pass

def parse_filename(filename):
    """ usage: parse_filename(filename) => dict

        Parses the .cef file indicated by filename and returns a dictionary of the contents. """
    with open(filename, 'r') as _file:
        output = parse(_file)
    return output

def parse(_file):
    """ usage: parse(cef_file) => dict

        Parses a .cef file and returns a dictionary of the contents. """
    output = dict()
    indentation = 0
    category_levels = []
    last_section_type = ''
    while True:
        try:
            section_type, new_indentation = _determine_section_type(_file)
        except EOFError:
            if not all(output.values()):
                raise FieldError("Unable to find fields for entry '{}'".format(entry_name))
            return output
        if last_section_type == "entry" and section_type != "fields":
            raise FieldError("Unable to find fields for entry '{}'".format(entry_name))

        if section_type == "category":
            category_name = _parse_category(_file)
            if not new_indentation:
                output[category_name] = category = dict()
                category_levels = [category]
            elif new_indentation > indentation:
                indentation = new_indentation
                category_levels.append(category)
                category[category_name] = category = dict()
            elif new_indentation == indentation:
                category_levels[-2][category_name] = category = dict()
            else:
                assert new_indentation < indentation
                del category_levels[-1]
        elif section_type == "entry":
            if new_indentation < indentation:
                indentation = new_indentation
                del category_levels[-1]
                category = category_levels[-1]
            entry_name = _parse_entry(_file)
        else:
            fields = _parse_fields(_file, indentation)
            assert fields
            category[entry_name] = fields
        last_section_type = section_type

def _determine_section_type(_file):
    position = _file.tell()
    output = ''
    indentation = 0
    while True:
        line = _file.readline()
        if not line:
            raise EOFError()
        indentation = _determine_indentation(line)
        line = line.strip()
        _indicator = set(line)
        if _indicator == set('='):
            output = "category"
        elif _indicator == set('-'):
            output = "entry"
        elif ':' in line:
            output = "fields"
        else:
            continue
        if output:
            _file.seek(position)
            return output, indentation

def _determine_indentation(line):
    indent_character = line[0]
    if indent_character not in (' ', '\n'):
        return 0
    else:
        for indentation, character in enumerate(line):
            if character != indent_character:
                return indentation

def _parse_category(_file):
    category = ''
    while True:
        line = _file.readline()
        if not line:
            raise EOFError()
        line = line.strip()
        if not line:
            continue
        if not category:
            if set(line) == set('='):
                raise CategoryError("Unable to find category name before indicator line")
            else:
                category = line
        else:
            return category

def _parse_entry(_file):
    entry = ''
    while True:
        line = _file.readline()
        if not line:
            raise EOFError()
        line = line.strip()
        if not line:
            continue
        if not entry:
            if set(line) == set('-'):
                raise EntryError("Entry name not found before indicator line")
            else:
                entry = line
        else:
            return entry

def _parse_fields(_file, indentation):
    output = dict()
    while True:
        position = _file.tell()
        line = _file.readline()
        if not line:
            return output

        if not line.strip():
            continue

        line_indentation = _determine_indentation(line)
        if line_indentation < indentation:
            _file.seek(position)
            return output
        if line_indentation > indentation:
            indentation = line_indentation

        line = line.strip()
        if ':' not in line:
            _file.seek(position)
            return output
        field, value = line.split(':', 1)
        field = field.replace('-', '', 1).strip()
        value = value.strip()
        if not value:
            entry_name = _parse_entry(_file)
            fields = _parse_fields(_file, indentation)
            value = {entry_name: fields}
        output[field] = value


#class CEF_File(object):
#
#    def __init__(self, filename):
#        self.filename = filename
#        self.info = parse_filename(filename)
#
#    def _get_categories(self):
#        return self.info.keys()
#    categories = property(_get_categories)
