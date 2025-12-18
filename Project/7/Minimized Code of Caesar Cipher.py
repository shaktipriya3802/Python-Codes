from logo_art import logo

alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Prints the logo
print(logo)

# Defining the Caesar Cipher Function which Encrypts & Decrypts the data entered by the user
def caesar(text_,shift_amount):
    shifted_text = ""
    if encrypt_decrypt == "decode": # Once the user selects the option of DECRYPTION, the Shift Amount will be multiplied by (-1)
        shift_amount *= (-1)
    for letter in text_:
        if letter not in alphabet:
            shifted_text+=letter
        else:
            original_text = alphabet.index(letter)  # return the position of each letter in the message you typed
            shifted_position = original_text + shift_amount  # integer, applies the shift to the position i.e say "h" -> position of h = 8, shift = 3, shifted_text = 8+3 = 11
            shifted_position %= len(alphabet)
            shifted_text += alphabet[shifted_position]  # prints the alphabet according to the shifted position
    print(f"Here is the {encrypt_decrypt}d result:", shifted_text)

# While loop to execute it the Caesar Cipher Process repeatedlty
yes_or_no = False
while not yes_or_no:
    encrypt_decrypt = input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text_=text,shift_amount=shift)

#  User Confirmation: Asks the user if he/she wants to execute the Encryption/Decryption again 

    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if user_input=="no":
        yes_or_no=True
        print("Good Bye") # If the user selects "NO", The loop stops its execution by printing Good Bye

