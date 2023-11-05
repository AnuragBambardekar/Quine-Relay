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