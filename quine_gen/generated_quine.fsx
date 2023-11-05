let data = [
 "let data = [";
 "]";
 "let boundary = 1";
 "let a, b, c = 0, boundary, data.Length";
 "let quote, space, separator = string(char 34), string(char 32), string(char 59)";
 "for k in a..b-1 do";
 "   System.Console.WriteLine(data.[k])";
 "for d in data do";
 "   System.Console.WriteLine(space + quote + d + quote + separator)";
 "for k in b..c-1 do";
 "   System.Console.WriteLine(data.[k])";
]
let boundary = 1
let a, b, c = 0, boundary, data.Length
let quote, space, separator = string(char 34), string(char 32), string(char 59)
for k in a..b-1 do
   System.Console.WriteLine(data.[k])
for d in data do
   System.Console.WriteLine(space + quote + d + quote + separator)
for k in b..c-1 do
   System.Console.WriteLine(data.[k])
