# Exercise: Lists I

### Summary

Demonstrates some of the basic operations on lists of strings in
Python. Includes `join()`, `split()`, `append()`, `extend()`, `len()`,
and `sorted()`.

### Instructions

Create a new script called `oath.py` that does all of the following:

1. Creates a list variable called `oath` to first few words of the
    Athenian Oath in lower case: "we will ever strive for the ideals".
    To be clear, `oath` should be a list of strings for the individual words;
1. Uses the `len()` and `print()` to print a message that says `The length of the list is ` followed by the actual length;
1. Prints `oath`;
1. Uses the `join()` call to put the words in `oath` together to create a new variable called `oath_str`;
1. Prints `oath_str`;
1. Creates a new list called `oath_str_words` by using the `split()` call on `oath_str`;
1. Prints `oath_str_words`, which should be identical to `oath`;
1. Prints a blank line;  
1. Uses the `sorted()` call to create a new list called `sorted_oath`
   that is sorted in alphabetical order;
1. Then prints `sorted_oath`;
1. Creates `sorted_oath_str` that joins `sorted_oath` together, and print
    that out;
1. Prints a blank line;
1. Uses the `append()` call to add one word, "and", to `oath`;
1. Prints the updated version of `oath`;
1. Creates a string `more_oath_str` equal to "sacred things";
1. Uses `split()` to turn that into a list called `more_oath`;
1. Uses the `extend()` call to add `more_oath` to the end of `oath`;
1. Prints out `oath`.
1. Builds a new `oath_str` and prints it out.

If you aren't sure how to do some of these things, have a look at `demo.py` for some examples.

### Submitting

Once you're happy with everything and have committed all of the changes to
your local repository, please push the changes to GitHub. At that point,
you're done: you have submitted your answer.

### Tips

* You'll probably find you use `split()` and `join()` a lot: they're very useful for dealing with text.

* A handy way to get rid of extra
spaces in input text (say two or more spaces when you'd really like to have exactly one) is to split the string and then join the words
back together.
