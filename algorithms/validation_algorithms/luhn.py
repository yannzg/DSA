# Luhn Algorithm

def luhn(number):
    x = len(str(number))

    digits = [int(d) for d in str(number)]
    for i in range(x - 2, -1, -2):
        digits[i] *= 2

    for j in range(x):
        if digits[j] >= 10:
            digits[j] -= 9

    if sum(digits) % 10 == 0:
        return f"{number} is Luhn-valid."
    else:
        return f"{number} is Luhn-invalid"

if __name__ == "__main__":
    number = 4532015678923456
    print(luhn(number))