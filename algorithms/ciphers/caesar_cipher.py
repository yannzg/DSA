import sys

def only_digits(s):
    return s.isdigit()

def rotate(c, n):
    if not c.isalpha():
        return c

    if c.isupper():
        return chr((ord(c) - ord('A') + n) % 26 + ord('A'))
    else:
        return chr((ord(c) - ord('a') + n) % 26 + ord('a'))


def main():
    # Make sure program is run with just one command-line argument
    if len(sys.argv) != 2:
        print("Usage: python caesar.py key")
        sys.exit(1)

    # Make sure every character in the command-line argument is a digit
    if not only_digits(sys.argv[1]):
        print("Usage: python caesar.py key")
        sys.exit(1)

    # Convert the command-line argument to an integer
    n = int(sys.argv[1])

    # Prompt user for plaintext
    plaintext = input("Plaintext: ")

    # Encipher entire plaintext
    ciphertext = "".join(rotate(char, n) for char in plaintext)

    print(f"Ciphertext: {ciphertext}")


if __name__ == "__main__":
    main()