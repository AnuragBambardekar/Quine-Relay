import sys
from lang_data import boundary, separator, template, supported_langs

def quote(line, separator):
    q = '"'
    return ' ' + q + line + q + separator

def quine(lang):
    code = template(lang)
    bnd = boundary(lang)
    sep = separator(lang)
    data = [quote(line, sep) for line in code]
    return code[:bnd] + data + code[bnd:]

def usage():
    msg = "Usage: quine_generator lang, where lang is one of {0}."
    print(msg.format(", ".join(list(supported_langs))))
    print("Example:  quine_generator python")

if __name__ == "__main__" :
    try:
        assert len(sys.argv) > 0
        lang = sys.argv[1]
        assert lang in supported_langs
    except:
        usage()
        sys.exit(0)
    for line in quine(lang):
        print(line)