def odd_even(number):
    if number == 0:
        return "0 is not classified"

    if number % 2 == 0:
        return number, "even"

    return number, "odd"

def odd_even_list(numbers):
    result = []
    for number in numbers:
        value = odd_even(number)
        result.append(value)
    return result


def odd_even_final(num,multiple):
    if multiple:
        return odd_even_list()
    else:
        return odd_even()

# def palindrome(numb):
#     numb_str = str(numb)
#     reversed_str = numb_str[::-1]
#     if numb_str == reversed_str:
#         return "Yes it is palindrome"
#     else:
#         return "No it is not palindrome"
#
# print(palindrome(145))
# print(palindrome(121))

def palindrome(numb):
    numb_str = str(numb)
    reversed_str = ""
    for char in numb_str:
        reversed_str = char + reversed_str
    return numb_str == reversed_str

print(palindrome(123))
print(palindrome(121))

