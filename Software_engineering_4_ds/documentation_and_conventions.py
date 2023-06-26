def test():
    """
    This is a test function
    :return: None
    """
    return None

test.__doc__ #podemos lllamar la documentacion

### Code is read ucho more often than is written


############################################
#Using pycodestyle
#We saw earlier that pycodestyle can be run from the command line to check a file for PEP 8
#  compliance. Sometimes it's useful to run this kind of check from a Python script.
# In this exercise, you'll use pycodestyle's StyleGuide class to check multiple files for
#  PEP 8 compliance. Both files accomplish the same task, but they differ greatly in 
# formatting and readability. You can view the contents of the files by following their
#  links below.
############################################

# Import needed package
import pycodestyle

# Create a StyleGuide instance
style_checker = pycodestyle.StyleGuide()

# Run PEP 8 check on multiple files
result = style_checker.check_files(['nay_pep8.py', 'yay_pep8.py'])

# Print result of PEP 8 style check
print(result.messages)


############################################
#Conforming to PEP 8
#As we've covered, there are tools available to check if your code conforms to the PEP 8
#  guidelines. One possible way to stay compliant is to use an IDE that warns you when you
#  accidentally stray from the style guide. Another way to check code is to use the 
# pycodestyle package.
# The results below show the output of running pycodestyle check against the code shown in
#  your editor. The leading number in each line shows how many occurrences there were of
#  that particular violatio
############################################

# my_script.py:2:2:  E225 missing whitespace around operator
# my_script.py:2:7:  E231 missing whitespace after ','
# my_script.py:2:9:  E231 missing whitespace after ','
# my_script.py:5:7:  E201 whitespace after '('
# my_script.py:5:11: E202 whitespace before ')'


# Assign data to x
x = [8, 3, 4]

# Print the data
print(x)


############################################

# my_script.py:2:15: E261 at least two spaces before inline comment
# my_script.py:5:16: E262 inline comment should start with '# '
# my_script.py:11:1: E265 block comment should start with '# '
# my_script.py:13:2: E114 indentation is not a multiple of four (comment)
# my_script.py:13:2: E116 unexpected indentation (comment)

############################################

def print_phrase(phrase, polite=True, shout=False):
    if polite:  # It's generally polite to say please
        phrase = 'Please ' + phrase

    if shout:  # All caps looks like a written shout
        phrase = phrase.upper() + '!!'

    print(phrase)


# Politely ask for help
print_phrase('help me', polite=True)
# Shout about a discovery
print_phrase('eureka', shout=True)
