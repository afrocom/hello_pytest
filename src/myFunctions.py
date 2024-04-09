def sumOfInts(num1, num2):

    return num1 + num2


def sumOfFloat(number_1, number_2):

    if isinstance(number_1, float) and isinstance(number_2, float):

        return number_1 + number_2

    else:
        raise ValueError("Both inputs must be floating point numbers")

def get_ascii_code(char):

    return ord(char)


def print_ascii_stream(sentence):
    ascii_stream = [ord(char) for char in sentence]
    for ascii_code in ascii_stream:
        print(ascii_code, end=' ')
