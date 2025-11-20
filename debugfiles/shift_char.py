alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

text = "z"
shift = 1

def encrypt(original_text, shift_amount):
    encrypted_text = []

    for char in original_text:
        index_encoded = alphabet.index(char) + shift_amount
        while index_encoded > len(alphabet):
            index_encoded -= len(alphabet)
        encrypted_text.append(alphabet[index_encoded])

    print(str(encrypted_text))

encrypt(text, shift)