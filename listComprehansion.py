#1. Squares from 1 to 10
sqr = [x**2 for x in range(1, 11)]
print(sqr)

#2. Even numbers between 1 and 50
even = [x for x in range(1, 51) if x % 2 == 0]
print(even)

#3. Convert all strings to uppercase
words = ["apple", "banana", "cherry"]
upper_words = [w.upper() for w in words]
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
flat = [item for sublist in matrix for item in sublist]
print(flat)

#8. Replace negative numbers with 0
nums = [-3, 5, -1, 8]
updated = [x if x >= 0 else 0 for x in nums]
print(updated)

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
table = [[i*j for j in range(1, 6)] for i in range(1, 6)]
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
add = lambda a, b: a + b
print(add(5, 3))

#2.Check if number is even
is_even = lambda x: x % 2 == 0
print(is_even(4))

#3.Get last character
last_char = lambda s: s[-1]
print(last_char("Python"))

#4.Square list using map()
nums = [1,2,3,4]
squares = list(map(lambda x: x**2, nums))
print(squares)

#5.Get odd numbers using filter()
nums = [1,2,3,4,5]
odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)

#6.Sort tuples by second value
data = [(1,5), (2,3), (4,1)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

#7.Check palindrome
is_palindrome = lambda s: s == s[::-1]
print(is_palindrome("NITIN"))

#8.Maximum of three numbers
maximum = lambda a,b,c: max(a,b,c)
print(maximum(10,25,15))

#9. Reverse a string
reverse = lambda s: s[::-1]
print(reverse("Python"))

#10. Convert list of strings to integers
strings = ["1","2","3"]
nums = list(map(lambda x: int(x), strings))
print(nums)