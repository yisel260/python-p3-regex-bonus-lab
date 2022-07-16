import re

'''
NOTE 1: There are many possible solutions to this lab. There are probably a
number of solutions better than the one suggested here. Extra consideration
should be awarded to students who manage to fit [Tt]oday into their RegEx.

NOTE 2: This lab can be solved using the OR `|` operator between the three
string literals. This should be discouraged, as it isn't truly a pattern.

NOTE 3: Using methods that generate match objects- `search()`, `match()`, and
`fullmatch()`- captures with parentheses `()` that are repeated using curly
braces `{}` are ideal. Unfortunately, when using `findall()`, patterns with
parentheses return lists of tuples instead of lists of strings. This is a dumb
feature, but one worth experiencing now rather than later on in their careers.
'''

my_pattern = r"[A-Z][a-z']{3,5}\s[a-z']{4,}\s[a-z']{1,}\s[a-z']{3,}\s[a-z]{2,}[\.,]?\s[a-z]{3,}[\.\?]"
my_regex = re.compile(my_pattern)
