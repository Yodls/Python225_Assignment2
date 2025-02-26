# Python225_Assignment2

15.10.2. Exercise from https://allendowney.github.io/ThinkPython/chap15.html#exercises

In the previous chapter, a series of exercises asked you to write a Date class and several functions that work with Date objects. Now let’s practice rewriting those functions as methods.

    Write a definition for a Date class that represents a date – that is, a year, month, and day of the month.

    Write an __init__ method that takes year, month, and day as parameters and assigns the parameters to attributes. Create an object that represents June 22, 1933.

    Write __str__ method that uses an f-string to format the attributes and returns the result. If you test it with the Date you created, the result should be 1933-06-22.

    Write a method called is_after that takes two Date objects and returns True if the first comes after the second. Create a second object that represents September 17, 1933, and check whether it comes after the first object.

Hint: You might find it useful write a method called to_tuple that returns a tuple that contains the attributes of a Date object in year-month-day order.
