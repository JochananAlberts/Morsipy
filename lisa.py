from dictionary import morse_code_dict

def morsify(text):
    ### Returns the morse translation of a text ###
        return ' '.join(morse_code_dict[char] for char in text.upper() if char in morse_code_dict)


message = input("What message do you want to put into morse code? \n")
print(f"The encoded message: \n\n{morsify(message)}")
