a_lowercase = 'abcdefghijklmnopqrstuvwxyz'
a_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numLetters = 26

def alphabet_position(letter):
    pos = a_lowercase.find(letter)
    if pos >= 0:
        return pos
    else:
        return a_uppercase.find(letter)

def rotate_character(char, rot):
    pos = alphabet_position(char)
    if pos < 0:
        return char
    else:
        indx = (pos + rot) % numLetters
        if char in a_lowercase:
            return a_lowercase[indx]
        else:
            return a_uppercase[indx]

def encrypt(text, rot):
    result = ""
    for a_char in text:
        result += rotate_character(a_char, rot)
    return result
