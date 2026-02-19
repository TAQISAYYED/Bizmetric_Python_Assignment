#1. Squares from 1 to 10
sqr = [x**2 for x in range(1, 11)]
print(sqr)

#2. Even numbers between 1 and 50
even = [x for x in range(1, 51) if x % 2 == 0]
print(even)

#3. Convert all strings to uppercase
Words = ["apple", "banana", "cherry"]
upper_words = [W.upper() for W in Words]
print(upper_words)

#4. Only positive numbers
nums = [-5, 3, -2, 7, 0, 9]
positive = [x for x in nums if x > 0]
print(positive)

#5. List of tuples (num, num²) from 1 to 5
tuples = [(x, x**2) for x in range(1, 6)]
print(tuples)

#6. Extract vowels from string
string = "List Comprehension"
vowels = [ch for ch in string if ch.lower() in "aeiou"]
print(vowels)

#7. Flatten 2D list
matrix = [[1,2], [3,4], [5,6]]
flat = [x for y in matrix for x in y]
print(flat)

#8. Replace negative numbers with 0
nums = [-3, 5, -1, 8]
updatenum = [x if x >= 0 else 0 for x in nums]
print(updatenum)

#9. Length of each word
words = ["Python", "Java", "SQL"]
lengths = [len(w) for w in words]
print(lengths)

#10. Filter words starting with A or a
words = ["Apple", "banana", "Avocado", "grape"]
filtered = [w for w in words if not w.lower().startswith('a')]
print(filtered)

#11. Even or Odd labels
nums = [1,2,3,4,5]
labels = ["even" if x % 2 == 0 else "odd" for x in nums]
print(labels)

#12. Numbers divisible by 3 and 5 (1–100)
nums = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(nums)

#13. Multiplication table (1–5)
table = [[i*j for j in range(1, 6)] for i in range(1, 11)]
print(table)

#14. Dictionary keys to list
d = {"a":1, "b":2, "c":3}
keys = [k for k in d.keys()]
print(keys)

#15. Extract digits from string
string = "abc123xyz45"
digits = [ch for ch in string if ch.isdigit()]
print(digits)

#16. Remove spaces from string
string = "Hello World Python"
no_space = [ch for ch in string if ch != " "]
print("".join(no_space))

#17. Characters appearing more than once
string = "programming"
duplicates = [ch for ch in set(string) if string.count(ch) > 1]
print(duplicates)

#18. All words from list of sentences
sentences = ["Hello world", "Python is easy"]
words = [word for sentence in sentences for word in sentence.split()]
print(words)

#19. Unique elements from list
nums = [1,2,2,3,4,4,5]
unique = [x for i,x in enumerate(nums) if x not in nums[:i]]
print(unique)

#20. Cartesian Product
A = [1,2]
B = [3,4]
pairs = [(x,y) for x in A for y in B]
print(pairs)

#1.Add two numbers
add = lambda x , y : x+y
print(add(10,20))
#2.Check if number is even
iseven = lambda x : x % 2 == 0
print(iseven(11))

#3.Get last character
last = lambda x :x == x[-1]
print(last)

#4 .Square list using map()
nums = [1,2,3,4]
squares = list(map(lambda x: x**2, nums))
print(squares)

#5 .Get odd numbers using filter()
nums = [1,2,3,4,5]
odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)

#6.Sort tuples by second value
data = [(1,5), (2,3), (4,1)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

#7 .Check palindrome
is_palindrome = lambda s: s == s[::-1]
print(is_palindrome("NITIN"))

#8. Maximum of three numbers
maximum = lambda a,b,c: max(a,b,c)
print(maximum(10,25,15))

#9.  Reverse a string
reverse = lambda s: s[::-1]
print(reverse("Python"))

#10. Convert list of strings to integers
strings = ["1","2","3"]
nums = list(map(lambda x: int(x), strings))
print(nums)

# 11. Use lambda with filter() to remove empty strings from a list. 
list1 = ['','taqi' , 'farhan']
remove1 = list1(filter(lambda x : x.isnull() ))
# 12. Use lambda to compute factorial using reduce() (yeah, that one-liner 
# madness). 
from functools import reduce
fact = lambda n: reduce(lambda x, y: x * y, range(1, n+1))
print(fact(5))

# 13. Write a lambda that returns the larger of two numbers.
larger = lambda x,y : max(x,y)
larger(9,5)
# 14. Use lambda to check if number is divisible by 5. 
div5 = lambda  x : x % 5 == 0
div5(10)
# 15. Use lambda + map() to add 10 to each element of a list. 
numbers = [1, 2, 3, 4]
add10 = list(map(lambda x: x + 10, numbers))
print(add10)
# 16. Use lambda to sort a list of dictionaries by a key (like "age"). 
people = [
    {"name": "Ali", "age": 25},
    {"name": "Sara", "age": 20},
    {"name": "John", "age": 30}
]
sorted_list = sorted(people, key=lambda x: x["age"])
print(sorted_list)
# 17. Write a lambda that returns True if a character is a vowel. 
vowel = lambda x : x.upper() in ['A','E','I','O','U']
vowel('e')
# 18. Use lambda + filter to extract words of length > 5 from a list.
words = ["apple", "banana", "cat", "elephant"]
result = list(filter(lambda x: len(x) > 5, words))
print(result)
# 19. Use lambda to calculate the area of a circle (πr²). 
area = lambda r: 3.14 * r * r
print(area(5))
# 20. Write a lambda to remove duplicates from a list using filter + set.
numbers = [1,2,2,3,4,4,5]
result = list(filter(lambda x: True, set(numbers)))
print(result) 
# 21. Use lambda with reduce() to find the product of all numbers in a list.
numbers = [1,2,2,3,4,4,5]
result = list(filter(lambda x: True, set(numbers)))
print(result)
# 22. Write a lambda that returns absolute value of a number. 
abs_val = lambda x: x if x >= 0 else -x
print(abs_val(-10))
# 23. Use lambda to sort a list of strings by their length. 
words = ["apple", "kiwi", "banana"]
result = sorted(words, key=lambda x: len(x))
print(result)
# 24. Use lambda to get only uppercase characters from a string. 
text = "HeLLo WoRLd"
result = list(filter(lambda x: x.isupper(), text))
print(result)
# 25. Write a lambda that returns the square if number is even, cube if odd. 
numbers = [11, 31, 40, 50]
result = list(map(lambda x: x**2 if x%2==0 else x**3, numbers))
print(result)
# 26. Use lambda with map to convert Celsius to Fahrenheit. 
number = [10 , 30, 40 , 50]
arr = list(map(lambda x : (x * 9/5)+32 ,number))
print(arr)
# 27. Write a lambda to check if two strings are anagrams. 
anagram = lambda a, b: sorted(a) == sorted(b)
print(anagram("listen", "silent"))
# 28. Use lambda to extract only numeric values from a mixed list. 
data = [10, "hi", 20, "hello", 30]
result = list(filter(lambda x: isinstance(x, (int,float)), data))
print(result)
# 29. Use lambda inside any() to check if any list element is negative.
numbers = [10, 20, -5, 30]
result = any(map(lambda x: x < 0, numbers))
print(result)
# 30. Use lambda to generate a function that multiplies any number by 
multiply = lambda n: lambda x: x * n
double = multiply(2)
print(double(10))
