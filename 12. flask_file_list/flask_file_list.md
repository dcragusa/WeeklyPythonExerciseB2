Two weeks ago, we created a function that returned a list of dictionaries, in which each dictionary described a 
file's timestamp and SHA-1. Last week, we modified that code (only slightly), using our own objects instead of lists 
and dicts. We also added a `rescan` method that let us compare the files in our directory with their previous versions.

This week, we're going to take our object and connect it to the Web. If you've never done Web development before, 
then I think that you're in for some fun.

The basic idea is this: We're going to create a simple Web application, using Flask, that will allow us to request 
the current status of files in a directory. One URL `/scan` will create an instance of our object for that 
directory, scan the files in it, and store that information (pickled) on disk.  A second URL `/rescan` will load 
the pickled version of our object, and will report what has changed since the last time.  Moreover, it'll give us 
this result in JSON.

Now, this is a big task for people who have never done Web development before, so I'm going to break this stuff into 
several parts.  If you have done Web development before, and especially if you've used Flask before, then you might 
find this week's exercise to be rather simple. 

This week, I want you to write a Web application using the Flask framework that accepts the `/scan` URL, plus a 
parameter, a directory name.  It should return a list of the files in that directory or (if the directory doesn't 
exist) an error message.

(And if you're wondering where our objects from last week have gone, the answer is... we'll connect them to this 
system next week.)

If you're new to Flask, have no fear!  It's a fairly simple way to get started with Web development. Great 
documentation, including a tutorial, is here: http://flask.pocoo.org/

In order to do this exercise, you'll need to:

- Download and install Flask
- Create a new Flask application
- Write a function that looks for the directory that was requested
- Connect that function to the URL /scan
- Have the function return a list of files or an indication that the directory doesn't exist.

There's no test for this week.  I'm afraid that I haven't quite figured out how to do testing in Flask, although it 
shouldn't (in theory) be that hard.
