dirtyChars = ['!', ',', '?', ' ', '.', ';', ':', '/', '...']

phrase = input('Enter with a phrase: ')

phraseSanitized = ''
for char in phrase.lower():
    if char not in dirtyChars:
        phraseSanitized += char

phraseReversed = phraseSanitized[::-1]

if phraseSanitized == phraseReversed:
    print(f'The phrase "{phrase}" is palindrome')
else:
    print(f'The phrase "{phrase}" is not palindrome')
