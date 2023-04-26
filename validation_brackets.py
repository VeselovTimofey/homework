def validation_string(string_of_brackets: str) -> bool:
    if string_of_brackets == '':
        # checking for an empty string.
        return False
    answer = True
    element_counter = {'(': 0, '[': 0, '{': 0}
    double = {')': '(', ']': '[', '}': '{'}
    for element in string_of_brackets:
        if element in element_counter.keys():
            element_counter[element] += 1
        elif element in double.keys() and element_counter[double[element]] > 0:
            # checking that the element is a right bracket and has a pair
            element_counter[double[element]] -= 1
        else:
            # if there is something other than bracket, exit the loop
            element_counter['('] += 1
            break
    for number in element_counter.values():
        # check that we don't have brackets without a pair
        if number != 0:
            answer = False
            break
    return answer


if __name__ == "__main__":
    print(validation_string(string_of_brackets=input("Введите строку из скобок.")))
