import itertools

# Known first half of the password
first_half = "discourse"

# List of special characters
special_chars = ['!', '@', '#', '$', '&']

# Generate all permutations of the special characters
permutations = itertools.permutations(special_chars, len(special_chars))

# Generate and print all possible passwords
for perm in permutations:
    password = first_half + ''.join(perm)
    print(password)
