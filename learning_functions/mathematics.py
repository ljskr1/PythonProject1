# Questions:

# 1. Create a function for odd even classification of a number.

def odd_even(number):
    if number == 0:
        return "0 is not classified"

    if number % 2 == 0: #if number is div by 2 it is even
        return number, "even"

    return number, "odd" # if number is div 2 it is odd


# 2. Create a function for even odd classification of a list of numbers.

def odd_even_list(numbers):
    result = [] # empty to store result
    for number in numbers: # to loop each number in input list
        value = odd_even(number) # using odd_even function from Q.1 to classify number
        result.append(value) #add result and value
    return result


# 3. Can you fuse 1, 2 Together in a Single Function?

def odd_even_final(num,multiple):
    if multiple:
        return odd_even_list()
    else:
        return odd_even()


# 4. Create a number palindrome function. [Yesterday's Class Assessment]

# def palindrome(numb):
#     numb_str = str(numb)
#     reversed_str = ""
#     for char in numb_str:
#         reversed_str = char + reversed_str
#     return numb_str == reversed_str
#
# print(palindrome(123))
# print(palindrome(121))


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

def palindrome(numberr):
    original_numberr = numberr #save this input later so we can compare
    reversed_numberr = 0 # craeted a number to store reverse and
    # starts at 0 because there no reverse number yet
    for i in str(numberr):
        last_char = numberr % 10 # to get last digit of number
        reversed_numberr = reversed_numberr * 10 + last_char # add this digit to reverse num
        # and multiply current reversed number by 10 to make space for new digit
        numberr = numberr // 10 # to remove last digit of number by div 10 and ignoring remainder

    return reversed_numberr == original_numberr #comparing reverse numb with original

print(palindrome(145))
print(palindrome(121))

def factorial(nums):
    if nums == 0: #edge case
        return 0
    if nums == 1:
        return 1
    return factorial(nums-1) * nums

print(factorial(5))

fibbonacci
tower of hanoi