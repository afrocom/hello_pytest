def sumOfInts(num1, num2):

    return num1 + num2


def sumOfFloat(number_1, number_2):

    if isinstance(number_1, float) and isinstance(number_2, float):

        return number_1 / number_2

    else:
        raise ValueError("Both inputs must be floating point numbers")

print(sumOfFloat(12.5,5.5));