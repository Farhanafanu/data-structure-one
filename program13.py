s = "book"
vowels = "aeiou"
half = len(s) // 2
a = s[:half]
print(a)
b = s[half:]
print(b)
counta = 0
countb = 0

for i in a:
    if i in vowels:
        counta += 1
for i in b:
    if i in vowels:
        countb += 1

if counta == countb:
    print("true")
else:
    print("false") 
