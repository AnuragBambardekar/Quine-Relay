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
