data = [
 "data = [",
 "]",
 "boundary = 1",
 "a, b, c = 0, boundary, len(data)",
 "quote, space, separator = chr(34), chr(32), chr(44)",
 "for k in range(a,b):",
 "  print(data[k])",
 "for d in data:",
 "  print(space + quote + d + quote + separator)",
 "for k in range(b,c):",
 "  print(data[k])",
]
boundary = 1
a, b, c = 0, boundary, len(data)
quote, space, separator = chr(34), chr(32), chr(44)
for k in range(a,b):
  print(data[k])
for d in data:
  print(space + quote + d + quote + separator)
for k in range(b,c):
  print(data[k])
