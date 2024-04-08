print ("Input phrase: ")
phrase = input()

print ("You entered: "+ phrase)

alphabet = "abcdefghijklmnopqrstuvwxyz" 
newPhrase = " "

phrase = phrase.lower()

for char in phrase:
    if char in alphabet: 
        newChar = alphabet[(alphabet.index(char)+5)% 26]
        newPhrase += newChar
    else:
        newPhrase += char
print ("The Cipher Phrase is" + newPhrase)