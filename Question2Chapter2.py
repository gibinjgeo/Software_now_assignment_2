import re

s = '56aAww1984sktr235270aYmn145ss785fsq31D0'

number_string = ''.join(re.findall(r'\d', s))
letter_string = ''.join(re.findall(r'[a-zA-Z]', s))

print("Number string:", number_string)
print("Letter string:", letter_string)

even_numbers = [int(ch) for ch in number_string if int(ch) % 2 == 0]
ascii_even_numbers = [ord(str(ch)) for ch in even_numbers]

print("Even numbers in number string:", even_numbers)
print("ASCII values of even numbers:", ascii_even_numbers)

upper_case_letters = [ch for ch in letter_string if ch.isupper()]
ascii_upper_case_letters = [ord(ch) for ch in upper_case_letters]

print("Upper-case letters in letter string:", upper_case_letters)
print("ASCII values of upper-case letters:", ascii_upper_case_letters)
print("")
print("")
print("")

ciphered_quote = "V2 FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVHGHXRF V NZ BHG BS PHAGFBY hAONG GVZrf unEQ gb unNaoyr OHg Vs LOH PHAG UNAQYR ZR NG ZL 30EFG GURA LDH FHER NF URYYQBAG QRFREIR ZR NS ZL ORFG ZNEVYLA ZBAEBR"

def decrypt_caesar(cipher_text, shift):
    decrypted_text = []
    for char in cipher_text:
        if 'A' <= char <= 'Z':
            decrypted_text.append(chr((ord(char) - shift - 65) % 26 + 65))
        elif 'a' <= char <= 'z':
            decrypted_text.append(chr((ord(char) - shift - 97) % 26 + 97))
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)


shift_key = 13

deciphered_quote = decrypt_caesar(ciphered_quote, shift_key)
print("Deciphered Quote:", deciphered_quote)
print("")
print("")
print("From the above Deciphered Quote, we can rearrange the quote to: "
      "I am selfish, impatient and a little insecure, I make mistakes, "
      "I am out of control and at times hard to handle. But if you can't handle "
      "me at my worst, then you sure as hell don't deserve me at my best. "
      "MARILYN MONROE")
