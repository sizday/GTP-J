import time
import math
import datetime


def is_year_leap(year):
    """The function takes 1 argument, the year,
    and returns True if the year is a leap year, and False otherwise"""
    return year % 4 == 0 and (year % 100!= 0 or year % 400 == 0)


def season(month):
    """Getting the time of year by month number"""
    if month==0:
        return None
    else:
        return time.localtime(time.mktime((1,1,1,month,1,1)))


def is_prime(number):
    """Checking whether a number is prime"""
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def is_date_correct(date):
    """Checking the date for correctness and existence"""
    if type(date)!= type(datetime.datetime.now()):
        return False

    return date.strftime("%Y-%m-%d") == datetime.datetime.now().strftime("%Y-%m-%d")


def magic_square(n):
    """Creation of a magic square dimension n * n"""

    # Let the function know that it needs to return a list
    return [0]*(n*n)


def recursive_horse(n):
    """Recursive traversal of a chessboard"""
    if n == 0:
        return

    for x in range(0, n-1):
        for y in range(0, n-1):
            if x+y!= n:
                if x+y == n-1:
                    print(x, y, n-1, n)


def sort_dict_by_value(dictionary):
    """Sorting a dictionary by values"""
    sorted_dictionary = {}
    for key, value in dictionary.iteritems():
        if key in sorted_dictionary:
            sorted_dictionary[key] += value
        else:
            sorted_dictionary[key] = value
    return sorted_dictionary


def triangle_square_by_heron(n):
    """Calculate the area of a triangle using Heron's formula"""
    # Triangles
    a = math.sqrt(3 * (n - 2))
    b = math.sqrt(3 * n)
    c = math.sqrt(n)
    # Heron's formula
    area = (n / 2) * (b * b + c * c - a * a)
    return area


def money_change(money_sum):
    """The amount of money is known. Exchange it with banknotes of 500, 100, 10
    and a coin of 2 rubles, if possible."""

    if money_sum == 0:
        return {'money': 0,'money_change': 0}

    money_change = money_sum - 500
    money_change = min(money_change, money_sum - 100)
    money_change = max(money_change, money_sum - 10)
    money_change = max(money_change, money_sum - 2)
    money_change = min(money_change, money_sum - 500)

    return money_change


def read_from_file(filepath):
    """Read data from a file along the way and display it on the screen"""
    f = open(filepath)
    lines = f.readlines()
    f.close()
    return lines


def factorial(number):
    """Get factorial of number using recursive"""
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)
