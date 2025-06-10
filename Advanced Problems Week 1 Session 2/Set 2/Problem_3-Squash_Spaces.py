# Problem 3: Squash Spaces
# Write a function squash_spaces() that takes in a string s
# as a parameter and returns a new string with each substring
# with consecutive spaces reduced to a single space.
# Assume s can contain leading or trailing spaces,
# but in the result should be trimmed. 
# Do not use any of the built-in trim methods.

def squash_spaces(s):
    s_split = s.split()
    return " ".join(s_split)

s = "   Up,     up,   and  away! "
print(squash_spaces(s))

s = "With great power comes great responsibility."
print(squash_spaces(s))
# Example Output:

# "Up, up, and away!"
# "With great power comes great responsibility."