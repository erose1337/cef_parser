if __name__ == "__main__":
    import cefparser
    import pprint
    output = cefparser.parse_filename("./test.cef")
    pprint.pprint(output)
    try:
        cefparser.parse_filename("./brokentest1.cef")
    except cefparser.CategoryError:
        pass
    else:
        print("CategoryError unit test failed")

    try:
        cefparser.parse_filename("./brokentest2.cef")
    except cefparser.EntryError:
        pass
    else:
        print("EntryError unit test failed")

    try:
        cefparser.parse_filename("./brokentest3.cef")
    except cefparser.FieldError:
        pass
    else:
        print("FieldError unit test failed")
