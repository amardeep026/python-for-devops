# Loops in Python (for and while)

## Introduction

Loops are a fundamental concept in programming, and they allow you to perform repetitive tasks efficiently. In Python, there are two primary types of loops: "for" and "while."

## For Loop

The "for" loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a set of statements for each item in the sequence. The loop continues until all items in the sequence have been processed.

**Syntax:**

``
`python
for variable in sequence:
    # Code to be executed for each item in the sequence
```

**Example:**

```python
for color in in colors :
    # Code to be executed for each item in the collection
colors = ["red", "blue", "green"]
for color in colors:
    print(color)

```

**Output:**
```
red
blue
green

```

In this example, the loop iterates over the "fruits" list, and in each iteration, the "fruit" variable takes on the value of the current item in the list.

#### While Loop

The "while" loop continues to execute a block of code as long as a specified condition is true. It's often used when you don't know in advance how many times the loop should run.

**Syntax:**

```python
while condition:
    # Code to be executed as long as the condition is true
```

**Example:**

```python
number = 10
while number > 5:
    print(number)
    number -= 1

```

**Output:**

```
10
9
8
7
6

```

