word = input()
start = 0

while word[start:] != word[start:][::-1]:
    start += 1

print(start)