VERSION = "0.1.0"
LANGUAGE = "python"
PROJECT = "cefparser"

API = {"cefparser.parse_filename" : {"arguments" : ("filename str", ),
                                     "returns" : ("dict", ),
                                     "exceptions" : ("IOError",
                                                     "cefparser.CategoryError",
                                                     "cefparser.EntryError",
                                                     "cefparser.FieldError")},
       "cefparser.parse" : {"arguments" : ("file object", ),
                            "returns" : ("dict", ),
                            "exceptions" : ("IOError", "cefparser.CategoryError",
                                            "cefparser.EntryError",
                                            "cefparser.FieldError")}
      }
