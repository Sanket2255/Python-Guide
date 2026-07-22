#!/usr/bin/env python3
"""
Generates a single-file HTML Python learning guide.
Edit CHAPTERS below to add/change content, then run:  python3 generate.py
"""

import html

CHAPTERS = []

def chapter(cid, num, title, group, blocks, questions=None):
    CHAPTERS.append({
        "id": cid, "num": num, "title": title, "group": group,
        "blocks": blocks, "questions": questions or []
    })

def p(text): return ("p", text)
def h3(text): return ("h3", text)
def code(text): return ("code", text.strip("\n"))
def ul(items): return ("ul", items)
def note(kind, title, text): return ("note", (kind, title, text))
def table(headers, rows): return ("table", (headers, rows))

def q(num, text, inp=None, out=None):
    return {"num": num, "text": text, "in": inp, "out": out}

# ---------------------------------------------------------------------------
# 00 — Introduction
chapter("intro", "00", "What is Python?", "Start Here", [
    p("Python is a high-level, general-purpose programming language created by Guido van Rossum and released in 1991. It's known for readable syntax that looks close to plain English, which makes it a popular first language and also a workhorse for web backends, data science, automation, and AI."),
    h3("Compiled vs Interpreted"),
    p("A compiled language (C, C++, Rust) translates the entire program into machine code before it runs, so execution is fast but you don't see any output until the whole build succeeds. An interpreted language (Python, JavaScript, Ruby) reads and executes code line by line, which makes development faster to iterate on but typically runs slower than compiled code."),
    table(["Aspect", "Compiled", "Interpreted (Python)"], [
        ["Translation", "All at once, ahead of time", "Line by line, at runtime"],
        ["Speed", "Faster execution", "Slower execution"],
        ["Errors", "Caught before running", "Stops at first error hit"],
        ["Portability", "Needs a rebuild per platform", "Runs anywhere Python is installed"],
    ]),
    note("info", "Where Python fits", "The CPython interpreter reads your .py file top to bottom, converts it to bytecode, and executes it on the fly — which is why a Python script can crash partway through instead of failing all at once."),
], [
    q(1, "In your own words, explain the difference between a compiled and an interpreted language, and give one real example of each."),
    q(2, "Why do you think Python is a popular choice for beginners compared to a language like C++?"),
])

# 01 — Installation & first run
chapter("install", "01", "Installation & Running Python", "Basics", [
    p("Download Python from python.org (or use a package manager) and confirm the install from a terminal:"),
    code("""
python --version
# or on some systems:
python3 --version
"""),
    h3("Two ways to run code"),
    ul([
        "REPL (Read-Eval-Print Loop): type `python` in a terminal to get an interactive shell — great for quick tests.",
        "Script file: save code in a `.py` file and run it with `python filename.py`.",
    ]),
    code("""
# hello.py
print("Hello, Python!")

# run it:
# python hello.py
"""),
    note("warn", "Common first mistake", "Forgetting the .py extension, or running the file from a different folder than the one it's saved in, are the two most common reasons a beginner's 'python hello.py' fails with a file-not-found error."),
], [
    q(1, "Write and run a script that prints your name and today's weekday on two separate lines."),
    q(2, "What command checks which Python version is installed on your machine?"),
])

# 02 — Comments & Variables
chapter("comments-vars", "02", "Comments & Variables", "Basics", [
    p("Comments are notes for humans — Python ignores them completely. Variables are named boxes that hold values; Python figures out the type automatically when you assign one."),
    code("""
# This is a single-line comment

'''
This is a
multi-line comment (technically a string Python discards)
'''

name = "Aditi"      # string
age = 21            # integer
height = 5.6        # float
is_student = True   # boolean

print(name, age, height, is_student)
"""),
    h3("Naming rules"),
    ul([
        "Must start with a letter or underscore, never a digit.",
        "Can contain letters, digits, underscores — no spaces or symbols.",
        "Case-sensitive: `score` and `Score` are different variables.",
        "Convention: use snake_case for variable names (total_marks, not TotalMarks).",
    ]),
], [
    q(1, "Create three variables — your city, your age, and your favorite number — then print all three in one line."),
    q(2, "Which of these are valid variable names, and why: `2total`, `_total`, `total-marks`, `totalMarks`?"),
])

# 03 — Data Types
chapter("data-types", "03", "Data Types", "Basics", [
    p("Every value in Python has a type. The core built-in types are:"),
    table(["Type", "Example", "Description"], [
        ["int", "42", "Whole numbers"],
        ["float", "3.14", "Decimal numbers"],
        ["str", "\"hello\"", "Text"],
        ["bool", "True / False", "Logical values"],
        ["list", "[1, 2, 3]", "Ordered, changeable collection"],
        ["tuple", "(1, 2, 3)", "Ordered, unchangeable collection"],
        ["set", "{1, 2, 3}", "Unordered, unique values"],
        ["dict", "{\"a\": 1}", "Key-value pairs"],
        ["NoneType", "None", "Represents 'no value'"],
    ]),
    code("""
x = 10
print(type(x))        # <class 'int'>

y = "10"
print(type(y))        # <class 'str'>

print(x == int(y))    # True — value 10 equals 10 after conversion
"""),
], [
    q(1, "What does `type(3.0)` return, and how is it different from `type(3)`?"),
    q(2, "Given `value = None`, write a check that prints \"empty\" if value is None, else prints the value."),
])

# 04 — Strings & Type Conversion
chapter("strings", "04", "Strings & Type Conversion", "Basics", [
    p("Strings are sequences of characters. They support slicing, formatting, and a large set of built-in methods."),
    code("""
name = "Python"
print(name[0])          # P
print(name[-1])         # n
print(name[0:3])        # Pyt
print(name.upper())     # PYTHON
print(name.lower())     # python
print(len(name))        # 6
print(name.replace("Py", "My"))  # Mython

age = 21
message = f"I am {age} years old"   # f-string
print(message)
"""),
    h3("Type conversion"),
    code("""
print(int("42") + 8)     # 50
print(str(42) + "8")     # "428"
print(float("3.5") * 2)  # 7.0
print(int(3.9))          # 3 (truncates, doesn't round)
"""),
], [
    q(1, "Given `word = \"Programming\"`, print just \"gram\" using slicing."),
    q(2, "Convert the string \"15\" and the string \"4.5\" to numbers and print their sum."),
])

# 05 — Input, Output & Operators
chapter("io-operators", "05", "Input, Output & Operators", "Basics", [
    p("`input()` reads a line of text from the user (always as a string). `print()` writes output, and accepts multiple values plus a `sep` / `end` option."),
    code("""
name = input("What is your name? ")
print("Hello,", name, sep=" ", end="!\\n")
"""),
    h3("Operators"),
    table(["Category", "Operators", "Example"], [
        ["Arithmetic", "+ - * / // % **", "7 // 2 -> 3, 7 % 2 -> 1"],
        ["Comparison", "== != > < >= <=", "5 == 5 -> True"],
        ["Logical", "and or not", "True and False -> False"],
        ["Assignment", "= += -= *= /=", "x += 1"],
    ]),
], [
    q(1, "Take two numbers from the user and print their sum, difference, and product."),
    q(2, "Explain the difference between `/` and `//` with an example."),
])

# 06 — Conditional Statements
chapter("conditionals", "06", "Conditional Statements", "Control Flow", [
    p("`if` / `elif` / `else` let a program branch based on a condition."),
    code("""
marks = 72

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print(grade)   # C
"""),
    note("info", "Ternary shortcut", "`grade = \"Pass\" if marks >= 40 else \"Fail\"` packs a simple if/else into one line."),
], [
    q(1, "Write a program that checks if a number is positive, negative, or zero.", "-5", "Negative"),
    q(2, "Write a program that decides if a year is a leap year.", "2024", "Leap year"),
])

# 07 — Loops overview
chapter("loops-intro", "07", "Loops — Overview", "Control Flow", [
    p("Loops repeat a block of code. Python has two: `for` (iterate over a known sequence) and `while` (repeat while a condition holds). `break` exits a loop early, `continue` skips to the next iteration."),
    code("""
for i in range(3):
    if i == 1:
        continue   # skip printing 1
    print(i)        # prints 0, then 2

count = 0
while True:
    count += 1
    if count == 3:
        break
print(count)        # 3
"""),
], [
    q(1, "What's the difference between `break` and `continue`? Give a one-line example of each."),
])

# 08 — For loop
chapter("for-loop", "08", "For Loop", "Control Flow", [
    p("A `for` loop walks through any iterable — a range, a string, a list, and so on."),
    code("""
for i in range(1, 6):
    print(i, end=" ")          # 1 2 3 4 5

for ch in "abc":
    print(ch.upper())          # A B C (each on its own line)

fruits = ["apple", "banana", "mango"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
"""),
], [
    q(1, "Print all even numbers from 1 to 20 using a for loop.", "1 to 20", "2 4 6 ... 20"),
    q(2, "Print a right-angle triangle of stars using nested for loops.", "4", "*\n**\n***\n****"),
])

# 09 — While loop
chapter("while-loop", "09", "While Loop", "Control Flow", [
    p("A `while` loop repeats as long as its condition is true — useful when you don't know in advance how many times you'll loop."),
    code("""
n = 5
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)   # 120
"""),
    note("warn", "Infinite loops", "Forgetting to update the loop's condition variable (like `n -= 1` above) is the most common cause of a while loop that never ends."),
], [
    q(1, "Use a while loop to print the multiplication table of a given number up to 10.", "5", "5 10 15 ... 50"),
    q(2, "Use a while loop to reverse the digits of a number.", "1234", "4321"),
])

# 10 — Functions
chapter("functions", "10", "Functions", "Building Blocks", [
    p("A function is a reusable, named block of code. Parameters can have default values, and functions can return a value with `return`."),
    code("""
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Riya"))                 # Hello, Riya!
print(greet("Riya", "Good morning")) # Good morning, Riya!

def add(a, b):
    return a + b

result = add(4, 5)
print(result)   # 9
"""),
], [
    q(1, "Write a function `is_even(n)` that returns True if n is even, else False."),
    q(2, "Write a function `factorial(n)` that returns n! using a loop inside the function.", "5", "120"),
])

# 11 — Data structures overview
chapter("ds-intro", "11", "Data Structures — Overview", "Data Structures", [
    p("Python ships with four built-in collection types, each suited to a different job:"),
    table(["Type", "Ordered?", "Duplicates?", "Mutable?", "Use it for"], [
        ["list", "Yes", "Yes", "Yes", "A general-purpose sequence you'll modify"],
        ["tuple", "Yes", "Yes", "No", "A fixed sequence (like coordinates)"],
        ["set", "No", "No", "Yes", "Fast membership checks, removing duplicates"],
        ["dict", "Yes (3.7+)", "Keys: No", "Yes", "Looking values up by a key"],
    ]),
], [
    q(1, "You need to store a student's (name, roll_no) that should never change. Which data structure fits, and why?"),
])

# 12 — List
chapter("list", "12", "List", "Data Structures", [
    p("A list is an ordered, changeable collection that allows duplicates."),
    code("""
marks = [88, 92, 79, 92]
marks.append(100)          # [88, 92, 79, 92, 100]
marks.remove(79)           # [88, 92, 92, 100]
marks.sort()               # [88, 92, 92, 100]
print(marks[0], marks[-1]) # 88 100
print(len(marks))          # 4

squares = [x**2 for x in range(5)]   # list comprehension
print(squares)              # [0, 1, 4, 9, 16]
"""),
], [
    q(1, "Given `nums = [4, 2, 9, 1, 7]`, sort it in descending order without using `sort(reverse=False)` twice."),
    q(2, "Write a list comprehension that returns only the odd numbers from 1 to 20."),
])

# 13 — Tuple
chapter("tuple", "13", "Tuple", "Data Structures", [
    p("A tuple is like a list but immutable — once created, it can't be changed. That makes it useful for fixed data and slightly faster to iterate over."),
    code("""
point = (4, 7)
print(point[0], point[1])   # 4 7

# point[0] = 10   # would raise TypeError — tuples can't be modified

a, b = point                # unpacking
print(a, b)                 # 4 7
"""),
], [
    q(1, "Why might you choose a tuple over a list for storing latitude/longitude coordinates?"),
])

# 14 — Set
chapter("set", "14", "Set", "Data Structures", [
    p("A set stores unique, unordered values and is optimized for membership tests and mathematical set operations."),
    code("""
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # union -> {1,2,3,4,5,6}
print(a & b)   # intersection -> {3,4}
print(a - b)   # difference -> {1,2}

nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)
print(unique)  # {1, 2, 3}
"""),
], [
    q(1, "Given two lists of names, use sets to find the names common to both.", "['A','B','C'], ['B','C','D']", "{'B', 'C'}"),
])

# 15 — Dictionary
chapter("dict", "15", "Dictionary", "Data Structures", [
    p("A dictionary stores key-value pairs, letting you look up a value by its key instead of by position."),
    code("""
student = {"name": "Ishaan", "age": 20, "branch": "CSE"}

print(student["name"])          # Ishaan
student["age"] = 21             # update
student["cgpa"] = 8.7           # add new key

for key, value in student.items():
    print(key, "->", value)

print(student.get("email", "not set"))  # not set (safe lookup)
"""),
], [
    q(1, "Build a dictionary that counts how many times each character appears in a word.", "\"hello\"", "{'h':1,'e':1,'l':2,'o':1}"),
])

# 16 — Exception Handling
chapter("exceptions", "16", "Exception Handling", "Robust Code", [
    p("`try` / `except` catches errors at runtime so your program can handle them gracefully instead of crashing."),
    code("""
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That wasn't a valid number.")
except ZeroDivisionError:
    print("Can't divide by zero.")
else:
    print("Result:", result)
finally:
    print("Done processing.")
"""),
    note("info", "else vs finally", "`else` runs only if no exception was raised; `finally` always runs, whether an exception happened or not — useful for cleanup like closing a file."),
], [
    q(1, "Write a function that safely divides two numbers and returns \"undefined\" instead of crashing on division by zero.", "10, 0", "undefined"),
])

# 17 — File Handling
chapter("files", "17", "File Handling", "Robust Code", [
    p("The `with` statement opens a file and automatically closes it afterward, even if an error occurs."),
    code("""
# writing
with open("notes.txt", "w") as f:
    f.write("Learning Python\\n")
    f.write("File handling is useful.\\n")

# reading
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)

# appending
with open("notes.txt", "a") as f:
    f.write("One more line.\\n")
"""),
], [
    q(1, "Write code that reads a text file and prints only the lines that contain the word \"error\"."),
])

# 18 — OOP overview
chapter("oop-intro", "18", "OOP in Python — Overview", "OOP", [
    p("Object-Oriented Programming organizes code around objects — bundles of data (attributes) and behavior (methods) — rather than just a sequence of instructions. Python supports the four pillars of OOP: encapsulation, inheritance, polymorphism, and abstraction, covered chapter by chapter next."),
], [
    q(1, "In your own words, what's the difference between a class and an object?"),
])

# 19 — Classes
chapter("classes", "19", "Classes", "OOP", [
    p("A class is a blueprint for creating objects — it defines what attributes and methods every object of that type will have."),
    code("""
class Car:
    wheels = 4   # class attribute, shared by all cars

    def honk(self):
        return "Beep beep!"

print(Car.wheels)   # 4
"""),
], [
    q(1, "Define a class `Circle` with a class attribute `pi = 3.14` and a method `describe` that returns a fixed sentence."),
])

# 20 — Objects
chapter("objects", "20", "Objects", "OOP", [
    p("An object is a specific instance of a class, with its own data."),
    code("""
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "Red")
car2 = Car("Honda", "Blue")

print(car1.brand, car1.color)   # Toyota Red
print(car2.brand, car2.color)   # Honda Blue
"""),
], [
    q(1, "Create two `Car` objects with different brands and print both brand names."),
])

# 21 — Constructor
chapter("constructor", "21", "Constructor (__init__)", "OOP", [
    p("`__init__` runs automatically when an object is created, letting you set up its initial state."),
    code("""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print(f"{name}'s profile created.")

s1 = Student("Meera", 88)   # prints: Meera's profile created.
print(s1.marks)             # 88
"""),
], [
    q(1, "Add a default value for `marks` in the Student constructor so it's optional, defaulting to 0."),
])

# 22 — Attributes & Methods
chapter("attrs-methods", "22", "Attributes & Methods", "OOP", [
    p("Attributes are the data stored on an object; methods are functions defined inside a class that act on that data via `self`."),
    code("""
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

acc = BankAccount("Dev")
acc.deposit(500)
acc.withdraw(200)
print(acc.balance)   # 300
"""),
], [
    q(1, "Add a `transfer(self, other_account, amount)` method to `BankAccount` that moves money to another account."),
])

# 23 — Inheritance
chapter("inheritance", "23", "Inheritance", "OOP", [
    p("Inheritance lets one class (child) reuse and extend the attributes/methods of another (parent)."),
    code("""
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

for pet in [Dog("Rex"), Cat("Milo")]:
    print(pet.speak())
"""),
], [
    q(1, "Create a `Bird` class that inherits from `Animal` and overrides `speak` to return \"chirps\"."),
])

# 24 — Polymorphism
chapter("polymorphism", "24", "Polymorphism", "OOP", [
    p("Polymorphism means the same method name can behave differently depending on which object calls it — as seen with `speak()` in the previous chapter. It also shows up as built-in functions behaving differently per type, like `len()` working on strings, lists, and dicts alike."),
    code("""
print(len("hello"))        # 5
print(len([1, 2, 3, 4]))   # 4
print(len({"a": 1, "b": 2}))  # 2
"""),
], [
    q(1, "Write three classes — Square, Circle, Triangle — each with an `area()` method, then loop over a list of them calling `area()` on each."),
])

# 25 — Encapsulation
chapter("encapsulation", "25", "Encapsulation", "OOP", [
    p("Encapsulation bundles data with the methods that operate on it, and restricts direct access using naming conventions: a single underscore (`_x`) signals 'internal use', a double underscore (`__x`) triggers name-mangling for stronger protection."),
    code("""
class Account:
    def __init__(self, balance):
        self.__balance = balance   # 'private' attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

acc = Account(1000)
acc.deposit(500)
print(acc.get_balance())   # 1500
# print(acc.__balance)     # would raise AttributeError
"""),
], [
    q(1, "Explain why exposing `balance` directly (without a getter) could be risky in a banking application."),
])

# 26 — Abstraction
chapter("abstraction", "26", "Abstraction", "OOP", [
    p("Abstraction hides implementation details and exposes only what's necessary. Python provides `ABC` (Abstract Base Class) to force subclasses to implement specific methods."),
    code("""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h

# Shape()          # would raise TypeError — can't instantiate an abstract class
r = Rectangle(4, 5)
print(r.area())     # 20
"""),
], [
    q(1, "Add a `Circle(Shape)` class that implements `area()` using radius, and explain what happens if you forget to implement it."),
])

# 27 — Dunder Methods
chapter("dunder", "27", "Dunder (Magic) Methods", "OOP", [
    p("Double-underscore methods let your objects work with Python's built-in syntax — printing, addition, comparisons, and more."),
    code("""
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)          # Point(1, 2)  — thanks to __str__
print(p1 + p2)     # Point(4, 6)  — thanks to __add__
"""),
], [
    q(1, "Add an `__eq__` method to `Point` so that `Point(1,2) == Point(1,2)` returns True."),
])

# 28 — Advanced Topics
chapter("advanced", "28", "Advanced Topics", "Beyond the Basics", [
    h3("*args and **kwargs"),
    code("""
def total(*args):              # args becomes a tuple
    return sum(args)

def profile(**kwargs):         # kwargs becomes a dict
    for k, v in kwargs.items():
        print(f"{k}: {v}")

print(total(1, 2, 3, 4))       # 10
profile(name="Sara", age=22)
"""),
    h3("Comprehensions"),
    code("""
squares = [x**2 for x in range(5)]                  # [0, 1, 4, 9, 16]
evens_dict = {x: x**2 for x in range(5) if x % 2 == 0}  # {0:0, 2:4, 4:16}
"""),
    h3("Lambda, map, filter, zip"),
    code("""
square = lambda x: x ** 2
print(square(6))   # 36

nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))       # [2,4,6,8,10]
evens   = list(filter(lambda x: x % 2 == 0, nums)) # [2, 4]
pairs   = list(zip(["a", "b"], [1, 2]))            # [('a',1), ('b',2)]
"""),
    h3("Decorators & generators (a quick taste)"),
    code("""
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet():
    print("Hi!")

greet()   # Calling greet \\n Hi!

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)   # 3 2 1
"""),
], [
    q(1, "Write a function `describe(**kwargs)` that prints each keyword argument as \"key -> value\"."),
    q(2, "Write a generator function that yields the first n Fibonacci numbers.", "5", "0 1 1 2 3"),
    q(3, "Given a list of numbers, use `filter` and `lambda` to keep only numbers greater than 10.", "[4, 15, 8, 23, 2]", "[15, 23]"),
])

# ---------------------------------------------------------------------------
# Rendering

def esc(s):
    return html.escape(s, quote=False)

def render_block(block):
    kind, val = block
    if kind == "p":
        return f'<p>{esc(val)}</p>'
    if kind == "h3":
        return f'<h3>{esc(val)}</h3>'
    if kind == "code":
        return f'<pre><code class="language-python">{esc(val)}</code></pre>'
    if kind == "ul":
        items = "".join(f"<li>{esc(i)}</li>" for i in val)
        return f'<ul>{items}</ul>'
    if kind == "note":
        cls, title, text = val
        return (f'<div class="note note-{cls}"><div class="note-title">{esc(title)}</div>'
                f'<div class="note-text">{esc(text)}</div></div>')
    if kind == "table":
        headers, rows = val
        thead = "".join(f"<th>{esc(h)}</th>" for h in headers)
        tbody = "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in row) + "</tr>" for row in rows)
        return f'<table class="ref-table"><tr>{thead}</tr>{tbody}</table>'
    return ""

def render_questions(qs):
    if not qs:
        return ""
    items = []
    for item in qs:
        io = ""
        if item.get("in") or item.get("out"):
            io = '<div class="q-io">'
            if item.get("in"):
                io += f'<span class="q-in">Input: {esc(item["in"])}</span>'
            if item.get("out"):
                io += f'<span class="q-out">Output: {esc(item["out"])}</span>'
            io += '</div>'
        items.append(f'<div class="q-item"><div class="q-num">Q{item["num"]}</div>'
                      f'<div class="q-text">{esc(item["text"])}</div>{io}</div>')
    return f'<div class="questions"><h3>Practice Questions</h3>{"".join(items)}</div>'

def render_chapter(ch):
    body = "".join(render_block(b) for b in ch["blocks"])
    questions = render_questions(ch["questions"])
    return f'''
<section id="{ch["id"]}">
  <div class="chapter-header" data-num="{ch["num"]}">
    <div class="chapter-num">Chapter {ch["num"]}</div>
    <h1>{esc(ch["title"])}</h1>
  </div>
  <div class="content">
    <div class="section">{body}</div>
    {questions}
  </div>
</section>'''

def render_nav():
    groups = []
    seen = set()
    for ch in CHAPTERS:
        if ch["group"] not in seen:
            groups.append(ch["group"])
            seen.add(ch["group"])
    out = []
    for g in groups:
        out.append(f'<div class="nav-label">{esc(g)}</div>')
        for ch in CHAPTERS:
            if ch["group"] == g:
                out.append(f'<a href="#{ch["id"]}">{ch["num"]} &mdash; {esc(ch["title"])}</a>')
    return "\n".join(out)

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Python — A Practical Guide</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">
<style>
  :root {
    --teal: #0F766E;
    --teal-light: #F0FDFA;
    --teal-border: #99F6E4;
    --slate: #0F172A;
    --slate-mid: #475569;
    --slate-light: #64748B;
    --bg: #F8FAFC;
    --white: #ffffff;
    --amber: #B45309;
    --amber-light: #FFFBEB;
    --code-bg: #0F172A;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: "Inter", "Segoe UI", system-ui, sans-serif; background: var(--bg); color: var(--slate-mid); line-height: 1.7; }

  .sidebar { position: fixed; top: 0; left: 0; width: 260px; height: 100vh; background: var(--slate); overflow-y: auto; z-index: 100; padding-bottom: 40px; }
  .sidebar-logo { padding: 22px 20px 16px; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 8px; }
  .sidebar-logo h2 { color: white; font-size: 15px; font-weight: 700; }
  .sidebar-logo p { color: rgba(255,255,255,0.5); font-size: 11.5px; margin-top: 4px; }
  .nav-label { padding: 12px 20px 4px; color: rgba(255,255,255,0.35); font-size: 10px; font-weight: 700; letter-spacing: 1.4px; text-transform: uppercase; }
  .sidebar a { display: block; padding: 7px 20px; color: rgba(255,255,255,0.72); text-decoration: none; font-size: 12.8px; border-left: 3px solid transparent; }
  .sidebar a:hover, .sidebar a.active { background: rgba(255,255,255,0.08); color: white; border-left-color: var(--teal-border); }

  .main { margin-left: 260px; min-height: 100vh; }

  .cover { background: linear-gradient(135deg, #0F172A 0%, #134E4A 100%); min-height: 70vh; display: flex; align-items: center; justify-content: center; flex-direction: column; text-align: center; padding: 70px 40px; }
  .cover h1 { color: white; font-size: clamp(34px,6vw,60px); font-weight: 800; margin-bottom: 16px; }
  .cover h1 span { color: #5EEAD4; }
  .cover p { color: rgba(255,255,255,0.7); font-size: 16px; max-width: 480px; }

  .chapter-header { background: linear-gradient(135deg, var(--teal) 0%, #134E4A 100%); padding: 48px 56px 36px; position: relative; overflow: hidden; }
  .chapter-header::after { content: attr(data-num); position: absolute; right: 40px; top: 50%; transform: translateY(-50%); font-size: 100px; font-weight: 900; color: rgba(255,255,255,0.08); }
  .chapter-num { color: #5EEAD4; font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px; }
  .chapter-header h1 { color: white; font-size: clamp(24px,4vw,36px); font-weight: 800; position: relative; z-index: 1; }

  .content { padding: 40px 56px; max-width: 880px; }
  .section { background: white; border: 1px solid #E2E8F0; border-radius: 14px; padding: 26px 30px; border-left: 5px solid var(--teal); box-shadow: 0 2px 10px rgba(15,23,42,0.04); }
  .section h3 { color: var(--teal); font-size: 14.5px; font-weight: 700; margin: 18px 0 8px; }
  .section p { margin-bottom: 10px; font-size: 15px; }
  .section ul { padding-left: 20px; margin-bottom: 10px; }
  .section li { font-size: 14.5px; margin-bottom: 6px; }

  pre { background: var(--code-bg); border-radius: 10px; padding: 16px 20px; margin: 14px 0; overflow-x: auto; font-size: 13px; }
  pre code { font-family: "Fira Code", "Courier New", monospace; }

  .ref-table { width: 100%; border-collapse: collapse; margin: 14px 0; border-radius: 8px; overflow: hidden; }
  .ref-table th { background: var(--teal); color: white; padding: 10px 14px; text-align: left; font-size: 12.5px; }
  .ref-table td { padding: 9px 14px; border-bottom: 1px solid #E2E8F0; font-size: 13.5px; }
  .ref-table tr:nth-child(even) td { background: var(--teal-light); }

  .note { border-radius: 10px; padding: 14px 18px; margin: 14px 0; }
  .note-info { background: var(--teal-light); border-left: 4px solid var(--teal); }
  .note-warn { background: var(--amber-light); border-left: 4px solid var(--amber); }
  .note-title { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: var(--slate-light); margin-bottom: 4px; }
  .note-text { font-size: 14px; color: var(--slate); }

  .questions { background: var(--teal-light); border-radius: 12px; padding: 20px 24px; margin: 20px 0 0; }
  .questions h3 { color: var(--teal); margin-bottom: 14px; font-size: 14.5px; }
  .q-item { background: white; border: 1px solid var(--teal-border); border-radius: 8px; padding: 12px 16px; margin-bottom: 10px; }
  .q-item:last-child { margin-bottom: 0; }
  .q-num { color: var(--teal); font-weight: 800; font-size: 12px; margin-bottom: 4px; }
  .q-text { font-size: 13.5px; color: var(--slate); margin-bottom: 6px; }
  .q-io { display: flex; gap: 8px; flex-wrap: wrap; }
  .q-io span { background: #F1F5F9; border: 1px solid #E2E8F0; border-radius: 6px; padding: 3px 9px; font-family: monospace; font-size: 12px; }
  .q-in { color: var(--teal); }
  .q-out { color: #16A34A; }

  .closing { background: linear-gradient(135deg, #0F172A, #134E4A); padding: 50px 60px; text-align: center; color: rgba(255,255,255,0.8); font-size: 14px; }

  @media (max-width: 768px) {
    .sidebar { display: none; }
    .main { margin-left: 0; }
    .content, .chapter-header { padding-left: 22px; padding-right: 22px; }
  }
</style>
</head>
<body>

<nav class="sidebar">
  <div class="sidebar-logo">
    <h2>Python Guide</h2>
    <p>Personal learning notes</p>
  </div>
  <a href="#cover">Cover</a>
__NAV__
</nav>

<div class="main">

<section id="cover" class="cover">
  <h1>Python<br><span>A Practical Guide</span></h1>
  <p>From your first line of code to object-oriented programming — with practice questions at every step.</p>
</section>

__CHAPTERS__

<div class="closing">
  <p>Built as a personal reference — edit any chapter in <code>generate.py</code> and re-run it to update this page.</p>
</div>

</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js"></script>
<script>
  hljs.highlightAll();

  const sections = document.querySelectorAll("section[id]");
  const links = document.querySelectorAll(".sidebar a");
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        links.forEach(a => a.classList.remove("active"));
        const a = document.querySelector(`.sidebar a[href="#${e.target.id}"]`);
        if (a) a.classList.add("active");
      }
    });
  }, { threshold: 0.25 });
  sections.forEach(s => io.observe(s));
</script>
</body>
</html>
"""

def main():
    nav = render_nav()
    chapters_html = "\n".join(render_chapter(ch) for ch in CHAPTERS)
    html_out = TEMPLATE.replace("__NAV__", nav).replace("__CHAPTERS__", chapters_html)
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html_out)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_out)
    print(f"Generated output.html and index.html — {len(CHAPTERS)} chapters")

if __name__ == "__main__":
    main()
