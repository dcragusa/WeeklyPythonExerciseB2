This week, we'll experiment with threads. Here's the basic idea: I want to count all of the words in all of the files that match a particular pattern. (We'll use `glob.glob` to retrieve the files matching that pattern.)

The idea is that I can invoke the function

    count_words('/foo/bar/*.txt')

and all of the words (i.e., strings separated by one or more whitespace characters) will be counted.

I want you to implement this twice:

- `count_words_sequential` goes through each of the matching files sequentially
- `count_words_threading` opens a thread for each of the files.

In order to implement the second version of `count_words`, you might need to learn a bit about how threading works in Python.  In particular, you'll want to use the `threading` library (and the `Thread` class within it), including the `start` and `join` methods.  You'll also probably want to use a `Queue` (in the `queue` module) to synchronize the information you've found so far.

The goal here is to count all of the words in all of the files that match the pattern, not to count the words in each separate file.  So if there are three `.txt` files in the `/foo/bar` directory, with 100, 200, and 300 words in them respectively, then you should print `600` as a final answer.
