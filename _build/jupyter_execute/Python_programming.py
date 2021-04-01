# Introduction to Python Programming

In this second workshop we'll take our first look at programming in Python. We'll cover the key data types, as well as functions, and control flow statements. 

%%HTML
<div style="text-align: center">
<iframe width="560" height="315" src="https://youtube.com/embed/HjF98JryayQ" frameborder="0" allowfullscreen></iframe>

</div>

## Slides

You can view and download the slides in a variety of formats by clicking on the image below.

<center>

[![link_to_slides](images/intro_slides.png)](https://docs.google.com/presentation/d/1yWZ8Q_MD4RGkeqDTDukaS7T18oX08BmONcaLwZNAAKk/edit?usp=sharing)
    
</center>

## Data Types and Variable Assignment

This is a Jupyter Notebook. It allows use to write text in Markdown format (as we have in this block), and also run Python code and see the output. If you have completed the previous workshop, you should be able to launch a Jupyter Notebook on your own machine. Make sure you have a conda environment activated (type `conda activate` in your terminal if you don't). Set up a new Notecook by typing `jupyter notebook` in a terminal window. This should launch Jupyter Notebooks running in your browser. 

    conda activate
    jupyter notebook

Start a new Python script in your `Python (data_science)` environment.

![](images/new_notebook.png)

Some of the most common data types in Python are integer (`int`) and floating point (`float`) for representing numbers, and strings (`str`) for representing text. We can assign values to variables - the data type is dynamically inferred by Python (in contrast to other languages such as C++ where they have to be explicitly declared). You can check what type a variable is by using `type()`.

Try running the following two lines of Python code in your Jupyter Notebook.

my_name = "Andrew"
print(type(my_name))

In the output, you should see that the variable `my_name` has been identified as type `str` as it is contains text.

Assigning values to variables is a key component in scripting/coding. You can use variables to store values that you need to be able to access later, and variables can be re-assigned as your script progresses (maybe you want to store temporary values in a variable). You can print the content of a variable using the `print(variable_name)` function in Python. In the code below, we create two variables. The `print` function can take multiple arguments so we can print the values of the two variables with the line `print(first_variable_name, second_variable_name)`.


my_favourite_number_text = "My favourite number is:"
my_favourite_number = 25
print(my_favourite_number_text, my_favourite_number)

How might you modify the above code so that it displays the following:
    
    25 is my favourite number.


```{admonition} Click the button to reveal answer
:class: dropdown 
    my_favourite_number = 25
    my_favourite_number_text = "is my favourite number."
    print(my_favourite_number, my_favourite_number_text)
```

You might have come up with a slightly different solution. It's important to remember there are often several (sometimes many) ways to achieve the same task - even in quite simple cases.

Let’s now assign a different number to the `my_favourite_number` variable and change the `my_favourite_number_text` back to what it was originally.

my_favourite_number = 16
my_favourite_number_text = "My favourite number is:"
print(my_favourite_number_text, my_favourite_number)

## Lists

Lists can be assigned to variables. In Python lists are indicated by square brackets, `[` and `]`, and contain elements - often of the same type - for example, lists of integers, strings etc. Lists can also contain a mix of elements of different types (but you may want to avoid this). The next bit of code creates a list called `my_numbers` that contains 4 integer elements. Remember, in contrast to R, Python uses zero-position indexing. So the first element in the list is at position 0, the second at position 1 etc. We can index an element in the list using square brackets. Let's index the second element...

my_numbers = [10, 20, 30, 40]
my_numbers[1]

The next list is a list of strings. How would you go about indexing the fourth element?

my_names = ["Andrew", "Suzanne", "Eliza", "Seb"]

```{admonition} Click the button to reveal answer
:class: dropdown 
    my_names[3]
```

Elements in lists can be changed (i.e., lists are mutable):

my_names[0] = "Iggy Pop"
print(my_names)

List can be sliced using `:` The following will slice from the third element to the end of the list.

my_names[2:]

While the line below will slice from the start of the list up to (but *excluding*) the third element.

my_names[:2]

We can also specify the start and stop points of the slicing as follows.

my_names[1:3]

## Tuples

Tuples are like lists, except they are *immutable* - in other words, their contents cannot be changed later. While lists are created using square brackets, tuples are created using round brackets. But like lists, you use square brackets to reference elements in a tuple.

my_tuple = (10, 20, 30, 40)
my_tuple[3]

If you try to change an element in a tuple, an error will be generated.

my_tuple[3] = 5

Tuples can be sliced too. The following will slice from the start up to (but excluding) the fourth element.

my_tuple[:3]

How would you slice `my_tuple` so that it contains only the second and third elements?

```{admonition} Click the button to reveal answer
:class: dropdown 
    my_tuple[1:3]
```

If you wanted to, you could map the above output onto a new variable called `my_slided_tuple` and use the logical operator `==` (more on this later) to check that they are the same.

my_sliced_tuple = my_tuple[:3]
my_sliced_tuple == my_tuple[:3]

## Arrays

An array is a data structure consisting of a collection of elements, each identified by at least one array index (or key). Arrays are core data structures in data science and machine learning. For example, you can store images as 2-dimensional arrays representing pixel brightness across the area of the image.

Data frames and tibbles in R are types of 2-dimensional arrays - data stored in rectangular format with rows and columns. Arrays don’t have to just be in two dimensions but it can be tricky imagining more dimensions...

NumPy Arrays are better than inbuilt Python Arrays in that they are more efficient as the arrays grow larger in size. We'll spend more time on NumPy arrays in the next workshop but let's just take a brief look.

In the code below we’re importing the `numpy` package as `np` (this is the conventional alias for this package). We then set our randomisation seed to ensure reproduciblity. Remember, computers can't generate true random numbers so use an algorithm. We can fix the start of this generation procedure to ensure that if we re-run our code we get the same random numbers. We then create an array of random integers from 0 (inclusively) and 10 (exclusively) that has 3 rows and 4 columns. We use the Numpy routine `random` and the operation `randint` to generate this array. We need to specify the low and high values of the range we're sampling from, and the shape of the array (number of rows by number of columns) we are wanting to generate.

import numpy as np

np.random.seed(1234)
my_array = np.random.randint(low = 0, high = 10, size = (3, 4))
my_array


We can then check the shape of the array using `.shape` 

my_array.shape

## Getting Help

In your Jupyter Notebook you can type `help()` and put in the brackets the name of the module and function you want help with. Most help files are incredibly useful and will clearly describe what a function does, what it takes as its input parameters, and what it returns in its output. Below is what I get when I ask for help with the `shape` operation in `numpy`.

help(np.shape)

## Variable Assignments are References (not Copies)

Assignment in Python involves creating bindings between a target and an object in computer memory - not just simple copying - this can easily trip you up if you assume that assignment creates a new **copy** of of the original object.

my_old_names = ['Andrew', 'Suzanne', 'Eliza', 'Seb']
my_new_names = my_old_names

print(my_new_names)

my_old_names[0] = 'this is surprising'

print(my_new_names)

## Functions

Python has a number of built-in functions such as print(), abs(), bin() etc. You can see the full list [here](https://docs.python.org/3/library/functions.html). Generally, functions take an input, do something with the input, and then output the result. You can use the `help()` function to get help on other functions. 


help(print)

## User-Defined Functions

If you find yourself writing the same chunk of code again and again, you might want to turn it into a function. For example, imagine I want to display someone’s BMI on the basis of knowing their height (in metres) and mass (in kg). The formula for BMI is: BMI = kg/m2. Let’s write a function that takes as its input someone’s weight and height, and then returns their BMI. We use `def` to define our function that we're calling `bmi`. It takes two parameters, `weight` and `height`. Inside the body of the function it creates a new variable called `bmi_value` which is `weight` divided by `height` squared. The function then returns this value.

We can then call the function to work out the bmi of someone with a weight of 87 kgs, and a height of 1.8 metres with with `bmi(87, 1.8)`.

Note that in the code below we are using indentation for the body of the function. Indentation in Python is important and is meaningful (i.e., it's not an aesthetic decision). Indentation is used to indicate a block of code. The convention is to indent each line of a block by 4 spaces. 

def bmi(weight, height):
    bmi_value = weight/(height*height)
    return bmi_value

bmi(87, 1.8)

## Control Flow Statements - For Loops

We can run the same command or chunk of code any number of times by placing it within a for loop. In the following, we print the phrase `“Hello world!”` five times. In Python, the code block within the loop that is to be repeated needs to indented.

for i in range(0, 5):
    print("Hello world!")

We can also iterate over elements in an array using a for loop. In the following example, we iterate through the elements in our list and print that element.

my_names = ['Andrew', 'Suzanne', 'Eliza', 'Seb']

for element in my_names:
    print(element)

### Iterating Over an Array

In the same way we can iterate over lists, we can iterate over arrays row-by-row.  Let’s create a 2-dimensional array called `vital_stats` with the weights and heights of three individuals. The first row of the array will be their weights, and the second row their heights.

weights = np.array([80, 60, 90])
heights = np.array([1.8, 1.65, 1.75])
names = np.array(['Iggy', 'David', 'Lou'])
vital_stats = np.array((weights, heights, names))

print(vital_stats)

We see that in a for loop we can iterate over the rows in our array. 

for index in vital_stats:
    print(index)

What we really want to do is iterate over column.  Luckily there is a Transpose attribute built into NumPy arrays that produces the transposed array (i.e., columns and rows swapped).

for index in vital_stats.T:
    print(index)

We can cycle through the rows of this transposed array (with the rows now corresponding to the weight, height and name of each individual), and pass these values to the `bmi` function that we wrote. Each person’s weight is in column 0 of the array, and each person’s height in column 1. Their name is in column 2. The following loop cycles through our NumPy array person by person and calls the `bmi` function for each person in the array before printing out the result (rounded to zero decimal places using the `round` function). Note that the elements in the array we have created are all of type `str` as this is the only way to represent the elements as being of the same type (which is a requirement of NumPy arrays). We can convert each number that is currently of type `str` to a number with `float` so that we can pass it to the `bmi` function. 

for person in vital_stats.T:
    weight = float(person[0])
    height = float(person[1])
    print(person[2], 'has a BMI of', round(bmi(weight, height)))



