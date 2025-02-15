name = input().upper().split() 
results = []
for string in name: 
    result = ''
    for s in string: 
        number = ord(s)
        result += chr(65 + (number - 65 + 9) % 26)
    results.append(result)
print(*results)