#!/usr/bin/python -tt
"""
doc
"""

import sys

# Define a main() function that prints a little greeting.
def main():
    # print 'Hello world'
    if len(sys.argv) > 1:
        sys.exit(2);
        print repeat('Hello', False)
    print repeat('Yah', True)

def repeat(s, exclaim):
    """
    Repeat the String 's' three times,
    If the exclaim is true, it will add ! at the end
    """
    result = s * 3 #append s back to back three times.
    if exclaim:
        result = result + '!!!'
    return result

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()


