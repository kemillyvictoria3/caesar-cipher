def encode(message, shift):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K'
     ,'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',
    'Z']
    partialstart = ''
    partialend = ""
    shiftedAlphabet = ""
    encodemensage = ''
   
    if shift == 0:
        shiftedAlphabet = alphabet
    elif shift > 0 and shift < 26:
        partialstart = alphabet [:shift]
        partialend = alphabet [shift:]
        shiftedAlphabet = partialend + partialstart
    elif shift < 0 and shift > -26:
        shift = shift * -1
        partialstart = alphabet [:shift]
        partialend = alphabet [shift:]
        shiftedAlphabet = partialend + partialstart
    else:
        return("shift_error")
    for letter in message:
        letter_index = alphabet.index(letter)
        encodemensage = encodemensage + shiftedAlphabet[letter_index]

    return (encodemensage)
