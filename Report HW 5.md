# Homework 05 Report
# Kelsey Edinborough
# Fall 2024

1. What does the `in` operator do? Provide examples of the `in` using strings and lists (or tuples). The 'in' operator checks to see if a certain element that you ask for is in the string, list, or tuple that you are searching for. It returns True if it does and False if it does not contain that element. 


One example from the homework is: 

        if all_caps_filter in all_caps_movie_title:
            return True
        else:
            return False

This checks to see if the  filter title is in the movie title and returns true if yes and false if no. 

Another example is: 

    list1= [3, 5, 9]
    if 3 in list1:
        print("yes")
    else: 
        print("false") 
   
2. Taking a moment to research, why would one want to use .casefold() instead of .lower() in python when comparing strings? Please include the reference on where you find the information. One might want to use .casefold() instead of .lower() because .casefold() recognizes characters outside of the ASCII table as well, meaning it can convert more characters to lowercase than .lower() can, which makes it more universal and efficient. (GeeksforGeeks, 2023)
   

3. For each of the three sequential types you have learned (list, string, tuple) - label as mutable or immutable (refer to the team activity).
   * string - immutable 
   * list - mutable 
   * tuple - immutable 

4. Explain mutability and immutability in your own words. Immutability means you can't change somethings contents and mutability means you can change the contents for example you can take away parts, or you can add elements, or you can directly replace elements.  

5. Given the following code:

    ```python
    def mystery_function(x):
        x = 100

    x = 1
    print(x)
    mystery_function(x)
    print(x)
    ```

* What is the output of the code above?

  1

  1
* Explain why the output is what it is. 
When moving through the code it defines mystery_function. Then it states x = 1 and calls it to print(x), so the code outputs 1. Then mystery_function is called and there is return so there is nothing that is outputted. Then it calls print(x) again, so another 1 is printed. 


6. Given the following code:

    ```python
    def mystery_function(x):
        x[0] = 100

    x = [1, 2, 3]
    print(x)
    mystery_function(x)
    print(x)
    ```
* What is the output of the code above? 

[1, 2, 3]

[100, 2, 3]

* Explain why the output is what it is. 
Mystery_function(x) is defined. Then x is set to [1, 2, 3], so when the next line calls print(x), [1,2,3] is printed. Then mystery_function is called where x[0] is set to 100. Therefore, 100 replaced 1 in the set [1,2,3], making the new output for print(x), [100,2,3]. 

7. Would happen if `x` was a tuple? What is generated when you try to run the code above with a tuple?

    ```
    TypeError: 'tuple' object does not support item assignment


    ```


8. Given the following code:

    ```python
    def mystery_function(x):
        x[1][0] = 100

    x = (3, [1, 2, 3], [4, 5, 6])
    print(x)
    mystery_function(x)
    print(x)
    ```

* What is the output of the code above?

    (3, [1, 2, 3], [4, 5, 6])

    (3, [100, 2, 3], [4, 5, 6])


## Deeper Thinking

We talked a lot about immutable and mutable. Why would this matter? Take a moment to describe in your own words why computers would care. Pay particular attention to how computers store data in memory, and how making something immutable may help with that storage. Immutable objects are easier for the computer to handle in terms of memory because the storage needed is set up front. Whereas mutable objects can take up an indefinite amout of space for a computer because it can be continuously changed. Immutable objects are more reliable in terms of coding because something is not being frequently changed in the computer. (Tul Maria, 2021)