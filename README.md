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
Write the same script, however keeping in mind the syntax differences from Python.

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



## References
- https://drcabana.org/
- https://drcabana.org/quine/
- https://learn.microsoft.com/en-us/dotnet/fsharp/get-started/get-started-vscode
