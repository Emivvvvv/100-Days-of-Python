import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = (int(input("Type the shift number:\n"))) % 26

def caesar(text, shift, direction):
    if direction == "decode":
        shift *= -1
    modified_text = []
    for letter in text:
        if letter not in alphabet:
            modified_text.append(letter)
        else:
            letter_place = alphabet.index(letter)
            modified_text.append(alphabet[(letter_place + shift) % 26])
    print(f"The {direction}d text is {''.join(modified_text)}")

caesar(text, shift, direction)