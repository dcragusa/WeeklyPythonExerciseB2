Last week, we created a simple Flask application, in which the user could pass (via the URL) the name of a 
directory. Our Web application took input from the user via the query string, and returned text based on the 
content of the query string.

This week, we'll connect our Flask application with our FileList class.  The idea is as follows:
- When a user visits the `/scan` URL, and passes a directory name via the query string, the directory is scanned.
- After the directory is scanned, its contents should be pickle stored to disk, replacing `/` characters in the 
    path with `-` characters.
- When a user visits the `/rescan` URL and passes a directory name, there are three basic possible outcomes:
    - It's not a directory, in which case we'll give an error message.
    - It's a directory we've never mentioned or scanned before, in which case it'll give an error message.
    - It's a directory we have scanned before.  We open the pickle file for the named directory, and then use the 
        `FileList` object to produce a report of which files have been added, changed, or removed for the user.
