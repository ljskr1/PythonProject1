import random

odd_even_lamda = lambda num: num % 2

if '__main__' == __name__: #so it wont run in main cuz it wont be imported
    print(odd_even_lamda(2))


from functools import reduce

print(reduce(lambda x, y: x*y, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

print(reduce(lambda a,b : a+b, [1,2,3,4,5,6,7,8,9]))

print(reduce(lambda a,b:a if a>b else b, [1,2,3,4,5,6,7,8,9]))

list1 = [random.randint(1, 43) for i in range(10)]
list2 = [random.randint(5, 52) for i in range(10)]
print(list1)

# Print 'o' for odd and 'e' for even numbers
print(['o' if num % 2 else 'e' for num in list1])

# Using map, ensure consistent output: 'e' for even, 'o' for odd
print(list(map(lambda x: 'e' if x % 2 == 0 else 'o', list1)))


print(list(map(lambda x, y: (x, y), list1, list2)))

print(list(map(is_prime, list)))
