# Больше одного return, стоит переписать
def validation_string(string_of_brackets):
    elements = {'(': 0, '[': 0, '{': 0}
    double = {')': '(', ']': '[', '}': '{'}
    for element in string_of_brackets:
        if element in elements.keys():
            elements[element] += 1
        elif element in double.keys():
            elements[double[element]] -= 1
            if elements[double[element]] < 0:
                return "нет"
        else:
            return "нет"
    for number in elements.values():
        if number != 0:
            return "нет"
    return "да"


if __name__ == "__main__":
    print(validation_string(string_of_brackets="[]{}[[]]"))
