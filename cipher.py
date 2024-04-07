# add your code here
print ("Input phrase: ")
phrase = input()

print ("You entered: "+ phrase)

alphabet = "abcdefghijklmnopqrstuvwxyzabcde" 
newPhrase = " "

# i is a placeholder for an integer, like x in algebra. For our purpose, i stand in for any and all numbers in the ran

# Len is short for Length. When we give range a staring point of 0 and ending point of Len, we're telling the program

for i in range(0, len(phrase)):
    try:
        char = phrase[i]
        newChar = str(alphabet[alphabet.index(char)+5])
        # Think of += as meaning "add to variable", so when we use +=, we're adding something to an existing variable.
        newPhrase += newChar

    #except is an exception case. This only runs if the paramaters set in the try case fail.

    except:
        newChar = str(alphabet[0])
        newPhrase += newChar

print ("The Cipher Phrase is" + newPhrase)