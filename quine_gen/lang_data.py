fsharp = [
    "let data = [",
    #---- boundary ----#
    "]",
    "let boundary = 1",
    "let a, b, c = 0, boundary, data.Length",
    "let quote, space, separator = string(char 34), string(char 32), string(char 59)",
    "for k in a..b-1 do",
    "   System.Console.WriteLine(data.[k])",
    "for d in data do",
    "   System.Console.WriteLine(space + quote + d + quote + separator)",
    "for k in b..c-1 do",
    "   System.Console.WriteLine(data.[k])"
    ]

# Notice the class name. Java ties the class name to the file name.
# The test machinery wants to call the quine 'quine.java', hence
# the chosen class name.
java = [
    "public class quine {",
    " public static void main(String[] args) {",
    "  String[] data = {",
    #---- boundary ----#
    "  };",
    "  int boundary = 3;",
    "  int a = 0; int b = boundary; int c = data.length;" ,
    "  char quote = (char) 34; char space = (char) 32; char separator = (char) 44;",
    "  for (int k = a; k < b; k++)",
    "    System.out.println(data[k]);",
    "  for (String line : data)",
    "    System.out.println(String.valueOf(space) + quote + line + quote + separator);",
    "  for (int k = b; k < c; k++)",
    "    System.out.println(data[k]);",
    " }",
    "}"
    ]


python = [
    "data = [",
    #---- boundary ----#
    "]",
    "boundary = 1",
    "a, b, c = 0, boundary, len(data)",
    "quote, space, separator = chr(34), chr(32), chr(44)",
    "for k in range(a,b):",
    "  print(data[k])",
    "for d in data:",
    "  print(space + quote + d + quote + separator)",
    "for k in range(b,c):",
    "  print(data[k])"
    ]


facts = { "fsharp"   :{"boundary":1 , "template":fsharp  , "separator":';' },
          "java"     :{"boundary":3 , "template":java    , "separator":',' },
          "python"   :{"boundary":1 , "template":python  , "separator":',' },
        }
supported_langs = facts.keys()

def boundary(lang):
    assert lang in supported_langs
    return facts[lang]["boundary"]

def separator(lang):
    assert lang in supported_langs
    return facts[lang]["separator"]

def template(lang):
    assert lang in supported_langs
    return facts[lang]["template"]