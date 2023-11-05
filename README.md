# Attempting to build a Quine Relay

Let's build a Quine Relay

## How to build a quine
A quine is a program P such that Eval P = P. That is, evaluating the program produces the original program, or at least a textual representation thereof. A quine relay is a sequence of programs, say [P, Q, R] such that

- Eval P = Q
- Eval Q = R
- Eval R = P

The exact number of programs does not matter. What matters is that the programs cyclically produce one another. The programs are not required to be written in the same language; it is more interesting when they are not. The Eval functions are taken to be appropriate for the languages at hand. If P, Q, and R are written in different languages, we would require distinct Eval functions, say python, ruby, and lua interpreters.

## Generate ordinary quines? Maybe just 1 quine

### Let's build a Quine in Python
- Write the quine script and execute and see it print the program again.
- You can confirm whether the program is indeed a quine by using the `diff` tool (in Linux):

Execute:
```cmd
python simple_quine.py

data = [
    "data = [",
    "]",
    "q = chr(34)",
    "boundary = 1",
    "for d in data[:boundary]:",
    "    print(d)",
    "for d in data:",
    "    print('    ' + q + d + q + ',')",
    "for d in data[boundary:]:",
    "    print(d)",
]
q = chr(34)
boundary = 1
for d in data[:boundary]:
    print(d)
for d in data:
    print('    ' + q + d + q + ',')
for d in data[boundary:]:
    print(d)
```
To confirm, whether you indeed made a Quine, we can use diff (in Linux) tool to check.
```cmd
diff -s simple_quine.py =(python simple_quine.py)
```

### Let's build a Quine in F#
#### Install F# with Visual Studio Code
Install the .NET SDK and Visual Studio Code.

Select the Extensions icon and search for "Ionide":

The only plugin required for F# support in Visual Studio Code is Ionide-fsharp (Ionide for F#)

**Creating my first F# code:**
```cmd
dotnet new console -lang "F#" -o FirstIonideProject
cd FirstIonideProject
```

**Now, write the script to convert a word to piglatin.**

To execute the script, Highlight the entire function (it should be 11 lines long). Once it's highlighted, hold the Alt key and hit Enter.

This did three things:

- It started the FSI process.
- It sent the code you highlighted over to the FSI process.
- The FSI process evaluated the code you sent over.

```cmd
- let toPigLatin (word: string) =
-     let isVowel (c: char) =
-         match c with
-         | 'a' | 'e' | 'i' |'o' |'u'
-         | 'A' | 'E' | 'I' | 'O' | 'U' -> true
-         |_ -> false
-
-     if isVowel word[0] then
-         word + "yay"
-     else
-         word[1..] + string(word[0]) + "ay";;
val toPigLatin: word: string -> string

> toPigLatin "banana";;
val it: string = "ananabay"
```

#### Great! Let's now build a quine in F#
- Write the same script we wrote earlier in Python, however keeping in mind the syntax differences from Python.
- Make sure to call your program quine.fsx rather than quine.fs. The F# compiler considers an fs file to be program and an fsx file to be a script; it treats them differently. For our purpose the script is easier to work with.

Then execute the code (Select the code and hit Alt+Enter)

Execute: <br>
```cmd
dotnet fsi simple_quine.fsx

let data = [
 "let data = [";
 " ]";
 "let q = string(char 34)";
 "let semicolon = string(char 59)";
 "let space = string(char 32)";
 "let boundary = 1";
 "for d in data[..boundary-1] do";
 "   System.Console.WriteLine(d)";
 "for d in data do";
 "   System.Console.WriteLine(space + q + d + q + semicolon)";
 "for d in data[boundary..] do";
 "   System.Console.WriteLine(d)";
 ]
let q = string(char 34)
let semicolon = string(char 59)
let space = string(char 32)
let boundary = 1
for d in data[..boundary-1] do
   System.Console.WriteLine(d)
for d in data do
   System.Console.WriteLine(space + q + d + q + semicolon)
for d in data[boundary..] do
   System.Console.WriteLine(d)
```

You can check (in Linux) whether you indeed made a Quine.
```cmd
diff -s quine.fsx =(dotnet fsi quine.fsx)
```

## Building a Quine Generator
- So far we have seen a pair of quines, **one in python and one in F#**. Each consists of data and logic used to control the printing of said data. 
- The plan here is to repackage the data and the logic. A single python program will handle the printing logic across all languages. The data representing the various quines will live in in python lists, one per language.

Write the scripts (**gen_quine** and **lang_data**) and execute (code is here: https://codeberg.org/drcabana/quines/src/branch/main/src)

```cmd
python .\quine_generator.py python> generated_quine.py
python quine_generator.py java > quine.java
python quine_generator.py fsharp > generated_quine.fsx
```

**we can also make a shell script to automate this, but for my convenience I chose not to do that**
#---- Generate the specified quine and write it to a file
../src/gen_quine python > quine.py

#---- Execute the quine, store its output as clone
run_python quine.py > clone.py

#---- Diff the clone against the original
diff -s quine.py clone.py


Commands I used to execute the generated quine and make a clone to compare it: <br>
```cmd
python .\generated_quine.py > clone.py
dotnet fsi .\generated_quine.fsx > clone.fsx
javac .\quine.java
java quine > clone.java
```

Now check difference using diff tool (I used WSL Ubuntu) <br>
- Open Windows CMD
- Type `ubuntu`
```cmd
anuragb@AnuragBamba98: cd /mnt/c/Users/anura/Documents/VSCode_Workspace/Quine_relays/quine_gen
```

You might need to change the encoding of `clone.py` to UTF-8 using Notepad++ before running the diff command. <br>
Although, the code is same and quine is indeed formed, it'd say that the binary files are different.
```cmd
diff generated_quine.py clone.py
```


**Troubleshooting:**
```cmd
SyntaxError: Non-UTF-8 code starting with '\xff' in file C:\Users\anura\Documents\VSCode_Workspace\Quine_relays\quine_gen\generated_quine.py on line 2, but no encoding declared; see https://python.org/dev/peps/pep-0263/ for details
```

Open file in Notepad++ and change Encoding of generated quines to UTF-8.


## Poly-Quine/ Quine Relay generator
- Now the goal is to extend the quine generator so that it can generate quine relays
- The program will now expect one or more string arguments, selected from *java*,*python*,*fsharp*. A single argument results in a standard quine. It should be OK to repeat arguments.

- The use-case described in the tutorial is that what if we want to insert some lines/parameters in code (having the same functionality) developed in multiple languages.

- To do this, we can modify the template from earlier, by splitting the list of strings into list of lists of strings.

- At runtime, we can insert the variables/parameters/lines between the 2 or more lists that make up the template.

```cmd
PS C:\Users\anura\Documents\VSCode_Workspace\Quine_relays\quine_relay_gen> python .\polyquine.py java python fsharp java

public class quine {
 public static void main(String[] args) {
  String[] data = {
 "public class quine {",
 " public static void main(String[] args) {",
 "  String[] data = {",
 "  };",
 "  int a=14; int b=15; int c=24; int sep=44;",
 "  char q = (char) 34; char space = (char) 32; char separator = (char) sep;",
 "  for (int i = a; i < b; i++)",
 "    System.out.println(data[i]);",
 "  for (int i = 0; i < data.length; i++)",
 "    System.out.println(String.valueOf(space) + q + data[i] + q + separator);",
 "  for (int i = b; i < c; i++)",
 "    System.out.println(data[i]);",
 " }",
 "}",
 "data = [",
 "]",
 "a, b, c, sep = 24, 25, 34, 59",
 "q, space, separator = chr(34), chr(32), chr(sep)",
 "for k in range(a,b):",
 "  print(data[k])",
 "for d in data:",
 "  print(space + q + d + q + separator)",
 "for k in range(b,c):",
 "  print(data[k])",
 "let data = [",
 "]",
 "let a, b, c, sep = 34, 37, 48, 44",
 "let q, space, separator = string(char 34), string(char 32), string(char sep)",
 "for i in a..b-1 do",
 "   System.Console.WriteLine(data.[i])",
 "for i in 0..data.Length-1 do",
 "   System.Console.WriteLine(space + q + data.[i] + q + separator)",
 "for i in b..c-1 do",
 "   System.Console.WriteLine(data.[i])",
 "public class quine {",
 " public static void main(String[] args) {",
 "  String[] data = {",
 "  };",
 "  int a=0; int b=3; int c=14; int sep=44;",
 "  char q = (char) 34; char space = (char) 32; char separator = (char) sep;",
 "  for (int i = a; i < b; i++)",
 "    System.out.println(data[i]);",
 "  for (int i = 0; i < data.length; i++)",
 "    System.out.println(String.valueOf(space) + q + data[i] + q + separator);",
 "  for (int i = b; i < c; i++)",
 "    System.out.println(data[i]);",
 " }",
 "}",
  };
  int a=14; int b=15; int c=24; int sep=44;
  char q = (char) 34; char space = (char) 32; char separator = (char) sep;
  for (int i = a; i < b; i++)
    System.out.println(data[i]);
  for (int i = 0; i < data.length; i++)
    System.out.println(String.valueOf(space) + q + data[i] + q + separator);
  for (int i = b; i < c; i++)
    System.out.println(data[i]);
 }
}
```

## Prerequisites

- The host needs to have the various languages (Python, fsharp and java) installed

## References
- https://drcabana.org/
- https://drcabana.org/quine/
- https://codeberg.org/drcabana/polyquine
- https://learn.microsoft.com/en-us/dotnet/fsharp/get-started/get-started-vscode
