# Introduction to Python Programming

%%HTML
<div style="text-align: center">
<iframe width="560" height="315" src="https://youtube.com/embed/HjF98JryayQ" frameborder="0" allowfullscreen></iframe>

</div>

## Data Types and Variable Assignment

This is a Jupyter Notebook. It allows use to write text in Markdown format (as we have in this block), and also run Python code and see the output. If you have completed the previous workshop, you should be able to launch a Jupyter Notebook on your own machine. Make sure you have a conda environment activated (type `conda activate` in your terminal if you don't). Set up a new Notecook by typing `jupyter notebook` in a terminal window. This should launch Jupyter Notebooks running in your browser. 

    conda activate
    jupyter notebook

Start a new Python script in your `Python (data_science)` environment.

![](images/new_notebook.png)

Some of the most common data types in Python are integers (`int`) and floating point (`float`) for representing numbers, and strings (`str`) for representing text. We can assign values to variables - the data type is dynamically inferred by Python (in contrast to other languages such as C++ where they have to be explicitly declared). You can check what type a variable by using `type()`.

Try running the following two lines of Python code in your Jupyter Notebook.

my_name = "Andrew"
print(type(my_name))

In the output, you should see that the variable `my_name` has been identified as type `str` as it is contains text.

Assigning values to variables is a key component in scripting/coding. You can use variables to store values that you need to be able to access later, and variables can be re-assigned as your script progresses (maybe to store temporary values). You can print the content of a variable using the `print(variable_name)` function in Python. In the code below, we create two variables. The print() function can take multiple arguments so we can print the values of the two variables with the line `print(my_favourite_number_text, my_favourite_number)`.


my_favourite_number_text = "My favourite number is:"
my_favourite_number = 25
print(my_favourite_number_text, my_favourite_number)

How might you modify the above code so that it displays the following:
    
    My favourite number is 25.
    
Have a think and then click below for one way to do this.

```{admonition} Click the button to reveal answer
:class: dropdown 
    my_favourite_number_text = "is my favourite number."
    my_favourite_number = 25
    print(my_favourite_number, my_favourite_number_text)
```

You might have come up with a slightly different solution. It's important to remember there are often several (sometimes many) ways to achieve the same task - even in quite simple cases.