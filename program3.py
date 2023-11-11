sentence = " This is a  sentence    "
spacecount = sentence.count(' ')
print(spacecount)

words = sentence.split()
wordcount = len(words)
print(wordcount)
newspace=spacecount/(wordcount-1)
print(newspace)
extra_spaces = spacecount % (wordcount - 1) if wordcount > 1 else spacecount
formatted_sentence = (' ' * newspace).join(words)


print(formatted_sentence)

