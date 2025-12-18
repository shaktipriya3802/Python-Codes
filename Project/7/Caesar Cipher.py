from logo_art import logo

alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Printing the logo
print(logo)

# ENCRYPTION
def encrypt():
    shifted_text = "" # Stores the encrypted text
    for letter in text: 
        if letter not in alphabet: # Prints the encrypted letter leaving the Symbols, characters, Space, Number 
            shifted_text+=letter
        else:
            original_text = alphabet.index(letter)  # return the position of each letter in the message you typed
            shifted_position = original_text + shift  # integer, applies the shift to the position i.e say "h" -> position of h = 8, shift = 3, shifted_text = 8+3 = 11
            shifted_position %= len(alphabet) # Prints beyond Z
            shifted_text += alphabet[shifted_position]  # prints the alphabet according to the shifted position
    print("Here is the encoded result:", shifted_text)

# DECRYPTION 
def decrypt():
    original_text = ""
    for letter in text:
        if letter not in alphabet:
            original_text+=letter
        else:
            shifted_text = alphabet.index(letter)
            shifted_position = shifted_text - shift
            shifted_position %= len(alphabet)
            original_text += alphabet[shifted_position]
    print("Here is the decoded result:", original_text)


# While loop to execute the Cipher process repeatedly
yes_or_no = False
while not yes_or_no:
    encrypt_decrypt = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if encrypt_decrypt == "encode":
        encrypt() # Executes "Encryption Function" when user selects "Encryption"
    elif encrypt_decrypt=="decode":
        decrypt() # Executes "Decryption Function" when user selects "Decryption"
    else:
        print("You have entered the option incorrectly")

  # Asks the user if he wants to Encrypt/Decrypt i.e go Cipher again
    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if user_input=="No":
        yes_or_no=True
        print("Good Bye") # Prints Good Bye if he selects "No"

