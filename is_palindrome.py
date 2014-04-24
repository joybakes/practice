'''This snippet tests for palindromes. 
I make the assumption that in the English language, characters in 
the middle of a string are less likely to be equal than characters
at the head and tail of a string. Therefore, I start my tests from
the middle and work my way out.
'''

import string

def pal_check(test_string,x,y):
  
  # Base case, if we have reached either end of the test_string and those match
  if x == 0 and y == len(test_string)-1 and test_string[x] == test_string[y]:
    return True

  # Test to equality of current values in the test_string
  elif test_string[x] == test_string[y]:
    x -= 1
    y += 1
    match = pal_check(test_string, x, y)
  
  # If equality fails, set our match to False
  else:
    match = False

  return match

def is_palindrome(test_string):
  # Remove punctuation
  test_string = test_string.translate(None, string.punctuation)
  # Remove whitespace
  test_string = test_string.translate(None, string.whitespace)
  # Set all characters to lower
  test_string = test_string.lower()

  # Test to see if our test_string is even or odd, so we know where the middle is.
  if len(test_string) % 2 == 0:
    return pal_check(test_string, len(test_string)/2-1, len(test_string)/2)
  else:
    return pal_check(test_string, (len(test_string)-1)/2-1, (len(test_string)-1)/2+1)


print is_palindrome("erica")
print is_palindrome("racecar")
print is_palindrome("aviddiva")
print is_palindrome("A car, a man, a maraca.")
print is_palindrome("12A car, a man, a maraca.21")