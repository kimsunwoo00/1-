a = int(input())
b = input()

result1 = a * int(b[2])
result2 = a * int(b[1])
result3 = a * int(b[0])
result = a * int(b)

print(result1, result2, result3, result, sep='\n')
