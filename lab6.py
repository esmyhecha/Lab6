# ESMERALDA HECHAVARRIA

def encode_input(input_e):
    encoded_res = ''
    for char in input_e:
        char = int(char)
        char += 3
        encoded_res += str(char)
    return encoded_res


def main():
1    while True:
        print() #this is me making a change 
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
            pass

        if option == '3':
            break

if __name__ == "__main__":
    main()
