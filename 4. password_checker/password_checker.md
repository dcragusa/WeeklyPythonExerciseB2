This week, we're going to create a function that can be used to create numerous password checkers. That is, our function will take four parameters: `min_uppercase`, `min_lowercase`, `min_punctuation`, and `min_digits`. These four parameters represent the minimum number of uppercase, lowercase, punctuation, and digits needed for a password to be considered good.

The output from this `create_password_checker` is a function, one which takes a potential password (string) as its input, and returns a two-element tuple: The first is a boolean value, indicating whether the password passed the validation test. The second element of the tuple is a dictionary whose keys are "uppercase", "lowercase", "punctuation", and "digits" and whose values represent by how much we've exceeded the minimum. If we haven't achieved the minimum, then the value will be a negative number.

For example, let's say that we want our passwords to contain at least 2 uppercase letters, at least 3 lowercase letters, at least 1 punctuation mark, and at least 4 digits.  We can create a new password-checking function as follows:

    pc1 = create_password_checker(2, 3, 1, 4)


Now let's check ourselves some passwords:

    print(pc1('Ab!1'))
    print(pc1('ABcde!1234'))


Here are the results:

    (False, {'uppercase': -1, 'lowercase': -2, 'punctuation': 0, 'digits': -3})
    (True, {'uppercase': 0, 'lowercase': 0, 'punctuation': 0, 'digits': 0})


We can see that the first password doesn't pass inspection, but that the second does. In the first case, we can see that 1 uppercase letter, 2 lowercase letters, and 3 digits were missing from what would otherwise been a good password.
