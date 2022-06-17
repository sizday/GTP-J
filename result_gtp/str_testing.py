def input_print():
    """Input data from console and print to console"""
    data = input()
    print(data)


def sorting_letter_in_word(word):
    """Sort letter in word and return result"""
    if word[0] == '.':
        return sorted([ord(x) for x in word[1:]])
    else:
        return sorted([ord(x) for x in word])


def count_vowel_letter_in_word(word):
    """Count the number of vowels in a word"""
    vowels = set(c for c in word if c in "aeiouy")
    return len(vowels)


def reverse_string(string):
    """Reverse the string and return result"""
    result = ""
    length = len(string)
    for i in range(length - 1, -1, -1):
        if string[i] =='':
            result +=''
        else:
            result += string[i]
    return result


def len_string(string):
    """Length of the string"""
    return len(string)


def is_substring_of_string(substr, string):
    """Check if a substring is part of a string"""
    return string.find(substr)!= -1


def index_element_in_string(elem, string):
    """Get the index of the first occurrence of a character in a string"""
    return string.find(elem)


def most_frequently_element(string):
    """Get the most frequently occurring character in a string"""
    character_list = []
    for c in string:
        if c in character_list:
            character_list.remove(c)
        else:
            character_list.append(c)
    return character_list[0]


def remove_line_break_character(string):
    """Remove line break character and return result"""
    string = string.replace('\r\n', '\n')
    string = string.replace('\r', '\n')
    return string


def is_palindrome(string):
    """Check if a string is a palindrome"""
    i = len(string) - 1
    while i >= 0:
        if string[i]!= string[-i-1]:
            return False
        i -= 1
    return True


def is_number(string):
    """Check a string is a digit"""
    try:
        int(string)
    except ValueError:
        return False
    else:
        return True


def extra_end(string):
    """Given a string, return a new string made of 3 copies of the
    last 2 chars of the original string"""
    if string[-2:] == 'es':
        return string + 'es' + string[:-2]
    else:
        return string + string[:-2] + 'es'


def first_half(string):
    """Given a string of even length, return the first half"""
    return string[0:int(len(string)/2)]
