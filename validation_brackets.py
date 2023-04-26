def validation_string(string_of_brackets: str) -> bool:
    if string_of_brackets == '':
        # проверка на пустую строку
        return False
    answer = True
    element_counter = {'(': 0, '[': 0, '{': 0}
    double = {')': '(', ']': '[', '}': '{'}
    for element in string_of_brackets:
        if element in element_counter.keys():
            element_counter[element] += 1
        elif element in double.keys() and element_counter[double[element]] > 0:
            # проверяем, что элемент это правая скобка и у него есть пара
            element_counter[double[element]] -= 1
        else:
            # если есть что-то кроме скобок, выходим из цикла
            element_counter['('] += 1
            break
    for number in element_counter.values():
        # проверяем, что у нас не осталось скобки без пары
        if number != 0:
            answer = False
            break
    return answer


if __name__ == "__main__":
    print(validation_string(string_of_brackets=input("Введите строку из скобок.")))
