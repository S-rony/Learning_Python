alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
def decrypt(original_text, shift_amount):

# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
    backward_text = ""
    for letter in original_text:

        backwards_index = alphabet.index(letter) - shift_amount
        backwards_index %= len(alphabet)
        backward_text += alphabet[backwards_index]
    print(f"Here is the decoded result: {backward_text}")
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.

def caesar(original_text, shift_amount ,encode_or_decode):
    if encode_or_decode == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif encode_or_decode == "decode":
        decrypt(original_text=text, shift_amount=shift)

#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


caesar(text,shift,direction)



