a = int(input())
b = int(input())

if a > b:
    sign = ">"
elif a < b:
    sign = "<"
else:
    sign = "="

print(f"{a} {sign} {b}")