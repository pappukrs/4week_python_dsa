
def even_check(num):
    return num % 2 == 0


print(even_check(21))  # True



x = [ x**2   for x in range(1,100)  if x % 2==0 ]
print(x)


num = input("Enter a number: ")
print(even_check(int(num)))  # True

# Q1: Write a program to check if a number is positive, negative, or zero.
def number_check(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
print(number_check(21))  # Positive


# ✅ Q2: Write a program to check if a given year is a leap year.

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap Year"
            else:
                return "Not Leap Year"
        else:
            return "Leap Year"
    else:
        return "Not Leap Year"

print(leap_year(2020))  # Leap Year




# Q3: Write a program to take a name as input and greet the user with:

def greet_user(name):
    return f"Hello, {name}!"


print(greet_user("John"))  # Hello, John!




# ✅ Q4: Write a program that takes a number as input and prints:

# "Fizz" if the number is divisible by 3
# "Buzz" if the number is divisible by 5
# "FizzBuzz" if the number is divisible by both 3 and 5
# The number itself if none of the above.


def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
print(fizz_buzz(15))  # FizzBuzz

# 📝 Practice Problems: Loops
# 2️⃣ For Loop & While Loop

# ✅ Q5: Write a program to print the Fibonacci series up to n terms.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
print(fibonacci(10))  # 0 1 1 2 3 5 8 13 21 34


# ✅ Q6: Write a program to print the multiplication table of a given number n.

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
print(multiplication_table(5))


# ✅ Q7: Write a program to calculate the factorial of a number using a loop.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))  # 120

# ✅ Q8: Write a program to print the sum of all even numbers from 1 to n.

def sum_even(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

print(sum_even(10))  # 30


# ✅ Q9: Write a program to print the following pattern:

def pattern(n):
    for i in range(1, n + 1):
        print("*" * i)
print(pattern(5))      




# 📝 Practice Problems: Functions
# 3️⃣ Functions
# ✅ Q10: Write a function to check if a number is prime.

# ✅ Q11: Write a function that takes a list of numbers and returns the maximum and minimum values in the list.

# ✅ Q12: Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.

# ✅ Q13: Write a function to check if a string is a palindrome.

# ✅ Q14: Write a function to find the sum of digits of a given number.

# ✅ Q10: Write a function to check if a number is prime.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(17))  # True


# ✅ Q11: Write a function that takes a list of numbers and returns the maximum and minimum values in the list.

def max_min(numbers):
    return max(numbers), min(numbers)

print(max_min([1, 2, 3, 4, 5]))  # (5, 1)



# ✅ Q12: Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(12, 15))  # 3


# ✅ Q13: Write a function to check if a string is a palindrome.


def is_palindrome(s):
    return s == s[::-1] 

print(is_palindrome("madam"))  # True


# ✅ Q14: Write a function to find the sum of digits of a given number.

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

print(sum_of_digits(12345))  # 15





# 📝 Practice Problems: Lists & Tuples
# 4️⃣ Lists & Tuples
# ✅ Q15: Write a program to find the second largest number in a list.

# ✅ Q16: Write a program to remove duplicates from a list.

# ✅ Q17: Write a program to find the intersection of two lists.

# ✅ Q18: Write a program to check if a given tuple is a palindrome.

# ✅ Q19: Write a program to sort a list of tuples based on the second element.


# ✅ Q15: Write a program to find the second largest number in a list.

def second_largest(numbers):
    return sorted(set(numbers))[-2]

print(second_largest([1, 2, 3, 4, 5]))  # 4


# ✅ Q16: Write a program to remove duplicates from a list.
def remove_duplicates(numbers):
    return list(set(numbers))

print(remove_duplicates([1, 2, 3, 2, 4, 5, 3]))  # [1, 2, 3, 4, 5]


# ✅ Q17: Write a program to find the intersection of two lists.    

def intersection(list1, list2):
    return list(set(list1) & set(list2))        

print(intersection([1, 2, 3], [2, 3, 4]))  # [2, 3]


# ✅ Q18: Write a program to check if a given tuple is a palindrome.    

def is_palindrome_tuple(t):
    return t == t[::-1]

print(is_palindrome_tuple((1, 2, 3, 2, 1)))  # True




# ✅ Q19: Write a program to sort a list of tuples based on the second element.
def sort_tuples(tuples):
    return sorted(tuples, key=lambda x: x[1])

print(sort_tuples([(1, 2), (3, 1), (5, 3)]))  # [(3, 1), (1, 2), (5, 3)]




# 📝 Practice Problems: Sets & Dictionaries
# 5️⃣ Sets & Dictionaries
# ✅ Q20: Write a program to find the union, intersection, and difference between two sets.

# ✅ Q21: Write a program to count the frequency of each word in a given string using a dictionary.

# ✅ Q22: Write a program to find the keys with the highest and lowest values in a dictionary.

# ✅ Q23: Write a program to merge two dictionaries and handle any duplicate keys by summing their values.

# ✅ Q24: Write a program to convert a dictionary to a list of tuples and vice versa.


# ✅ Q20: Write a program to find the union, intersection, and difference between two sets.


def set_operations(set1, set2):
    return set1 | set2, set1 & set2, set1 - set2

print(set_operations({1, 2, 3}, {2, 3, 4}))  # ({1, 2, 3, 4}, {2, 3}, {1})


# ✅ Q21: Write a program to count the frequency of each word in a given string using a dictionary.

def word_frequency(s):
    words = s.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

print(word_frequency("hello world hello"))  # {'hello': 2, 'world': 1}


# ✅ Q22: Write a program to find the keys with the highest and lowest values in a dictionary.

def min_max_keys(d):
    min_value = min(d.values())
    max_value = max(d.values())
    return [key for key, value in d.items() if value == min_value], [key for key, value in d.items() if value == max_value]
print(min_max_keys({"a": 1, "b": 2, "c": 1}))  # (['a', 'c'], ['b'])


# ✅ Q23: Write a program to merge two dictionaries and handle any duplicate keys by summing their values.

def merge_dicts(dict1, dict2):
    for key, value in dict2.items():
        dict1[key] = dict1.get(key, 0) + value
    return dict1

print(merge_dicts({"a": 1, "b": 2}, {"a": 2, "c": 3}))  # {'a': 3, 'b': 2, 'c': 3}


# ✅ Q24: Write a program to convert a dictionary to a list of tuples and vice versa.

def dict_to_tuples(d):
    return list(d.items())

def tuples_to_dict(tuples):
    return dict(tuples)

print(dict_to_tuples({"a": 1, "b": 2}))  # [('a', 1), ('b', 2)]
print(tuples_to_dict([('a', 1), ('b', 2)]))  # {'a': 1, 'b': 2}


# 📝 Practice Problems: String Manipulation
# 6️⃣ String Manipulation
# ✅ Q25: Write a program to check if two strings are anagrams.

# ✅ Q26: Write a program to count the vowels and consonants in a given string.

# ✅ Q27: Write a program to capitalize the first letter of each word in a string.

# ✅ Q28: Write a program to reverse the words in a string.

# ✅ Q29: Write a program to remove all special characters and numbers from a string.


# ✅ Q25: Write a program to check if two strings are anagrams.

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))  # True


# ✅ Q26: Write a program to count the vowels and consonants in a given string.

def count_vowels_consonants(s):
    vowels = sum(1 for char in s if char.lower() in "aeiou")
    consonants = sum(1 for char in s if char.isalpha() and char.lower() not in "aeiou")
    return vowels, consonants

print(count_vowels_consonants("hello"))  # (2, 3)


# ✅ Q27: Write a program to capitalize the first letter of each word in a string.

def capitalize_words(s):
    return " ".join(word.capitalize() for word in s.split())

print(capitalize_words("hello world"))  # Hello World


# ✅ Q28: Write a program to reverse the words in a string.

def reverse_words(s):
    return " ".join(s.split()[::-1])

print(reverse_words("hello world"))  # world hello


# ✅ Q29: Write a program to remove all special characters and numbers from a string.

def remove_special_characters(s):
    return "".join(char for char in s if char.isalpha())

print(remove_special_characters("he#llo 123"))  # hello


# 📝 Practice Problems: List Comprehensions
# 7️⃣ List Comprehensions
# ✅ Q30: Write a list comprehension to generate a list of squares of even numbers from 1 to 20.

# ✅ Q31: Write a list comprehension to filter out words that start with 'a' from a list of words.

# ✅ Q32: Write a list comprehension to create a dictionary where keys are numbers from 1 to 5, and values are their squares.

# ✅ Q33: Write a list comprehension to create a list of all lowercase letters from a given string.

# ✅ Q34: Write a list comprehension to generate the multiplication table of a number.


# ✅ Q30: Write a list comprehension to generate a list of squares of even numbers from 1 to 20.

squares = [x ** 2 for x in range(1, 21) if x % 2 == 0]

print(squares)  # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]


# ✅ Q31: Write a list comprehension to filter out words that start with 'a' from a list of words.

words = ["apple", "banana", "avocado", "orange"]

filtered_words = [word for word in words if word.startswith("a")]

print(filtered_words)  # ['apple', 'avocado']


# ✅ Q32: Write a list comprehension to create a dictionary where keys are numbers from 1 to 5, and values are their squares.

squares_dict = {x: x ** 2 for x in range(1, 6)}

print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ✅ Q33: Write a list comprehension to create a list of all lowercase letters from a given string.

s = "Hello, World!"

lowercase_letters = [char for char in s if char.islower()]

print(lowercase_letters)  # ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']



# ✅ Q34: Write a list comprehension to generate the multiplication table of a number.

n = 5

table = [f"{n} x {i} = {n * i}" for i in range(1, 11)]


print(table)  # ['5 x 1 = 5', '5 x 2 = 10', '5 x 3 = 15', '5 x 4 = 20', '5 x 5 = 25', '5 x 6 = 30', '5 x 7 = 35', '5 x 8 = 40', '5 x 9 = 45', '5 x 10 = 50']



# 📝 Practice Problems: Input/Output
# 8️⃣ Input/Output
# ✅ Q35: Write a program to take a list of names as input and write them to a file.

# ✅ Q36: Write a program to read a file and count the number of lines, words, and characters in it.

# ✅ Q37: Write a program to read a file and print only the lines that start with a specific word.

# ✅ Q38: Write a program to take input from the user and append it to a file.

# ✅ Q39: Write a program to find and replace a word in a file.


# ✅ Q35: Write a program to take a list of names as input and write them to a file.


names = ["Alice", "Bob", "Charlie"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")


# ✅ Q36: Write a program to read a file and count the number of lines, words, and characters in it.

with open("names.txt", "r") as file:
    lines = file.readlines()
    words = file.read().split()
    characters = file.read()

print(len(lines), len(words), len(characters))


# ✅ Q37: Write a program to read a file and print only the lines that start with a specific word.

word = "Alice"

with open("names.txt", "r") as file:
    for line in file:
        if line.startswith(word):
            print(line)


# ✅ Q38: Write a program to take input from the user and append it to a file.

text = input("Enter text: ")

with open("names.txt", "a") as file:
    file.write(text + "\n")
    

# ✅ Q39: Write a program to find and replace a word in a file.

word = "Alice"
replacement = "Bob"

with open("names.txt", "r") as file:
    text = file.read()

text = text.replace(word, replacement)

with open("names.txt", "w") as file:
    file.write(text)




#  Practice Problems: Sorting and Lambda Functions
# 9️⃣ Sorting & Lambda Functions
# ✅ Q40: Write a program to sort a list of numbers using a lambda function.

# ✅ Q41: Write a program to sort a list of dictionaries based on a specific key.

# ✅ Q42: Write a program to sort a list of strings by their length using a lambda function.

# ✅ Q43: Write a lambda function to calculate the product of two numbers.

# ✅ Q44: Write a lambda function to filter out all odd numbers from a list.


# ✅ Q40: Write a program to sort a list of numbers using a lambda function.

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

sorted_numbers = sorted(numbers, key=lambda x: x)


print(sorted_numbers)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]


# ✅ Q41: Write a program to sort a list of dictionaries based on a specific key.

people = [  

    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}

]


sorted_people = sorted(people, key=lambda x: x["age"])


print(sorted_people)  # [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 35}]


# ✅ Q42: Write a program to sort a list of strings by their length using a lambda function.

words = ["apple", "banana", "cherry", "date"]

sorted_words = sorted(words, key=lambda x: len(x))


print(sorted_words)  # ['date', 'apple', 'banana', 'cherry']


# ✅ Q43: Write a lambda function to calculate the product of two numbers.

product = lambda x, y: x * y

print(product(3, 4))  # 12


# ✅ Q44: Write a lambda function to filter out all odd numbers from a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))


print(filtered_numbers)  # [2, 4, 6, 8, 10]




# 📝 Bonus Practice Problems: DSA Concepts
# 🔥 Bonus
# ✅ Q45: Write a program to find the maximum subarray sum using Kadane’s algorithm.

# ✅ Q46: Write a program to implement binary search.

# ✅ Q47: Write a program to find the number of unique elements in a list using a set.

# ✅ Q48: Write a function to check if a given number is part of the Fibonacci sequence.

# ✅ Q49: Write a program to find the longest common prefix in a list of strings.

# ✅ Q50: Write a program to rotate a list to the right by k steps.



# ✅ Q45: Write a program to find the maximum subarray sum using Kadane’s algorithm.

def max_subarray_sum(nums):
    max_sum = float("-inf")
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum



print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6



# ✅ Q46: Write a program to implement binary search.

def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1



print(binary_search([1, 2, 3, 4, 5], 4))  # 3



# ✅ Q47: Write a program to find the number of unique elements in a list using a set.

def unique_elements(nums):
    return len(set(nums))


print(unique_elements([1, 2, 3, 2, 1]))  # 3



# ✅ Q48: Write a function to check if a given number is part of the Fibonacci sequence.


def is_fibonacci(num):
    a, b = 0, 1

    while a < num:
        a, b = b, a + b

    return a == num


print(is_fibonacci(5))  # True




# ✅ Q49: Write a program to find the longest common prefix in a list of strings.

def longest_common_prefix(strings):
    if not strings:
        return ""

    prefix = strings[0]

    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]

    return prefix



print(longest_common_prefix(["flower", "flow", "flight"]))  # fl



# ✅ Q50: Write a program to rotate a list to the right by k steps.

def rotate_list(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5]



