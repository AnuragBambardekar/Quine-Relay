fsharp = [
[   "let data = [",
    "]", ],
[   "let q, space, separator = string(char 34), string(char 32), string(char sep)",
    "for i in a..b-1 do",
    "   System.Console.WriteLine(data.[i])",
    "for i in 0..data.Length-1 do",
    "   System.Console.WriteLine(space + q + data.[i] + q + separator)",
    "for i in b..c-1 do",
    "   System.Console.WriteLine(data.[i])", ] ]

java = [
[   "public class quine {",
    " public static void main(String[] args) {",
    "  String[] data = {",
    "  };", ],
[   "  char q = (char) 34; char space = (char) 32; char separator = (char) sep;",
    "  for (int i = a; i < b; i++)",
    "    System.out.println(data[i]);",
    "  for (int i = 0; i < data.length; i++)",
    "    System.out.println(String.valueOf(space) + q + data[i] + q + separator);",
    "  for (int i = b; i < c; i++)",
    "    System.out.println(data[i]);",
    " }",
    "}", ] ]

python = [
[   "data = [",
    "]", ],
[   "q, space, separator = chr(34), chr(32), chr(sep)",
    "for k in range(a,b):",
    "  print(data[k])",
    "for d in data:",
    "  print(space + q + d + q + separator)",
    "for k in range(b,c):",
    "  print(data[k])", ] ]


facts = { "fsharp"  :{"boundary":1 , "template":fsharp ,  "separator":59 ,
                     "size": 1 + len(fsharp[0]) + len(fsharp[1]),
                     "parms": "let a, b, c, sep = {}, {}, {}, {}"},

         "java"    :{"boundary":3  ,"template":java ,  "separator":44 ,
                     "size": 1 + len(java[0]) + len(java[1]),
                     "parms": "  int a={}; int b={}; int c={}; int sep={};"},

         "python"  :{"boundary":1 , "template":python,  "separator":44 ,
                     "size": 1 + len(python[0]) + len(python[1]),
                     "parms": "a, b, c, sep = {}, {}, {}, {}"}, }

supported_langs = facts.keys()

def boundary(lang):
    assert lang in supported_langs
    return facts[lang]["boundary"]

def template(lang):
    assert lang in supported_langs
    return facts[lang]["template"]

def parameters(lang):
    assert lang in supported_langs
    return facts[lang]["parms"]

def separator(lang):
    assert lang in supported_langs
    return facts[lang]["separator"]

def size(lang):
    assert lang in supported_langs
    return facts[lang]["size"]