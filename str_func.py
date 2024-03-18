def upper_string(s):
    """
       Функция, которая преобразует всю строку в верхний регистр.
       :param s: Строка, которую нужно преобразовать.
       :return: Строка в верхнем регистре."""
    return s.upper()

def capitalize_first_letter(input_string):
    """
    Функция, которая делает заглавными первые буквы каждого слова в строке.
    :param input_string: Строка, которую нужно обработать.
    :return: Строка с заглавными первыми буквами каждого слова.
    """
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)