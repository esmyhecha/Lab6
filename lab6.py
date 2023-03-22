# ESMERALDA HECHAVARRIA

def encode_input(input_e):
    encoded_res = ''
    for char in input_e:
        char = int(char)
        char += 3
        encoded_res += str(char)
    return encoded_res

def decode_input(input_d): # decoder written by nagendra
    decoded_res = ''
    for char in input_d:
        char = int(char)
        char -= 3
        decoded_res += str(char)
    return decoded_res

def main():
   while True: #comment of my change for the rubric
        print()
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        option = input("Please enter an option: ")

        if option == '1':
            input_e = input("Please enter your password to encode: ")
            encode_input(input_e)
            print("Your password has been encoded and stored!")

        if option == '2':
            input_d = encode_input(input_e)
            og_pw = decode_input(input_d)
            print(f"Your password is {input_d}, and the original password is {og_pw}.")

        if option == '3':
            break

if __name__ == "__main__":
    main()
