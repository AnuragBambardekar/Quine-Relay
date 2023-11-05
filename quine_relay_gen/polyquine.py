#!/usr/bin/python3
import sys, itertools
from lang_data import boundary, parameters, separator, size, template, supported_langs

def concat(lol):
    ''' Concatenate a list of lists. '''
    return list(itertools.chain.from_iterable(lol))

def partial_sums(nums):
    '''Compute partial sums of list of numbers, e.g. [1,2,3,4] -> [0,1,3,6,10]'''
    sum = 0
    result = [0]
    for n in nums:
        sum += n
        result.append(sum)
    return result

def quote(line, separator):
    q = '"'
    return ' ' + q + line + q + separator

def populate_templates(langs):
    ''' Compute required offsets per language choices, inject them into raw templates. '''
    offsets = partial_sums([ size(l) for l in langs[:-1] ])
    templates = []
    num_langs = len(langs)
    for k in range(num_langs):
        langX = langs[k]
        langY = langs[(k+1) % num_langs]
        a = offsets[(k+1) % num_langs]
        b = a + boundary(langY)
        c = a + size(langY)
        parms = parameters(langX).format(a, b, c, separator(langY))
        top,bottom = template(langX)
        templates.append(top + [parms] + bottom)
    return templates[0],concat(templates)

def polyquine(langs):
    ''' Generate a polyquine in the specified languages. '''
    code,payload = populate_templates(langs)
    bnd = boundary(langs[0])
    sep = chr(separator(langs[0]))
    data = [quote(line, sep) for line in payload]
    return code[:bnd] + data + code[bnd:]

def usage():
    msg = "Usage: polyquine lang_1 ... lang_n where each lang argumment is one of {}."
    print(msg.format(", ".join(supported_langs)))
    print("Example:  polyquine java python fsharp java")
    print("At least one language is required, repetitions are allowed.")

if __name__ == "__main__" :
    try:
        assert len(sys.argv) > 0
        langs = sys.argv[1:]
        assert len(langs) > 0
        assert set(langs).issubset(set(supported_langs))
    except:
        usage()
        sys.exit(0)
    for line in polyquine(langs):
        print(line)