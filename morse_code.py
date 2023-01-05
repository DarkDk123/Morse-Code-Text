# Morse Code in Python Dictionary

Morse_Code_Dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ' ': '|'}


def encrypt_text(text: str) -> str:
    morse_code = ""
    for letter in text.upper():
        # Ternary if-else for more concise Encoding Format.
        morse_code += Morse_Code_Dict[letter] if (
            letter in Morse_Code_Dict) else ''
        # Adding 3-unit Spaces between each "letter".
        morse_code += '   '

    return morse_code


def decrypt_morse(morse: str) -> str:
    plain_text = ""
    for word in morse.split('|'):
        for letter in word.split('   '):
            for group in Morse_Code_Dict.items():
                plain_text += group[0].strip() if (letter in group) else ''
        plain_text += ' '
    return plain_text


if __name__ == '__main__':
    while 1:
        c = input("Wanna Encode('e') or Decode('d') or Exit('z'): ").lower()
        if (c == 'z'):
            print("Good Bye!!👋")
            break
        elif (c == 'e'):
            result = encrypt_text(input("Text to Encode: "))
        elif (c == 'd'):
            result = decrypt_morse(input("Morse to decode: "))
        else:
            print("Please Enter a valid Choice !!🙏")
            continue
        print("Result: ", result)
