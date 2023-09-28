from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(code, text, shift):
  
  # ENCODE
  if code == 'encode':
    cipher_text = ''
    for let in text: 
      if let in alphabet:
        position = alphabet.index(let) 
        new_pos = position + shift
        while new_pos > 25:
          new_pos -= 26
        new_let = alphabet[new_pos]
        cipher_text += new_let
      else:
        cipher_text += let
  
    print(f"Encoded text: {cipher_text}")

  # DECODE
  else:
    decrypted_text = ''
    for let in text:
      if let in alphabet:
        position = alphabet.index(let)
        new_pos = position - shift
        while new_pos <= -1:
          new_pos += 26
        new_let = alphabet[new_pos]
        decrypted_text += new_let
      else:
        decrypted_text += let

    print(f"Decrypted text: {decrypted_text}")

run_program = True

while run_program:
  code = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(code, text, shift)

  result = input("Do you wish to continue? Type no to quit: ")
  if result == 'no':
    run_program = False
    print('Bye Bye')