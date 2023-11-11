accounts = [[1,5],[7,3],[3,5]]
max=0
for i in accounts:
    s=0
    print(i)
    for j in i:
        print(j)
        s+=j
    print(s)
    if s>max:
     max=s
print("max value is",max)