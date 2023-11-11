
n = 123476565433434232
strn = str(n)

if len(strn) >= 4:
    outputstring = strn[:-3] + "." + strn[-3:]
    print(outputstring)
else:
    print(strn)
