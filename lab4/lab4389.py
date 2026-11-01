digits = input()
result = ""

while len(digits) > 3:
    result = "," + digits[-3:] + result
    digits = digits[:-3]

print(digits + result)