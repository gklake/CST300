inputMessage = input()
key = input()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
finalMessage = ''
for i in range(len(inputMessage)):
    a = alphabet.index(inputMessage[i])
    b = alphabet.index(key[i])
    finalMessage += alphabet[(a-b) % len(alphabet)]
    key += finalMessage[-1]
print(finalMessage)